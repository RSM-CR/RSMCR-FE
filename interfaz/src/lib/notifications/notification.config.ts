import type { AppNotification, WebSocketsFormat } from "$lib/types/notifications.types";

interface NotificationTypeConfig {
    getTitle: (payload: any) => string;
    getMessage: (payload: any) => string;
    silent?: boolean;
}

const config: Record<string, NotificationTypeConfig> = {
    'CREATE': {
        getTitle: () => 'Nuevo Invoice',
        getMessage: (payload: any) => `Se creo el invoice #${payload?.id ?? ''}`,
    },
    'UPDATE': {
        getTitle: () => 'Invoice Actualizado',
        getMessage: (payload: any) => `El invoice ${payload?.id ?? ''} se a actualizado`
    }
};

const fallback: NotificationTypeConfig = {
    getTitle: (payload: any) => payload?.type ?? 'Notificacion',
    getMessage: (payload: any) => payload?.payload ?? 'Tienes una notificacion nueva'
};

export function buildNotification(message: WebSocketsFormat): AppNotification {
    const cfg = config[message.type] ?? fallback;

    return {
        id: message.id ?? crypto.randomUUID(),
        type: message.type,
        payload: message.payload,
        title: cfg.getTitle(message.payload),
        message: cfg.getMessage(message.payload),
        read: false,
        createdAt: message.date
    };
}

export function shouldPlaySound(type: string): boolean {
    return!(config[type]?.silent ?? false);
}