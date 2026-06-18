async function getTenants() {
    try {
        const response = await fetch('http://localhost:8000/tenants');
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
        alert('Tenant selecionado ' + tenantid)
    } else {
        alert('Por favor, seleciona un Tenant')
    }
}

document.addEventListener('DOMContentLoaded', getTenants);
document.addEventListener('DOMContentLoaded', selectTenants)