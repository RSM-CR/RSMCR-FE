async function getTenants() {
    try {
        const response = await fetch('http://localhost:8000/getTenants');
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
    const tenantid = document.getElementById('tenantSelector').value
    if (tenantid) {
        localStorage.setItem('tenantId', tenantid)
        sendData({ tenantid })
        alert('Tenant selecionado ' + tenantid)
    } else {
        alert('Por favor, seleciona un Tenant')
    }
}

async function sendData(data) {
    try {
        const response = await fetch('http://localhost:8000/postTenants', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) throw new Error('Error: ' + response.status);
        
        const resutl = await response.json();
        console.log('Respuesta del Servidor', resutl);
    } catch(error) {
        console.error('Error:', error);
    }
}

document.addEventListener('DOMContentLoaded', getTenants);