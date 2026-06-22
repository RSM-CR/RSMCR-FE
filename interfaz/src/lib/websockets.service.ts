import { addMessage, type WebSocketsFormat } from '$lib/stores/websockets.store';

let socket: WebSocket | undefined;

export function connectWebSocket() {

	if (socket) return;

	socket = new WebSocket(
		'ws://localhost:8000/app'
	);

	socket.onmessage = (event) => {

		const data = JSON.parse(event.data);

		if (
			typeof data.type === 'string'
		) {
			addMessage(data as WebSocketsFormat);
		}
	};
}