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
  .login-container {
    max-width: 300px;
    margin: 50px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
  }
  input {
    width: 100%;
    padding: 8px;
    margin: 8px 0;
    box-sizing: border-box;
  }
  button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
  }

  .admin-left{
    background-color: #008CBA;
    color: white;
    border: none;



    width: 40%;
    cursor: pointer;
  }

  adminbtn{
    display: flex;

    align-items: center;
    gap: 10px;

    WIDTH: 100%;
    HEIGHT: 100%;
  }

  .admin-right{
    background-color: #008CBA;
    color: white;
    border: none;


    width: 40%;
    cursor: pointer;

  }

  .error {
    color: red;
    font-size: 0.9em;
  }
</style>

<div class="login-container">
  <h2>Iniciar Sesión</h2>
  <div>
    <label for="username">Correo electrónico:</label>
    <input type="text" placeholder="ejemplo@dominio.com" bind:value={username} />
  </div>
  <div>
    <label for="password">Contraseña:</label>
    <input type="password" id="password" placeholder="Contraseña" bind:value={password} />
  </div>
  <div>
    <label for="role">Rol de Administrador:</label>
    <div class="adminbtn">
        <button class="admin-left" on:click={() => role = 'admin'}>Administrador</button>
        <br>
        <button class="admin-right" on:click={() => role = 'user'}>Gerente</button>
    </div>
    
  </div>
  {#if error}
    <div class="error">{error}</div>
  {/if}
  <button on:click={handleLogin}>Ingresar</button>
</div>