<script lang="ts">
	import { onMount } from 'svelte';
	import { connectWebSocket } from '$lib/websockets.service';
	import { unlockAudioContext } from '$lib/notifications/sound';
	import NotificationBell from '$lib/components/NotificationBell.svelte';
	import ToastContainer from '$lib/components/ToastContainer.svelte';
    import "../app.css";

	onMount(() => {
		connectWebSocket();

		const unlock = () => {
			unlockAudioContext();
			window.removeEventListener('pointerdown', unlock);
			window.removeEventListener('keydown', unlock);
		};

		window.addEventListener('pointerdown', unlock);
		window.addEventListener('keydown', unlock);
	});

	let { children } = $props();
</script>

<header class="app-header">
	<NotificationBell />
</header>

<ToastContainer />

<div class="root">
    {@render children()}
</div>
