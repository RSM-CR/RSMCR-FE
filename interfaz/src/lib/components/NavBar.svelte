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

    ul {
        display: flex;
        gap: 16px;
<<<<<<< HEAD
        justify-content: center;
        align-items: center;
        font-size: 18px;
        list-style: none;
        padding: 0;
        margin: 0 auto;
        margin-top: 20px;
        margin-bottom: 20px;
        color: #ffffff;
        border-radius: 10px;
        background-color: #4A8EAC;
        width: 300px;
=======
        padding: 8px;
        list-style-type: none;
>>>>>>> 101aa1e5adc4d8bd05c26530012e87d5f13496ec
    }
</style>