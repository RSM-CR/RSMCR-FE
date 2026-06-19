import { websocketMessages } from "$lib/stores/websockets";

let socket: WebSocket;

export function connectWebSocket() {
    if (socket) return;

    socket = new WebSocket('app://localhost:8000/app');

    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);

        websocketMessages.update((items) => [...items, data]);
    };
}