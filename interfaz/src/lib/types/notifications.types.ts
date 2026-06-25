export interface WebSocketsFormat{
    type: string,
    payload: unknown,
    date: string,
    id?: string
}

export interface AppNotification {
    id: string;
    type: string;
    payload: unknown;
    title: string;
    message: string;
    read: boolean;
    createdAt: string;
}