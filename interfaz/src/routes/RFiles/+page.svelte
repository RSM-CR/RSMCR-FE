<script lang="ts">
	import { onMount } from 'svelte';
	import { slide } from 'svelte/transition';
	import { fetchRecentXml, type RecentXml } from '$lib/recent-xml.service';

	let showItems = $state(true);
	let i = $state(5);
	let xmls: RecentXml[] = $state([]);
	let loading = $state(true);

	onMount(async () => {
		xmls = await fetchRecentXml(10);
		loading = false;
	});
</script>

<div class="shell">
	<header>
		<h1>Panel de documentos recientes</h1>
	</header>

	<div class="divider"></div>

	<main>
		<div class="controls">
			<label class="toggle-label">
				<span class="toggle">
					<input type="checkbox" bind:checked={showItems} />
					<span class="slider-t"></span>
				</span>
				Mostrar documentos
			</label>

			<div class="range-wrap">
				<span>Número de elementos a mostrar</span>
				<input type="range" bind:value={i} min="1" max="10" step="1" />
			</div>
		</div>

		<div class="doc-list">
			{#if loading}
				<p>Cargando XML recientes...</p>
			{:else}
				{#if showItems}
					{#each xmls.slice(0, i) as doc}
						<div class="doc-row" transition:slide|global>
							<strong>{doc.name}</strong>
							<pre>{doc.content}</pre>
						</div>
					{/each}
					{#if xmls.length === 0}
						<p>No hay XML recientes en filedb/xero.</p>
					{/if}
				{/if}
			{/if}
		</div>
	</main>
</div>

<style>
	@import 'tailwindcss';

	.shell {
		min-height: 100vh;
		display: flex;
		flex-direction: column;
		background: #ffffff;
	}

	header {
		padding: 2rem 2rem 1.5rem;
		background: linear-gradient(135deg, #0c447c 0%, #0f6e56 100%);
	}

	header h1 {
		color: #e6f1fb;
		font-size: 1.4rem;
		font-weight: 500;
		margin: 0;
	}

	.divider {
		height: 6px;
		background: linear-gradient(135deg, #0c447c 0%, #0f6e56 100%);
		opacity: 0.35;
	}

	main {
		flex: 1;
		background: #ffffff;
	}

	.controls {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 1rem 1.5rem 0.75rem;
		border-bottom: 1px solid #eee;
	}

	.toggle-label {
		display: flex;
		align-items: center;
		gap: 8px;
		font-size: 0.85rem;
		color: #555;
		cursor: pointer;
		user-select: none;
	}

	.toggle {
		position: relative;
		width: 36px;
		height: 20px;
	}

	.toggle input {
		opacity: 0;
		width: 0;
		height: 0;
	}

	.slider-t {
		position: absolute;
		inset: 0;
		background: #b4b2a9;
		border-radius: 20px;
		transition: background 0.2s;
		cursor: pointer;
	}

	.slider-t::before {
		content: '';
		position: absolute;
		width: 14px;
		height: 14px;
		background: white;
		border-radius: 50%;
		left: 3px;
		top: 3px;
		transition: transform 0.2s;
	}

	.toggle input:checked + .slider-t {
		background: #1d9e75;
	}

	.toggle input:checked + .slider-t::before {
		transform: translateX(16px);
	}

	.range-wrap {
		display: flex;
		align-items: center;
		gap: 8px;
		font-size: 0.85rem;
		color: #555;
	}

	.range-wrap input[type='range'] {
		width: 100px;
		accent-color: #1d9e75;
	}

	.doc-list {
		min-height: 260px;
	}

	.doc-row {
		padding: 0.75rem 1.5rem;
		border-bottom: 1px solid #eee;
		font-size: 0.9rem;
		font-weight: 500;
		color: #111;
	}
</style>