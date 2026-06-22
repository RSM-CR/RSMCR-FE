<script lang="ts">
    import { onMount } from "svelte";

    interface Tenant
    {
        tenantId: string,
        tenantName: string
    }

    let tenantSelector: HTMLElement;
    let selectorValue = $state("");

    async function getTenants() {
        try {
            const response = await fetch('http://localhost:8000/xero/tenants/get');
            if (!response.ok) throw new Error('Error al obtener tenants: ' + response.status);
            const data = await response.json();
            data.forEach((tenant: Tenant) => {
                const option = document.createElement('option');
                option.value = tenant.tenantId;
                option.textContent = tenant.tenantName;
                tenantSelector.appendChild(option);
            });
        } catch (error) {
            console.error('Error fetching tenants:', error);
        }
    }

    function selectTenants() {
        const tenantId = selectorValue;
        if (tenantId) {
            sendData(tenantId);
        } else {
            alert('Por favor, seleciona un Tenant')
        }
    }

    async function sendData(tenantId: string) {
        try {
            const response = await fetch(`http://localhost:8000/xero/tenants/post/${tenantId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
            });

            if (!response.ok) throw new Error('Error: ' + response.status);
            
            const resutl = await response.json();
            console.log('Respuesta del Servidor', resutl);
            window.location.replace("/apagar");
        } catch(error) {
            console.error('Error:', error);
        }
    }

    onMount(getTenants)
</script>

<div class="root">
    <div class="card">
        <div class="content">
            
            <h1>Selector de Tenant</h1>
            <p class="desc">Por favor, selecciona un tenant:</p>
            <select id="tenantSelector" bind:value={selectorValue} bind:this={tenantSelector}>
                <option value="">Selecciona un tenant</option>
            </select>
            <button onclick={selectTenants}>Seleccionar Tenant</button>
        </div>
    </div>
</div>

<style>
    .root {
        margin: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        position: relative;
    }

    .root::before {
        content: "";
        position: fixed;
        inset: -60px;
        background-image: url('$lib/assets/FondoTenants.jpg');
        background-size: cover;
        background-position: center;
        filter: blur(60px) brightness(0.9);
        z-index: -1;
    }

    .card {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 320px;
        border-radius: 24px;
        line-height: 1.6;
        z-index: 1;

        background: rgba(10, 60, 255, 0.25);
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        border: 1px solid rgba(10, 60, 255, 0.5);
        box-shadow:
            0 8px 32px rgba(10, 60, 255, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.4),
            inset 0 -1px 0 rgba(10, 60, 255, 0.2);
    }

    .card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 10%;
        width: 80%;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6), transparent);
        border-radius: 50%;
    }

    .card::after {
        content: "";
        position: absolute;
        inset: 0;
        border-radius: 24px;
        background: linear-gradient(
            135deg,
            rgba(10, 60, 255, 0.2) 0%,
            rgba(255, 255, 255, 0.05) 50%,
            rgba(10, 60, 255, 0.15) 100%
        );
        pointer-events: none;
    }

    .content {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 20px;
        padding: 36px;
        border-radius: 22px;
        color: #ffffff;
        background: transparent;
        width: 100%;
        box-sizing: border-box;
        transition: all 0.48s cubic-bezier(0.23, 1, 0.32, 1);
        position: relative;
        z-index: 1;
    }

    .content svg {
        width: 48px;
        height: 48px;
        flex-shrink: 0;
        filter: drop-shadow(0 2px 4px rgba(10, 60, 255, 0.4));
    }

    .content h1 {
        font-size: 20px;
        font-weight: 600;
        margin: 0;
        color: #fff;
        text-shadow: 0 1px 4px rgba(10, 60, 255, 0.5);
    }

    .content .desc {
        font-size: 14px;
        margin: 0;
        color: rgba(255, 255, 255, 0.85);
    }

    .content select {
        width: 100%;
        padding: 8px 12px;
        border-radius: 10px;
        border: 1px solid rgba(10, 60, 255, 0.5);
        font-size: 14px;
        background: rgba(10, 60, 255, 0.2);
        color: #fff;
        outline: none;
        cursor: pointer;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
    }

    .content select option {
        color: #111;
        background: #fff;
    }

    .content button {
        width: 100%;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.5);
        background: rgba(10, 60, 255, 0.35);
        color: #fff;
        font-size: 15px;
        font-weight: 600;
        cursor: pointer;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        transition: all 0.2s;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.4);
        text-shadow: 0 1px 3px rgba(0,0,0,0.3);
    }

    .content button:hover {
        background: rgba(10, 60, 255, 0.55);
        box-shadow:
            inset 0 1px 0 rgba(255,255,255,0.5),
            0 4px 16px rgba(10, 60, 255, 0.4);
    }
</style>