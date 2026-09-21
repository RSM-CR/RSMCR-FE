<!-- Login.svelte -->
<script>
  import { writable } from 'svelte/store';

  // Estado de login
  let username = '';
  let password = '';
  let role = '';
  let error = '';

  // Simulación de credenciales
  const mockUser = {
    username: 'admin',
    password: '1234'
  };

  // Función de manejo del login
  function handleLogin() {
    if (username === mockUser.username && password === mockUser.password) {
      error = '';
      alert('¡Inicio de sesión exitoso!');
      // Aquí puedes redirigir a otra ruta o mostrar contenido protegido
    } else {
      error = 'Usuario o contraseña incorrectos';
    }
  }
</script>

<style>
  :root {
    --verde: #2e7d32;
    --verde-claro: #4CAF50;
    --celeste: #008CBA;
    --celeste-claro: #4FC3F7;
    --gris-texto: #333;
    --gris-borde: #ddd;
  }

  .login-container {
    max-width: 340px;
    margin: 50px auto;
    padding: 28px;
    border: 1px solid var(--gris-borde);
    border-radius: 12px;
    box-shadow: 2px 4px 16px rgba(0, 0, 0, 0.08);
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    background-color: #fff;
  }

  h2 {
    text-align: center;
    color: var(--verde);
    font-weight: 600;
    letter-spacing: 0.5px;
    margin-bottom: 20px;
  }

  .field {
    margin-bottom: 16px;
  }

  label {
    display: block;
    font-size: 0.85em;
    font-weight: 600;
    color: var(--gris-texto);
    margin-bottom: 6px;
    padding-left: 8px;
    border-left: 3px solid var(--celeste);
    letter-spacing: 0.3px;
  }

  input {
    width: 100%;
    padding: 10px 12px;
    margin: 0;
    box-sizing: border-box;
    border: 1px solid var(--gris-borde);
    border-radius: 6px;
    font-size: 0.95em;
    font-family: inherit;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
  }

  input:focus {
    outline: none;
    border-color: var(--celeste-claro);
    box-shadow: 0 0 0 3px rgba(79, 195, 247, 0.2);
  }

  button {
    font-family: inherit;
    font-weight: 600;
    letter-spacing: 0.3px;
    cursor: pointer;
    transition: opacity 0.2s ease, transform 0.1s ease;
  }

  button:hover {
    opacity: 0.9;
  }

  button:active {
    transform: scale(0.98);
  }

  .submit-btn {
    width: 100%;
    padding: 12px;
    margin-top: 8px;
    background-color: var(--verde-claro);
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 1em;
  }

  .adminbtn {
    display: flex;
    align-items: center;
    gap: 10px;
    width: 100%;
  }

  .admin-left {
    background-color: var(--verde-claro);
    color: white;
    border: 2px solid transparent;
    padding: 10px 20px;
    border-radius: 6px;
    width: 50%;
  }

  .admin-left.active {
    border-color: var(--verde);
    box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.3);
  }

  .admin-right {
    background-color: var(--celeste);
    color: white;
    border: 2px solid transparent;
    padding: 10px 20px;
    border-radius: 6px;
    width: 50%;
  }

  .admin-right.active {
    border-color: var(--celeste-claro);
    box-shadow: 0 0 0 2px rgba(0, 140, 186, 0.3);
  }

  .error {
    color: #d32f2f;
    background-color: #fdecea;
    padding: 8px 10px;
    border-radius: 6px;
    font-size: 0.85em;
    margin: 12px 0;
    border-left: 3px solid #d32f2f;
  }
</style>

<div class="login-container">
  <h2>Iniciar Sesión</h2>

  <div class="field">
    <label for="username">Correo electrónico</label>
    <input type="text" id="username" placeholder="ejemplo@dominio.com" bind:value={username} />
  </div>

  <div class="field">
    <label for="password">Contraseña</label>
    <input type="password" id="password" placeholder="Contraseña" bind:value={password} />
  </div>

  <div class="field">
    <label for="role">Rol de Administrador</label>
    <div class="adminbtn" id="role">
      <button
        class="admin-left"
        class:active={role === 'admin'}
        on:click={() => (role = 'admin')}
      >
        Administrador
      </button>
      <button
        class="admin-right"
        class:active={role === 'user'}
        on:click={() => (role = 'user')}
      >
        Gerente
      </button>
    </div>
  </div>

  {#if error}
    <div class="error">{error}</div>
  {/if}

  <button class="submit-btn" on:click={handleLogin}>Ingresar</button>
</div>