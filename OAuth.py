# Importamos la librería httpx para hacer llamadas HTTP
import httpx

# Estas son tus credenciales de Xero (las obtienes en su portal)
CLIENT_ID = "TU_CLIENT_ID"
CLIENT_SECRET = "TU_CLIENT_SECRET"

# URL donde Xero te va a devolver el "code"
REDIRECT_URI = "http://localhost:8000/callback"


# ==============================
# 1. GENERAR URL DE LOGIN
# ==============================
def get_auth_url():
    # Construimos la URL donde el usuario va a iniciar sesión en Xero
    url = (
        "https://login.xero.com/identity/connect/authorize"
        "?response_type=code"                      # indica que queremos un "code"
        f"&client_id={CLIENT_ID}"                  # tu client_id
        f"&redirect_uri={REDIRECT_URI}"            # donde Xero te redirige
        "&scope=openid profile email files offline_access"  # permisos
    )

    # Devolvemos la URL
    return url


# ==============================
# 2. INTERCAMBIAR CODE → TOKEN
# ==============================
async def get_token(code):
    # URL oficial de Xero para obtener tokens
    url = "https://identity.xero.com/connect/token"

    # Datos que enviamos en el POST
    data = {
        "grant_type": "authorization_code",  # tipo de OAuth
        "code": code,                        # el code que recibiste
        "redirect_uri": REDIRECT_URI         # debe coincidir con el anterior
    }

    # Creamos cliente HTTP
    async with httpx.AsyncClient() as client:
        # Hacemos POST con autenticación básica (client_id + secret)
        response = await client.post(
            url,
            data=data,
            auth=(CLIENT_ID, CLIENT_SECRET)
        )

    # Convertimos la respuesta a JSON
    return response.json()


# ==============================
# 3. OBTENER TENANT_ID
# ==============================
async def get_tenants(access_token):
    # Endpoint para obtener organizaciones
    url = "https://api.xero.com/connections"

    # Headers necesarios
    headers = {
        "Authorization": f"Bearer {access_token}"  # token de acceso
    }

    async with httpx.AsyncClient() as client:
        # Hacemos GET
        response = await client.get(url, headers=headers)

    # Devuelve lista de organizaciones (tenants)
    return response.json()


# ==============================
# 4. LLAMAR API (FILES)
# ==============================
async def get_folders(access_token, tenant_id):
    # Endpoint de la Files API
    url = "https://api.xero.com/files.xro/1.0/Folders"

    # Headers obligatorios para Xero
    headers = {
        "Authorization": f"Bearer {access_token}",  # quién eres
        "xero-tenant-id": tenant_id,                # qué empresa
        "Accept": "application/json"                # formato respuesta
    }

    async with httpx.AsyncClient() as client:
        # Llamada GET para obtener carpetas
        response = await client.get(url, headers=headers)

    # Retornamos los datos
    return response.json()