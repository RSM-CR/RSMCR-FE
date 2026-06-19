<script lang="ts">
    import NavBar from "$lib/components/NavBar.svelte";
    import { Tab } from "$lib/tab";
    import { resolve } from "$app/paths";
    import { onMount } from "svelte";
    import { connectWebSocket } from "$lib/websockets.service";

    onMount(() => {
        connectWebSocket()
    })

    const urlActual = resolve("/editor");

    const tabs = [new Tab("Vista simple", urlActual), new Tab("Editor XML", `${urlActual}/xml`)]

    let { children } = $props();
</script>

<NavBar tabs={tabs}/>
{@render children()}