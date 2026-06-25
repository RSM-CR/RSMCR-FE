import { writable } from "svelte/store";

const STORAGE_KEY = 'app:notifications:sound-enabled';

function loadInit(): boolean {
    if (typeof window === 'undefined') return true;

    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        return raw === null ? true : raw === 'true';
    } catch {
        return true;
    }
}

function persist(value: boolean) {
    if (typeof window === 'undefined') return;

    try {
        localStorage.setItem(STORAGE_KEY, String(value));
    } catch (error) {
        console.error(`Error al intentar guardar las preferencis de sonido en el almacenamiento local: ${error}`);
    }
}

function createSoundPreferenceStore() {
    const store = writable<boolean>(loadInit());

    return {
        subscribe: store.subscribe,
        toggle() {
            store.update((enabled) => {
                const next = !enabled;
                persist(next);
                return next
            });
        }
    }
}

export const soundEnabled = createSoundPreferenceStore();