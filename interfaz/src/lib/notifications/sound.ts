const MIN_INTERVAL_MS = 250;

let audioContext: AudioContext | undefined;
let lastPlayedAt = 0;

function getAudioContext(): AudioContext {
    if (!audioContext) {
        const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
        audioContext = new AudioContextClass();
    }
    return audioContext;
}

export function unlockAudioContext() {
    const ctx = getAudioContext();
    if (ctx.state === 'suspended') {
        ctx.resume().catch((error) => {`Hubo un error en el desbloqueo del audio: ${error}`});
    }
}

function playTone(ctx: AudioContext, frequency: number, startTime: number, duration: number) {
    const oscillator = ctx.createOscillator();
    const gain = ctx.createGain();

    oscillator.type = 'sine';
    oscillator.frequency.setValueAtTime(frequency, startTime);

    gain.gain.setValueAtTime(0.0001, startTime);
    gain.gain.exponentialRampToValueAtTime(0.25, startTime + 0.01);
    gain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);

    oscillator.connect(gain);
    gain.connect(ctx.destination);

    oscillator.start(startTime);
    oscillator.stop(startTime + duration);
}

export function playNotificationSound() {
    const now = Date.now();
    if (now - lastPlayedAt < MIN_INTERVAL_MS) return;
    lastPlayedAt = now;

    try {
        const ctx = getAudioContext();
        if (ctx.state === 'suspended') ctx.resume().catch((error) => {`Hubo un error en la reproduccion del audio de la notificacion: ${error}`});

        const t0 = ctx.currentTime;
        playTone(ctx, 880, t0, 0.12);
        playTone(ctx, 1175, t0 + 0.1, 0.18);
    } catch (error) {
        console.error(`Web Audio no disponible o bloqueado: ${error}`)
    }
}