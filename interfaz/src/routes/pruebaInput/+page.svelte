<script lang="ts">
    import Input from "$lib/components/Input.svelte";

    let codigoProducto = $state("");
    let codigoCABYS = $state("");
    let medioPago = $state("");
    let numcuentaemisor = $state("");
    let tipodoc = $state("");
    let numdoc = $state("");
    let unidadmedida = $state("");
    let condicionventa = $state("");
    let provincia = $state("");
    let sucursal = $state("");
    let canton = $state("");
    let terminal = $state("");
    let distrito = $state("");
    let precioUnitario = $state("");
    let cantidad = $state("");
    let moneda = $state("");
    let otrasSenas = $state("");
    let situacionenvio = $state("");
    let codigoactividad = $state("");
    let tipoidreceptor = $state("");
    let codMedicamentos = $state("");
    let descuento = $state("");
    let otrosImps = $state("");
    let IVA = $state("");
    let totalinea = $state("");
    let tipoTransaccion = $state("");
    let vin = $state("");
</script>



<Input titulo="Código del producto:" bind:value={codigoProducto} />
<Input titulo="Número de cuenta del emisor:" bind:value={numcuentaemisor} />
<Input titulo="Tipo de documento:" bind:value={tipodoc} />
<Input titulo="Número de documento:" bind:value={numdoc} />
<Input titulo="Unidad de medida:" bind:value={unidadmedida} />
<Input titulo="Condición de venta:" bind:value={condicionventa} />
<Input titulo="Provincia:" bind:value={provincia} />
<Input titulo="Sucursal:" bind:value={sucursal} />
<Input titulo="Cantón:" bind:value={canton} />
<Input titulo="Terminal:" bind:value={terminal} />
<Input titulo="Distrito:" bind:value={distrito} />
<Input titulo="Precio Unitario:" bind:value={precioUnitario} />
<Input titulo="Cantidad:" bind:value={cantidad} />
<Input titulo="Moneda:" bind:value={moneda} />
<Input titulo="Descripción:" bind:value={otrasSenas} />
<Input titulo="Situación de envío:" bind:value={situacionenvio} />
<Input titulo="Código de actividad:" bind:value={codigoactividad} />
<Input titulo="Tipo de identificación del receptor:" bind:value={tipoidreceptor} />
<Input titulo="Código de Medicamentos:" bind:value={codMedicamentos} />
<Input titulo="Descuento:" bind:value={descuento} />
<Input titulo="Código CABYS:" bind:value={codigoCABYS} />
<Input titulo="Método de pago:" bind:value={medioPago} />
<Input titulo="Otros Impuestos:" bind:value={otrosImps} />
<Input titulo="IVA:" bind:value={IVA} />
<Input titulo="Total de la línea:" bind:value={totalinea} />
<Input titulo="Tido de transacción:" bind:value={tipoTransaccion} />
<Input titulo="VIN o Serie:" bind:value={vin} />