<script lang="ts">
	import { notifications } from '$lib/stores/notifications.store';
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p>
<p>Mira <a href="./RFiles">mi pagina</a></p>

<h2>Notificaciones recibidas (debug)</h2>
{#each $notifications as notification (notification.id)}
	<p>[{notification.type}] {notification.title} — {notification.message}</p>
	<pre>{JSON.stringify(notification.payload, null, 2)}</pre>
{/each}