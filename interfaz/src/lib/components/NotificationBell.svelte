<script lang="ts">
	import { notifications, unreadCount } from '$lib/stores/notifications.store';
	import { connectionStatus } from '$lib/websocket-connection';
	import { soundEnabled } from '$lib/stores/sound-preference.store';

	let open = $state(false);

	function toggle() {
		open = !open;
	}

	function handleClickOutside(event: MouseEvent) {
		const target = event.target as HTMLElement;
		if (!target.closest('.notification-bell')) open = false;
	}
</script>

<svelte:window onclick={handleClickOutside} />

<div class="notification-bell">
	<button onclick={toggle} aria-label="Notificaciones">
		🔔
		<span
			class="status-dot"
			class:open={$connectionStatus === 'open'}
			class:reconnecting={$connectionStatus === 'reconnecting'}
			class:closed={$connectionStatus === 'closed'}
			title={$connectionStatus}
		></span>
		{#if $unreadCount > 0}
			<span class="badge">{$unreadCount}</span>
		{/if}
	</button>

	{#if open}
		<div class="dropdown">
			<div class="dropdown-header">
				<span>Notificaciones</span>
				<div class="header-actions">
					<button
						class="icon-btn"
						onclick={() => soundEnabled.toggle()}
						aria-label={$soundEnabled ? 'Silenciar notificaciones' : 'Activar sonido'}
					>
						{$soundEnabled ? '🔊' : '🔇'}
					</button>
					{#if $unreadCount > 0}
						<button class="link" onclick={() => notifications.markAllAsRead()}>
							Marcar todas como leídas
						</button>
					{/if}
				</div>
			</div>

			{#if $notifications.length === 0}
				<p class="empty">No tienes notificaciones todavía</p>
			{:else}
				<ul>
					{#each $notifications as notification (notification.id)}
						<li class:unread={!notification.read}>
							<button onclick={() => notifications.markAsRead(notification.id)}>
								<strong>{notification.title}</strong>
								<p>{notification.message}</p>
								<time>{new Date(notification.createdAt).toLocaleString()}</time>
							</button>
						</li>
					{/each}
				</ul>
			{/if}
		</div>
	{/if}
</div>

<style>
	.notification-bell {
		position: relative;
	}
	.notification-bell > button {
		position: relative;
		background: none;
		border: none;
		font-size: 20px;
		cursor: pointer;
	}
	.status-dot {
		position: absolute;
		bottom: -1px;
		right: -1px;
		width: 8px;
		height: 8px;
		border-radius: 50%;
		background: #bbb;
		border: 1.5px solid white;
	}
	.status-dot.open {
		background: #2ecc71;
	}
	.status-dot.reconnecting {
		background: #f1c40f;
	}
	.status-dot.closed {
		background: #e74c3c;
	}
	.badge {
		position: absolute;
		top: -4px;
		right: -4px;
		background: #d63031;
		color: white;
		border-radius: 999px;
		font-size: 11px;
		line-height: 1;
		padding: 2px 5px;
	}
	.dropdown {
		position: absolute;
		right: 0;
		top: calc(100% + 8px);
		width: 320px;
		max-height: 420px;
		overflow-y: auto;
		background: white;
		border: 1px solid #e2e2e2;
		border-radius: 10px;
		box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
		z-index: 1000;
	}
	.dropdown-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 12px 14px;
		border-bottom: 1px solid #eee;
		font-weight: 600;
	}
	.header-actions {
		display: flex;
		align-items: center;
		gap: 8px;
	}
	.icon-btn {
		background: none;
		border: none;
		cursor: pointer;
		font-size: 14px;
		padding: 2px;
	}
	.link {
		background: none;
		border: none;
		color: #1a73e8;
		font-size: 13px;
		font-weight: 400;
		cursor: pointer;
	}
	.empty {
		padding: 24px 14px;
		text-align: center;
		color: #888;
		font-size: 14px;
	}
	ul {
		list-style: none;
		margin: 0;
		padding: 0;
	}
	li button {
		width: 100%;
		text-align: left;
		background: none;
		border: none;
		border-bottom: 1px solid #f3f3f3;
		padding: 12px 14px;
		cursor: pointer;
	}
	li.unread button {
		background: #eef5ff;
	}
	li p {
		margin: 2px 0;
		font-size: 13px;
		color: #555;
	}
	li time {
		font-size: 11px;
		color: #999;
	}
</style>