import { writable } from "svelte/store"

export interface WebSocketsFormat {
    type: string,
    payload: any
}

export const websocketMessages = writable<WebSocketsFormat[]>([]);