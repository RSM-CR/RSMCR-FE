
<strong>Panel de documentos recientes</strong>
<br>
<br>
<br>
<script>
	import { slide } from 'svelte/transition';

	let items = ['XML 1', 'XML 2', 'XML 3', 'XML 4', 'XML 5', 'XML 6', 'XML 7', 'XML 8', 'XML 9', 'XML 10'];

	let showItems = $state(true);
	let i = $state(5);
</script>

<label>
	Mostrar documentos recientes
	<input type="checkbox" bind:checked={showItems} />
	
</label>
<br>
<br>
<label>
	Número de documentos a mostrar
	<br>
	<strong>1</strong><input type="range" bind:value={i} max="10"/><strong>10</strong> <!--El color de el checkbox y del range varía con respecto al color del escritorio del usuario. No se puede cambiar de ninguna manera.-->
</label>

{#if showItems}
	{#each items.slice(0, i) as item}
		<div transition:slide|global>
			{item}
		</div>
	{/each}
{/if}

<style>
	div {
		padding: 0.5em 0;
		border-top: 1px solid #eee;
	}
	@import 'tailwindcss';

	
</style>
