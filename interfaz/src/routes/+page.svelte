<script lang="ts">
    import { websocketMessages } from '$lib/stores/websockets.store'
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p>
<p>Mira <a href="./RFiles">mi pagina</a></p>

{#each $websocketMessages as message}
    <p>{message.type}</p>
    <pre>{JSON.stringify(message.payload, null, 2)}</pre>
{/each}