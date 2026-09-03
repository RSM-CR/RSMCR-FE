<script lang="ts">
	import { notifications } from '$lib/stores/notifications.store';
</script>

<h1>Inicio de Sesión</h1>


<div class="button-container">
	<a href="./login_admin" class="start-button">Iniciar como Administrador</a>
</div>

<div class="button-container">
	<a href="./login_guest" class="start-button">Iniciar como Usuario</a>
</div>


{#each $notifications as notification (notification.id)}
	<p>[{notification.type}] {notification.title} — {notification.message}</p>
	<pre>{JSON.stringify(notification.payload, null, 2)}</pre>
{/each}

<style>
	.button-container {
		display: flex;
		justify-content: center;
		align-items: center;
		margin: 40px 0;
	}

	h1 {
		text-align: center;
		margin-top: 40px;
		font-size: 36px;
		color: #333;
	}
	.start-button {
		display: inline-block;
		padding: 14px 32px;
		background-color: #4CAF50;
		color: white;
		text-decoration: none;
		border-radius: 8px;
		font-size: 18px;
		font-weight: 600;
		cursor: pointer;
		transition: background-color 0.2s ease;
	}

	.start-button:hover {
		background-color: #45a049;
	}
</style>
