import { readonly, writable, type Readable } from "svelte/store";

export type ConnectionStatus = 'connecting' | 'open' | 'reconnecting' | 'closed';

const WS_URL = 'ws://localhost:8000/app';
const BASE_RECONNECT_DELAY_MS = 1000;
const MAX_RECONNECT_DELAY_MS = 30000;

const statusStore = writable<ConnectionStatus>('connecting');

export const connectionStatus: Readable<ConnectionStatus> = readonly(statusStore);

type RawMessageListener = (data: unknown) => void;

let socket: WebSocket | undefined;
let reconnectAttempts = 0;
let reconnectTimeout: ReturnType<typeof setTimeout> | undefined;
let manuallyClosed = false;
let listener: RawMessageListener | undefined;

function sheludeReconnect() {
    const delay = Math.min(BASE_RECONNECT_DELAY_MS * 2 ** reconnectAttempts, MAX_RECONNECT_DELAY_MS);
    reconnectAttempts++;
    reconnectTimeout = setTimeout(openSocket, delay)
}

function openSocket() {
    statusStore.set(reconnectAttempts === 0 ? 'connecting' : 'reconnecting')

    socket = new WebSocket(WS_URL)

    socket.onopen = () => {
        reconnectAttempts = 0;
        statusStore.set('open');
    };

    socket.onmessage = (event) => {
        listener?.(JSON.parse(event.data));
    };

    socket.onclose = () => {
        socket = undefined;
        statusStore.set('closed');

        if (!manuallyClosed) sheludeReconnect();
    };

    socket.onerror = () => {
        socket?.close();
    }
}

export function onMessage(callback: RawMessageListener) {
    listener = callback;
}

export function connectWebSocket() {
    if (socket) return;

    manuallyClosed = false
    clearTimeout(reconnectTimeout);
    openSocket();
}

export function disconnectWebSocket() {
    manuallyClosed = true;
    clearTimeout(reconnectTimeout);
    socket?.close();
    socket = undefined;
}