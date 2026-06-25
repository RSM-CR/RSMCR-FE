import { writable } from "svelte/store";
import type { AppNotification } from "$lib/types/notifications.types";

const TOAST_DURATION_MS = 5000;

function createToastStore() {
    const store = writable<AppNotification[]>([]);

    return {
        subscribe: store.subscribe,
        push(notification: AppNotification) {
            store.update((items) => [...items, notification]);

            setTimeout(() => {
                store.update((items) => items.filter((n) => n.id !== notification.id));
            }, TOAST_DURATION_MS)
        },
        dismiss(id: string) {
            store.update((items) => items.filter((n) => n.id !== id));
        }
    };
}

export const toasts = createToastStore();