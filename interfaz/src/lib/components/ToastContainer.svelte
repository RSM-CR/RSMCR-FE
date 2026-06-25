<script lang="ts">
	import { toasts } from '$lib/stores/toasts.store';
	import { notifications } from '$lib/stores/notifications.store';
	import { fly } from 'svelte/transition';

	function open(id: string) {
		notifications.markAsRead(id);
		toasts.dismiss(id);
	}
</script>

<div class="toast-container">
	{#each $toasts as toast (toast.id)}
		<div class="toast" transition:fly={{ x: 60, duration: 200 }}>
			<button class="body" onclick={() => open(toast.id)}>
				<strong>{toast.title}</strong>
				<p>{toast.message}</p>
			</button>
			<button class="close" aria-label="Cerrar" onclick={() => toasts.dismiss(toast.id)}>
				×
			</button>
		</div>
	{/each}
</div>

<style>
	.toast-container {
		position: fixed;
		top: 16px;
		right: 16px;
		display: flex;
		flex-direction: column;
		gap: 8px;
		z-index: 2000;
	}
	.toast {
		display: flex;
		align-items: flex-start;
		gap: 8px;
		background: white;
		border: 1px solid #e2e2e2;
		border-radius: 10px;
		box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
		min-width: 260px;
		max-width: 320px;
	}
	.body {
		flex: 1;
		text-align: left;
		background: none;
		border: none;
		cursor: pointer;
		padding: 12px 4px 12px 14px;
	}
	.body p {
		margin: 2px 0 0;
		font-size: 13px;
		color: #555;
	}
	.close {
		background: none;
		border: none;
		cursor: pointer;
		font-size: 16px;
		color: #999;
		padding: 8px 12px;
	}
</style>