<script lang="ts">
    import NavBar from "$lib/components/NavBar.svelte";
    import { Tab } from "$lib/tab";
    import { resolve } from "$app/paths";

    const urlActual = resolve("/editor");

    const tabs = [new Tab("Editor Automático", urlActual), new Tab("Editor JSON", `${urlActual}/json`)]

    let { children } = $props();
</script>

<NavBar tabs={tabs}/>

{@render children()}
