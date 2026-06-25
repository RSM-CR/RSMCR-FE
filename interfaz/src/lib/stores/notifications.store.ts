import { writable, derived, get, readable, type Readable } from "svelte/store";
import type { AppNotification } from "$lib/types/notifications.types";
import { read } from "$app/server";

const MAX_HISTORY = 100;
const STORAGE_KEY = 'app:notifications';

function loadFromStorage(): AppNotification[] {
    if (typeof window === 'undefined') return [];

    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        return raw ? JSON.parse(raw) : [];
    } catch(error) {
        console.error(`Error durente la recuperacion de las notificciones almacenadas en el almacenamiento local: ${error}`)
        return[]
    }
}

function saveToStorage(items: AppNotification[]) {
    if (typeof window === 'undefined') return;

    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
    } catch (error) {
        console.error(`Error durente el almacenamiento de las notificaciones en el almacenamiento local, almacenamiento lleno o deshabilitado: ${error}`)
    }
}

function createNotificationsStore() {
    const store = writable<AppNotification[]>(loadFromStorage())

    function mutate(updater: (items: AppNotification[]) => AppNotification[]) {
        store.update((items) => {
            const next = updater(items);
            saveToStorage(next);
            return next
        });
    }

    return {
        subscribe: store.subscribe,
        has(id: string) {
            return get(store).some((n) => n.id === id);
        },
        add(notification: AppNotification) {
            mutate((items) => [notification, ...items].slice(0, MAX_HISTORY));
        },
        markAsRead(id: string) {
            mutate((items) => items.map((n) => (n.id === id ? {...n, read: true} : n)));
        },
        markAllAsRead() {
            mutate((items) => items.map((n) => ({...n, read: true})));
        },
        remove(id: string) {
            mutate((items) => items.filter((n) => n.id !== id));
        },
        clear() {
            mutate(() => []);
        }
    };
}

export const notifications = createNotificationsStore();

export const unreadCount: Readable<number> = derived(
    notifications,
    ($notifications) => $notifications.filter((n) => !n.read).length
);