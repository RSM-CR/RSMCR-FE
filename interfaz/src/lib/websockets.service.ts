import { get } from 'svelte/store';
import { onMessage, connectWebSocket, disconnectWebSocket } from './websocket-connection';
import { notifications } from './stores/notifications.store';
import { toasts } from './stores/toasts.store';
import { soundEnabled } from './stores/sound-preference.store';
import { buildNotification, shouldPlaySound } from './notifications/notification.config';
import { playNotificationSound } from './notifications/sound';
import type { WebSocketsFormat } from './types/notifications.types';
import { handlers } from 'svelte/legacy';

export { connectWebSocket, disconnectWebSocket };

function handleIncomingMessage(message: WebSocketsFormat) {
	const notification = buildNotification(message);

	if (notifications.has(notification.id)) return;

	notifications.add(notification);
	toasts.push(notification);

	if (get(soundEnabled) && shouldPlaySound(message.type)) {
		playNotificationSound();
	}
}

onMessage((data) => {
	if (typeof (data as {type?: unknown})?.type === 'string') {
		handleIncomingMessage(data as WebSocketsFormat);
	}
})