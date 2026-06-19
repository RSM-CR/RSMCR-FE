import { writable, type Readable } from 'svelte/store';

export interface WebSocketsFormat {
	type: string;
	payload: unknown;
}

const websocketMessagesStore = writable<WebSocketsFormat[]>([]);

export const websocketMessages: Readable<WebSocketsFormat[]> = websocketMessagesStore;

export function addMessage(message: WebSocketsFormat) {
	websocketMessagesStore.update((items) => [...items, message]);
}