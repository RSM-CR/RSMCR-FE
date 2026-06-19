<script lang="ts">
    import { Tab } from "../tab";

	interface Props {
		tabs?: Tab[];
	}

    let { tabs = [] }: Props = $props();
</script>

<nav>
    {#each tabs as tab}
        <ul>
            <a href={tab.ruta}>{tab.nombre}</a>
        </ul>
    {/each}
</nav>

<style>
    nav
    {
        display: flex;
        gap: 16px;
        padding: 8px;
    }
</style>