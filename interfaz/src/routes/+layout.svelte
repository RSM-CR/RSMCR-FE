<script lang="ts">
    import { onMount } from "svelte";
    import { connectWebSocket } from "$lib/websockets.service";

    onMount(() => {
        connectWebSocket()
    })
    
    let { children } = $props();
</script>

{@render children()}