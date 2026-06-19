<script lang="ts">
    import { Tab } from "../tab";

	interface Props {
		tabs?: Tab[];
	}

    let { tabs = [] }: Props = $props();
</script>

<nav>
<ul>
    {#each tabs as tab}
        <li>
            <a href={tab.ruta}>{tab.nombre}</a>
        </li>
    {/each}
</ul>
</nav>

<style>
    ul
    {
        display: flex;
        gap: 16px;
        padding: 8px;
    }
</style>