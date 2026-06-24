<script lang="ts">
    import "../app.css";
    import { onMount } from "svelte";
    import { connectWebSocket } from "$lib/websockets.service";

    onMount(() => {
        connectWebSocket()
    })
    
    let { children } = $props();
</script>

<div class="root">
    {@render children()}
</div>