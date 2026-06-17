import logging
import httpx
from servidor.secretos import obtener_entorno
from xero.auth import obtener_token

logger = logging.getLogger(__name__)
_entorno = obtener_entorno()


async def fetch_xero_resource(resource_url: str) -> dict | None:
    try:
        token = obtener_token()
        tenant_id = _entorno.ID_TENANT_XERO

        async with httpx.AsyncClient() as client:
            resp = await client.get(
                resource_url,
                headers={
                    "Authorization": f"Bearer {token['access_token']}",
                    "Xero-Tenant-Id": tenant_id,
                    "Accept": "application/json",
                },
            )
            resp.raise_for_status()
            return resp.json()
    except httpx.HTTPStatusError as e:
        logger.error("Error HTTP al obtener recurso: %s — %s", e.response.status_code, e.response.text)
        return None
    except Exception as e:
        logger.error("Error inesperado al obtener recurso: %s", e)
        return None


async def handle_invoice_create(event: dict) -> None:
    resource_url = event.get("resourceUrl")
    if not resource_url:
        logger.error("Evento sin resourceUrl: %s", event)
        return
        
    data = await fetch_xero_resource(event["resourceUrl"])
    if not data:
        return
    for invoice in data.get("Invoices", []):
        logger.info("Nueva factura — Número: %s | Estado: %s | Total: %s %s",
            invoice.get("InvoiceNumber"), invoice.get("Status"),
            invoice.get("Total"), invoice.get("CurrencyCode"))

async def handle_invoice_update(event: dict) -> None:
    resource_url = event.get("resourceUrl")
    if not resource_url:
        logger.error("Evento sin resourceUrl: %s", event)
        return
    
    data = await fetch_xero_resource(event["resourceUrl"])
    if not data:
        return
    for invoice in data.get("Invoices", []):
        logger.info("Factura actualizada — Número: %s | Estado: %s",
            invoice.get("InvoiceNumber"), invoice.get("Status"))


EVENT_HANDLERS = {
    ("INVOICE", "CREATE"):  handle_invoice_create,
    ("INVOICE", "UPDATE"):  handle_invoice_update,
}


async def process_webhook_events(payload: dict) -> None:
    events = payload.get("events", [])
    if not events:
        logger.info("Webhook de verificación recibido (Intent to Receive)")
        return

    logger.info("Procesando %d evento(s)", len(events))
    for event in events:
        logger.info("Evento recibido: %s", event)
        logger.info(
        "Categoría=%s | Tipo=%s | ResourceId=%s",
        event.get("eventCategory"),
        event.get("eventType"),
        event.get("resourceId")
        )
        category = event.get("eventCategory")
        event_type = event.get("eventType")
        handler = EVENT_HANDLERS.get((category, event_type))

        if handler:
            try:
                await handler(event)
            except Exception as e:
                logger.error("Error en handler %s %s: %s", category, event_type, e)
        else:
            logger.warning("Sin handler para: %s %s", category, event_type)