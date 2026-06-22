async function getTenants() {
    try {
        const response = await fetch('http://localhost:8000/xero/tenants/get');
        if (!response.ok) throw new Error('Error al obtener tenants: ' + response.status);
        const data = await response.json();
        const tenantSelect = document.getElementById('tenantSelector');
        data.forEach(tenant => {
            const option = document.createElement('option');
            option.value = tenant.tenantId;
            option.textContent = tenant.tenantName;
            tenantSelect.appendChild(option);
        });
    } catch (error) {
        console.error('Error fetching tenants:', error);
    }
}

function selectTenants() {
    const tenantId = document.getElementById('tenantSelector').value
    if (tenantId) {
        sendData(tenantId);
    } else {
        alert('Por favor, seleciona un Tenant')
    }
}

async function sendData(tenantId) {
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

document.addEventListener('DOMContentLoaded', getTenants);