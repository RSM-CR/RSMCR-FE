<!-- @component

## Funcionamiento del código

### En este código se añaden los datos que Xero no proporciona de manera manual 

Con este código se importan los datos extraídos anteriormente de un **python** y
se encarga de que las variables sean convertidas a un **XML** y las devuelvan como un **JSON**,
para finalmente poder añadir las variables que hagan falta de manera manual y al presionar el botón sean
añadidad automáticamente al XML.

-->

<script lang="ts">
    import type { Factura } from '$lib/factura';
    import { getContext } from 'svelte';

    const factura: Factura = getContext('factura');

    let codProducto = $state('');
    let codCabys = $state('');
    let unidMedida = $state('Unidad');

    let descripcion = $state('');
    let descuento = $state(0);
    let otrosImps = $state(0);

    let tipoTransaccion = $state('');
    let numVinSerie = $state('');

    let precioUnitario = $state(0);
    let cantidad = $state(0);

    let tipodoc = $state('');
    let condicionventa = $state('');
    let terminal = $state('');
    let sucursal = $state('');
    let moneda = $state('');
    let situacionenvio = $state('');
    let codigoactividad = $state('');
    let tipoidreceptor = $state('');
    let numcuentaemisor = $state('');
    let unidadMedidaGeneral = $state('');
    let provincia = $state('');
    let canton = $state('');
    let distrito = $state('');
    let otrassenas = $state('');
    let numdoc = $state('');

    // ── Líneas ya agregadas a la factura ────────────────────────────────────────
    let lineas = $state<any[]>([]);

    // ── Tab activo ────────────────────────────────────────────────────────────
    let tabActivo = $state('lineas'); // 'lineas' | 'otros'

    // ── Modal IVA ─────────────────────────────────────────────────────────────
    let modalIVA        = $state(false);
    let tipoIVA         = $state('');
    let tarifaIVA       = $state('');

    // Tipo 07
    let precioVenta07   = $state(0);
    let precioCompra07  = $state(0);

    // Tipo 08 REBU
    let precioNeto08    = $state(0);
    let modalidadRebu   = $state('');

    // Tipo 09
    let precioFabrica09 = $state(0);

    // Exoneración (solo tipo 01)
    let motivoExoneracion     = $state('');
    let numDocExoneracion     = $state('');
    let institucion           = $state('');
    let fechaExoneracion      = $state('');
    let porcentajeExoneracion = $state('');
    let articulo              = $state('');
    let inciso                = $state('');

    // ── Catálogos ─────────────────────────────────────────────────────────────
    const unidadesMedida = [
        'Unidad','Al','Cm','G','Kg','L','M','M2','M3','Ml','Mm','Oz','Pie','Pulg','Tonelada','Otro'
    ];

    const tiposTransaccion = [
        { value: '', label: 'Seleccione una opción' },
        { value: '01', label: '01 – Venta normal' },
        { value: '02', label: '02 – Consignación' },
        { value: '03', label: '03 – Donación' },
        { value: '04', label: '04 – Exportación' },
    ];

    const tiposIVA = [
        { value: '01', label: '01 – Impuesto al Valor Agregado' },
        { value: '07', label: '07 – IVA (Cálculo especial)' },
        { value: '08', label: '08 – IVA Régimen de Bienes Usados (factor)' },
        { value: '09', label: '09 – IVA cobrado a nivel de fábrica' },
    ];

    const tarifasIVA = [
        { value: '01', pct: 0,   label: '01 – Tarifa 0% (Exento)' },
        { value: '02', pct: 1,   label: '02 – Tarifa reducida 1%' },
        { value: '03', pct: 2,   label: '03 – Tarifa reducida 2%' },
        { value: '04', pct: 4,   label: '04 – Tarifa reducida 4%' },
        { value: '05', pct: 0,   label: '05 – Transitorio 0%' },
        { value: '06', pct: 4,   label: '06 – Transitorio 4%' },
        { value: '07', pct: 8,   label: '07 – Transitorio 8%' },
        { value: '08', pct: 13,  label: '08 – Tarifa general 13%' },
        { value: '09', pct: 0.5, label: '09 – Tarifa reducida 0.5%' },
    ];

    const factoresRebu = {
        '01': { factor: 0.1130, descripcion: 'Modalidad 1 – Comprado a contribuyente con IVA' },
        '02': { factor: 0.1130, descripcion: 'Modalidad 2 – Margen (venta − compra) × 13%' },
        '03': { factor: 0.1031, descripcion: 'Modalidad 3 – Factor sobre precio neto (DGT-R-034-2019)' },
    };

    const motivosExoneracion = [
        { value: '01', label: '01 – Compras autorizadas' },
        { value: '02', label: '02 – Ventas exentas a diplomáticos' },
        { value: '03', label: '03 – Autorizado por Ley Especial' },
        { value: '04', label: '04 – Exenciones Dirección General de Hacienda' },
        { value: '05', label: '05 – Transitorio V' },
        { value: '06', label: '06 – Transitorio IX' },
        { value: '07', label: '07 – Transitorio XVII' },
        { value: '99', label: '99 – Otros' },
    ];

    // ── Derivados ─────────────────────────────────────────────────────────────
    let subtotal = $derived(+(cantidad * precioUnitario).toFixed(2));

    // IVA tipo 01
    let tarifaSel    = $derived(tarifasIVA.find(t => t.value === tarifaIVA) ?? null);
    let pct01        = $derived(tarifaSel?.pct ?? 0);
    let montoIVA01   = $derived(+(subtotal * pct01 / 100).toFixed(2));

    // IVA tipo 07
    let diferencia07 = $derived(+(precioVenta07 - precioCompra07).toFixed(2));
    let montoIVA07   = $derived(+(diferencia07 * 0.13).toFixed(2));

    // IVA tipo 08
    let factorRebu   = $derived(factoresRebu[modalidadRebu as keyof typeof factoresRebu] ?? null);
    let montoIVA08   = $derived(factorRebu ? +(precioNeto08 * factorRebu.factor).toFixed(2) : 0);

    // IVA tipo 09
    let montoIVA09   = $derived(+(precioFabrica09 * 0.13).toFixed(2));

    // IVA efectivo (lo que se muestra en el campo IVA del formulario)
    let ivaCalculado = $derived(
        tipoIVA === '01' ? montoIVA01 :
        tipoIVA === '07' ? montoIVA07 :
        tipoIVA === '08' ? montoIVA08 :
        tipoIVA === '09' ? montoIVA09 : 0
    );

    // Exoneración
    let montoExonerado = $derived(
        porcentajeExoneracion
            ? +((subtotal * Number(porcentajeExoneracion)) / 100).toFixed(2)
            : 0
    );
    let ivaEfectivo = $derived(+(ivaCalculado - montoExonerado).toFixed(2));

    // Total línea
    // Antes se usaba "ivaEfectivo > 0" como condición, lo cual fallaba cuando
    // la exoneración era del 100% (ivaEfectivo daba 0 y caía al IVA sin exonerar).
    // Ahora preguntamos si HAY un porcentaje de exoneración cargado, sin importar el resultado.
    let totalLinea = $derived(
        +(subtotal - descuento + otrosImps + (porcentajeExoneracion ? ivaEfectivo : ivaCalculado)).toFixed(2)
    );

    let mostrarArtIns = $derived(['02','03','06','07','08'].includes(motivoExoneracion));

    // ── Acciones ──────────────────────────────────────────────────────────────
    function limpiarLinea() {
        codProducto = ''; codCabys = '';
        unidMedida = 'Unidad'; cantidad = 2.00; precioUnitario = 1000.00;
        descripcion = ''; descuento = 0.00; otrosImps = 0.00;
        tipoTransaccion = ''; numVinSerie = '';
        tipoIVA = ''; tarifaIVA = '';
        precioVenta07 = 0; precioCompra07 = 0;
        precioNeto08 = 0; modalidadRebu = '';
        precioFabrica09 = 0;
        motivoExoneracion = ''; numDocExoneracion = '';
        institucion = ''; fechaExoneracion = '';
        porcentajeExoneracion = ''; articulo = ''; inciso = '';
    }

    function agregarLinea() {
        lineas.push({
            codProducto,
            codCabys,
            unidMedida,
            cantidad,
            precioUnitario,
            descripcion,
            descuento,
            otrosImps,
            tipoTransaccion,
            numVinSerie,
            tipoIVA,
            tarifaIVA,
            porcentajeIVA: pct01,
            montoIVA: ivaCalculado,
            motivoExoneracion,
            numDocExoneracion,
            institucion,
            fechaExoneracion,
            porcentajeExoneracion,
            montoExonerado,
            totalLinea
        });
        limpiarLinea();
    }

    function eliminarLinea(index: number) {
        lineas.splice(index, 1);
    }

    function onChangeTipoIVA() {
        tarifaIVA = ''; modalidadRebu = '';
        motivoExoneracion = ''; porcentajeExoneracion = '';
    }


async function enviarDatos(){
    if (lineas.length === 0) {
        alert('Agregá al menos una línea antes de generar el XML.');
        return;
    }

    const respuesta = await fetch("http://localhost:8000/generar-xml", {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify({
            metododepago: factura.Encabezado.MediosPago.TiposMedioPago,
            tipodoc,
            condicionventa,
            terminal,
            sucursal,
            moneda,
            situacionenvio,
            codigoactividad,
            tipoidreceptor,
            numcuentaemisor,
            unidadmedida: unidadMedidaGeneral,
            provincia,
            canton,
            distrito,
            otrassenas,
            numdoc,
            lineas
        })
    });
    const resultado = await respuesta.json();
    console.log(resultado.mensaje);
}

</script>

<div class="panel-root">
    <div class="datos-generales">
    <div class="panel-title">Editor de XML</div>

    <div class="grid-4">
        <div class="field">
            <label class="field__label" for="metodo-pago">Método de pago:</label>
            <input bind:value={factura.Encabezado.MediosPago.TiposMedioPago} id="metodo-pago" class="inp" placeholder="Método de pago..." />
        </div>
        <div class="field">
            <label class="field__label" for="num-cuenta-emisor">N.° cuenta emisor:</label>
            <input bind:value={numcuentaemisor} id="num-cuenta-emisor" class="inp" placeholder="Número cuenta emisor..." />
        </div>
        <div class="field">
            <label class="field__label" for="tipo-doc">Tipo de documento:</label>
            <input bind:value={tipodoc} id="tipo-doc" class="inp" placeholder="Tipo de documento..." />
        </div>
        <div class="field">
            <label class="field__label" for="num-doc">N.° de documento:</label>
            <input bind:value={numdoc} id="num-doc" class="inp" placeholder="Número de documento..." />
        </div>
        <div class="field">
            <label class="field__label" for="unidad-medida-top">Unidad de medida:</label>
            <input bind:value={unidadMedidaGeneral} id="unidad-medida-top" class="inp" placeholder="Unidad de Medida" />
        </div>
        <div class="field">
            <label class="field__label" for="condicion-venta">Condición de venta:</label>
            <input bind:value={condicionventa} id="condicion-venta" class="inp" placeholder="Condición de venta..." />
        </div>
        <div class="field">
            <label class="field__label" for="provincia">Provincia:</label>
            <input bind:value={provincia} id="provincia" class="inp" placeholder="Provincia..." />
        </div>
        <div class="field">
            <label class="field__label" for="sucursal">Sucursal:</label>
            <input bind:value={sucursal} id="sucursal" class="inp" placeholder="Sucursal..." />
        </div>
        <div class="field">
            <label class="field__label" for="canton">Cantón:</label>
            <input bind:value={canton} id="canton" class="inp" placeholder="Cantón..." />
        </div>
        <div class="field">
            <label class="field__label" for="terminal">Terminal:</label>
            <input bind:value={terminal} id="terminal" class="inp" placeholder="Terminal..." />
        </div>
        <div class="field">
            <label class="field__label" for="distrito">Distrito:</label>
            <input bind:value={distrito} id="distrito" class="inp" placeholder="Distrito..." />
        </div>
        <div class="field">
            <label class="field__label" for="moneda">Moneda:</label>
            <input bind:value={moneda} id="moneda" class="inp" placeholder="Moneda..." />
        </div>
        <div class="field">
            <label class="field__label" for="otras-senas">Otras señas:</label>
            <input bind:value={otrassenas} id="otras-senas" class="inp" placeholder="Otras Señas..." />
        </div>
        <div class="field">
            <label class="field__label" for="situacion-envio">Situación del envío:</label>
            <input bind:value={situacionenvio} id="situacion-envio" class="inp" placeholder="Situación del envío..." />
        </div>
        <div class="field">
            <label class="field__label" for="codigo-actividad">Código de actividad:</label>
            <input bind:value={codigoactividad} id="codigo-actividad" class="inp" placeholder="Código de Actividad..." />
        </div>
        <div class="field">
            <label class="field__label" for="tipo-id-receptor">Tipo id. Receptor:</label>
            <input bind:value={tipoidreceptor} id="tipo-id-receptor" class="inp" placeholder="Tipo de identificación del Receptor..." />
        </div>
    </div>
    </div>

    <div class="tabs">
        <button
            class="tab {tabActivo === 'lineas' ? 'tab--active' : ''}"
            onclick={() => tabActivo = 'lineas'}>
            LÍNEAS DETALLE
        </button>
        <button
            class="tab {tabActivo === 'otros' ? 'tab--active' : ''}"
            onclick={() => tabActivo = 'otros'}>
            OTROS CARGOS
        </button>
    </div>

    {#if tabActivo === 'lineas'}
    <div class="lineas-body">

        <div class="grid-4">
            <div class="field">
                <div class="field__label">
                    <span>Cód. Producto:</span>
                    <button class="link-btn">⊕ Agregar más cód.</button>
                </div>
                <div class="input-icon-wrap">
                    <input bind:value={codProducto} class="inp" placeholder="" />
                    <button class="icon-btn icon-btn--green">🔍</button>
                </div>
            </div>

            <div class="field">
                <label class="field__label" for="cod-cabys">Cód. CABYS:</label>
                <input bind:value={codCabys} id="cod-cabys" class="inp" placeholder="" />
            </div>

            <div class="field">
                <div class="field__label">
                    <span>Unid. Medida:</span>
                    <button class="link-btn">⊕ Unid. Comercial</button>
                </div>
                <select bind:value={unidMedida} class="inp inp--select">
                    {#each unidadesMedida as u}
                        <option value={u}>{u}</option>
                    {/each}
                </select>
            </div>
        </div>

        <div class="grid-3-wide">
            <div class="field">
                <label class="field__label" for="cantidad">Cantidad:</label>
                <input bind:value={cantidad} id="cantidad" type="number" step="0.01" class="inp" />
            </div>

            <div class="field">
                <label class="field__label" for="precio-unitario">Precio unitario:</label>
                <input bind:value={precioUnitario} id="precio-unitario" type="number" step="0.01" class="inp" />
            </div>

            <div class="field field--span2">
                <label class="field__label" for="descripcion">Descripción:</label>
                <input bind:value={descripcion} id="descripcion" class="inp" placeholder="" />
            </div>
        </div>

        <div class="grid-4">
            <div class="field">
                <div class="field__label">
                    <span>Descuento:</span>
                    <button class="link-btn">✏ Editar</button>
                </div>
                <input bind:value={descuento} type="number" step="0.01" class="inp" />
            </div>

            <div class="field">
                <div class="field__label">
                    <span>Otros imps:</span>
                    <button class="link-btn">✏ Editar</button>
                </div>
                <input bind:value={otrosImps} type="number" step="0.01" class="inp" />
            </div>

            <div class="field">
                <div class="field__label">
                    <span>I.V.A:</span>
                    <button class="link-btn" onclick={() => modalIVA = true}>✏ Editar</button>
                </div>
                <input
                    value={ivaCalculado > 0 || tipoIVA
                        ? (ivaEfectivo >= 0 && porcentajeExoneracion ? ivaEfectivo : ivaCalculado).toFixed(2)
                        : '0.00'}
                    class="inp inp--readonly"
                    readonly />
            </div>

            <div class="field">
                <label class="field__label" for="total-linea">Total línea:</label>
                <input value={totalLinea.toFixed(2)} id="total-linea" class="inp inp--readonly" readonly />
            </div>
        </div>

        <div class="grid-3-bottom">
            <div class="field">
                <button class="btn-combo">Lista de productos del combo</button>
            </div>

            <div class="field">
                <label class="field__label" for="tipo-transaccion">Tipo transacción<span class="opcional">(Opcional):</span></label>
                <select bind:value={tipoTransaccion} id="tipo-transaccion" class="inp inp--select">
                    {#each tiposTransaccion as t}
                        <option value={t.value}>{t.label}</option>
                    {/each}
                </select>
            </div>

            <div class="field">
                <label class="field__label" for="num-vin-serie">Número VIN o Serie<span class="opcional">(Opcional):</span></label>
                <div class="input-icon-wrap">
                    <input bind:value={numVinSerie} id="num-vin-serie" class="inp" placeholder="" />
                    <button class="icon-btn icon-btn--green">+</button>
                </div>
            </div>
        </div>

        <div class="actions-row">
            <div></div>
            <div></div>
            <button class="btn-limpiar" onclick={limpiarLinea}>Limpiar Línea</button>
            <button class="btn-agregar" onclick={agregarLinea}>Agregar Línea</button>
        </div>

        {#if lineas.length > 0}
        <div class="lineas-tabla-wrap">
            <table class="lineas-tabla">
                <thead>
                    <tr>
                        <th>Producto</th>
                        <th>Cant.</th>
                        <th>Precio unit.</th>
                        <th>IVA</th>
                        <th>Total</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {#each lineas as linea, i}
                    <tr>
                        <td>{linea.codProducto || linea.descripcion || '(sin código)'}</td>
                        <td>{linea.cantidad}</td>
                        <td>₡{Number(linea.precioUnitario).toFixed(2)}</td>
                        <td>₡{Number(linea.montoIVA).toFixed(2)}</td>
                        <td>₡{Number(linea.totalLinea).toFixed(2)}</td>
                        <td>
                            <button class="btn-eliminar-linea" onclick={() => eliminarLinea(i)}>✕</button>
                        </td>
                    </tr>
                    {/each}
                </tbody>
            </table>
        </div>
        {/if}

        <div class="generar-row">
            <button class="btn-generar" onclick={enviarDatos} disabled={lineas.length === 0}>
                Generar XML ({lineas.length} línea{lineas.length === 1 ? '' : 's'})
            </button>
        </div>

    </div>
    {/if}

    {#if tabActivo === 'otros'}
    <div class="lineas-body">
        <p class="otros-placeholder">Sección de Otros Cargos — próximamente.</p>
    </div>
    {/if}
</div>

{#if modalIVA}
    <div
        class="modal-overlay"
        role="button"
        tabindex="-1"
        onclick={() => modalIVA = false}
        onkeydown={(e) => e.key === 'Escape' && (modalIVA = false)}>
            <div class="modal" role="dialog" tabindex="-1" onclick={(e) => e.stopPropagation()} onkeydown={(e) => e.stopPropagation()}>

            <div class="modal-section">
                <label class="modal-label" for="tipo-iva">Tipo de I.V.A:</label>
                <select bind:value={tipoIVA} id="tipo-iva" onchange={onChangeTipoIVA} class="modal-select">
                    <option value="" disabled selected>Seleccione tipo...</option>
                    {#each tiposIVA as t}
                        <option value={t.value}>{t.label}</option>
                    {/each}
                </select>
            </div>

            {#if tipoIVA === '01'}
                <div class="modal-sep"><span>IVA General</span></div>
                <div class="modal-grid">
                    <div class="modal-field modal-field--full">
                        <label class="modal-label" for="tarifa-iva">Tarifa de I.V.A:</label>
                        <select bind:value={tarifaIVA} id="tarifa-iva" class="modal-select">
                            <option value="" disabled selected>Seleccione tarifa...</option>
                            {#each tarifasIVA as t}
                                <option value={t.value}>{t.label}</option>
                            {/each}
                        </select>
                    </div>
                    <div class="modal-field">
                        <label class="modal-label" for="base-imponible">Base imponible:</label>
                        <input class="modal-inp modal-inp--ro" id="base-imponible" value="₡{subtotal.toFixed(2)}" readonly />
                    </div>
                    <div class="modal-field">
                        <label class="modal-label" for="tarifa-aplicada">Tarifa aplicada:</label>
                        <input class="modal-inp modal-inp--ro" id="tarifa-aplicada" value="{pct01}%" readonly />
                    </div>
                    <div class="modal-field">
                        <label class="modal-label" for="monto-iva-01">Monto I.V.A:</label>
                        <input class="modal-inp modal-inp--ro" id="monto-iva-01" value="₡{montoIVA01.toFixed(2)}" readonly />
                    </div>
                    <div class="modal-field">
                        <label class="modal-label" for="total-con-iva-01">Total con I.V.A:</label>
                        <input class="modal-inp modal-inp--ro" id="total-con-iva-01" value="₡{(subtotal + montoIVA01).toFixed(2)}" readonly />
                    </div>
                </div>

                <div class="modal-sep"><span>Exoneración (opcional)</span></div>
                <div class="modal-grid">
                    <div class="modal-field modal-field--full">
                        <label class="modal-label" for="motivo-exoneracion">Motivo de exoneración:</label>
                        <select bind:value={motivoExoneracion} id="motivo-exoneracion" class="modal-select">
                            <option value="" selected>— Sin exoneración —</option>
                            {#each motivosExoneracion as m}
                                <option value={m.value}>{m.label}</option>
                            {/each}
                        </select>
                    </div>

                    {#if mostrarArtIns}
                        <div class="modal-field">
                            <label class="modal-label" for="num-articulo">N.° artículo:</label>
                            <input bind:value={articulo} id="num-articulo" type="number" class="modal-inp" placeholder="Artículo..." />
                        </div>
                        <div class="modal-field">
                            <label class="modal-label" for="num-inciso">N.° inciso:</label>
                            <input bind:value={inciso} id="num-inciso" type="number" class="modal-inp" placeholder="Inciso..." />
                        </div>
                    {/if}

                    {#if motivoExoneracion}
                        <div class="modal-field modal-field--full">
                            <label class="modal-label" for="num-doc-exoneracion">N.° documento exoneración (17 car.):</label>
                            <input bind:value={numDocExoneracion} id="num-doc-exoneracion" maxlength="17" class="modal-inp" placeholder="Número de documento..." />
                        </div>
                        <div class="modal-field">
                            <label class="modal-label" for="institucion">Institución emisora:</label>
                            <input bind:value={institucion} id="institucion" class="modal-inp" placeholder="Institución..." />
                        </div>
                        <div class="modal-field">
                            <label class="modal-label" for="fecha-exoneracion">Fecha exoneración:</label>
                            <input bind:value={fechaExoneracion} id="fecha-exoneracion" type="date" class="modal-inp" />
                        </div>
                        <div class="modal-field">
                            <label class="modal-label" for="porcentaje-exonerar">Porcentaje a exonerar (%):</label>
                            <input bind:value={porcentajeExoneracion} id="porcentaje-exonerar" type="number" min="0" max="100" class="modal-inp" placeholder="0 – 100" />
                        </div>
                        {#if porcentajeExoneracion}
                            <div class="modal-field">
                                <label class="modal-label" for="monto-exonerado">Monto exonerado:</label>
                                <input class="modal-inp modal-inp--ro" id="monto-exonerado" value="₡{montoExonerado.toFixed(2)}" readonly />
                            </div>
                            <div class="modal-field">
                                <label class="modal-label" for="iva-efectivo">I.V.A efectivo:</label>
                                <input class="modal-inp modal-inp--ro" id="iva-efectivo" value="₡{ivaEfectivo.toFixed(2)}" readonly />
                            </div>
                        {/if}
                    {/if}
                </div>
            {/if}

            {#if tipoIVA === '07'}
                <div class="modal-sep"><span>IVA – Cálculo Especial (art. 31 LIVA)</span></div>
                <p class="modal-nota">Base imponible = Precio de venta − Precio de compra. Tarifa: 13%.</p>
                <div class="modal-grid">
                    <div class="modal-field">
                        <label class="modal-label" for="precio-venta-07">Precio de venta (₡):</label>
                        <input bind:value={precioVenta07} id="precio-venta-07" type="number" step="0.01" class="modal-inp" placeholder="0.00" />
                    </div>
                    <div class="modal-field">
                        <label class="modal-label" for="precio-compra-07">Precio de compra (₡):</label>
                        <input bind:value={precioCompra07} id="precio-compra-07" type="number" step="0.01" class="modal-inp" placeholder="0.00" />
                    </div>
                    <div class="modal-field">
                        <label class="modal-label" for="diferencia-07">Diferencia (base):</label>
                        <input class="modal-inp modal-inp--ro" id="diferencia-07" value="₡{diferencia07.toFixed(2)}" readonly />
                    </div>
                    <div class="modal-field">
                        <label class="modal-label" for="monto-iva-07">Monto I.V.A (13%):</label>
                        <input class="modal-inp modal-inp--ro" id="monto-iva-07" value="₡{montoIVA07.toFixed(2)}" readonly />
                    </div>
                    <div class="modal-field modal-field--full">
                        <label class="modal-label" for="total-con-iva-07">Total con I.V.A:</label>
                        <input class="modal-inp modal-inp--ro" id="total-con-iva-07" value="₡{(precioVenta07 + montoIVA07).toFixed(2)}" readonly />
                    </div>
                </div>
            {/if}

            {#if tipoIVA === '08'}
                <div class="modal-sep"><span>IVA – Régimen Especial Bienes Usados (REBU)</span></div>
                <p class="modal-nota">IVA = Precio neto de venta × Factor DGT (Res. DGT-R-034-2019).</p>
                <div class="modal-grid">
                    <div class="modal-field modal-field--full">
                        <label class="modal-label" for="modalidad-rebu">Modalidad REBU:</label>
                        <select bind:value={modalidadRebu} id="modalidad-rebu" class="modal-select">
                            <option value="" disabled selected>Seleccione modalidad...</option>
                            {#each Object.entries(factoresRebu) as [k, v]}
                                <option value={k}>{v.descripcion}</option>
                            {/each}
                        </select>
                    </div>
                    <div class="modal-field modal-field--full">
                        <label class="modal-label" for="precio-neto-08">Precio neto de venta (₡):</label>
                        <input bind:value={precioNeto08} id="precio-neto-08" type="number" step="0.01" class="modal-inp" placeholder="0.00" />
                    </div>
                    {#if modalidadRebu}
                        <div class="modal-field">
                            <label class="modal-label" for="factor-aplicado">Factor aplicado:</label>
                            <input class="modal-inp modal-inp--ro" id="factor-aplicado" value="{factorRebu?.factor}" readonly />
                        </div>
                        <div class="modal-field">
                            <label class="modal-label" for="monto-iva-08">Monto I.V.A:</label>
                            <input class="modal-inp modal-inp--ro" id="monto-iva-08" value="₡{montoIVA08.toFixed(2)}" readonly />
                        </div>
                        <div class="modal-field modal-field--full">
                            <label class="modal-label" for="total-con-iva-08">Total con I.V.A:</label>
                            <input class="modal-inp modal-inp--ro" id="total-con-iva-08" value="₡{(precioNeto08 + montoIVA08).toFixed(2)}" readonly />
                        </div>
                    {/if}
                </div>
            {/if}

            {#if tipoIVA === '09'}
                <div class="modal-sep"><span>IVA cobrado a nivel de fábrica</span></div>
                <p class="modal-nota">El IVA (13%) ya fue cobrado por el fabricante/importador. Se registra para el XML.</p>
                <div class="modal-grid">
                    <div class="modal-field modal-field--full">
                        <label class="modal-label" for="precio-fabrica-09">Precio ex-fábrica (₡):</label>
                        <input bind:value={precioFabrica09} id="precio-fabrica-09" type="number" step="0.01" class="modal-inp" placeholder="0.00" />
                    </div>
                    <div class="modal-field">
                        <label class="modal-label" for="iva-incluido-09">I.V.A incluido (13%):</label>
                        <input class="modal-inp modal-inp--ro" id="iva-incluido-09" value="₡{montoIVA09.toFixed(2)}" readonly />
                    </div>
                    <div class="modal-field">
                        <label class="modal-label" for="precio-consumidor">Precio al consumidor:</label>
                        <input class="modal-inp modal-inp--ro" id="precio-consumidor" value="₡{(precioFabrica09 + montoIVA09).toFixed(2)}" readonly />
                    </div>
                </div>
            {/if}

            <div class="modal-actions">
                <button class="btn-modal-cancel" onclick={() => modalIVA = false}>Cancelar</button>
                <button class="btn-modal-ok" onclick={() => modalIVA = false}>Aceptar</button>
            </div>
        </div>
    </div>
{/if}

<style>

    /* ── Reset / base ────────────────────────────────────────────────────────── */
    *, *::before, *::after { box-sizing: border-box; }
    :global(body) { margin: 0; background: #f0f0f0; font-family: Arial, sans-serif; font-size: 13px; color: #333; }

    /* ── Panel raíz (usado tanto arriba como abajo) ─────────────────────────── */
    .panel-root {
        background: #fff;
        border: 1px solid #ccc;
        border-radius: 4px;
        margin: 20px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.12);
    }

    .datos-generales {
        padding: 16px 18px 18px;
        border-bottom: 1px solid #ccc;
    }

    .panel-title {
        font-size: 14px;
        font-weight: 700;
        color: #2a7a2a;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        border-bottom: 2px solid #ccc;
        padding-bottom: 8px;
        margin-bottom: 14px;
    }

    /* ── Tabs ────────────────────────────────────────────────────────────────── */
    .tabs {
        display: flex;
        border-bottom: 2px solid #ccc;
    }

    .tab {
        padding: 10px 22px;
        border: none;
        background: #e8e8e8;
        font-size: 13px;
        font-weight: 700;
        color: #555;
        cursor: pointer;
        border-right: 1px solid #ccc;
        border-bottom: 2px solid transparent;
        margin-bottom: -2px;
        transition: background 0.15s;
        letter-spacing: 0.03em;
    }
    .tab:hover { background: #ddd; }
    .tab--active {
        background: #fff;
        color: #2a7a2a;
        border-top: 2px solid #4caf50;
        border-bottom: 2px solid #fff;
    }

    /* ── Cuerpo del tab ──────────────────────────────────────────────────────── */
    .lineas-body {
        padding: 16px 18px 12px;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    /* ── Grids de filas ──────────────────────────────────────────────────────── */
    .grid-4 {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 12px;
        align-items: end;
    }

    .datos-generales .grid-4 {
        grid-template-columns: 1fr 1fr;
        row-gap: 12px;
    }

    .grid-3-wide {
        display: grid;
        grid-template-columns: 0.7fr 0.7fr 2fr;
        gap: 12px;
        align-items: end;
    }

    .grid-3-bottom {
        display: grid;
        grid-template-columns: 0.9fr 1fr 1fr;
        gap: 12px;
        align-items: end;
    }

    .actions-row {
        display: grid;
        grid-template-columns: 0.9fr 1fr 1fr 1fr;
        gap: 12px;
        align-items: center;
        margin-top: 2px;
    }

    /* ── Field ───────────────────────────────────────────────────────────────── */
    .field {
        display: flex;
        flex-direction: column;
        gap: 3px;
    }

    .field__label {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 12px;
        color: #444;
        font-weight: 600;
        min-height: 16px;
    }

    .link-btn {
        background: none;
        border: none;
        color: #2a7a2a;
        font-size: 11px;
        cursor: pointer;
        padding: 0;
        font-weight: 600;
    }
    .link-btn:hover { text-decoration: underline; }

    .info-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 16px; height: 16px;
        background: #2196f3;
        color: #fff;
        border-radius: 50%;
        font-size: 10px;
        font-weight: 700;
        cursor: default;
    }

    .opcional { color: #888; font-weight: 400; margin-left: 2px; }

    /* ── Inputs ──────────────────────────────────────────────────────────────── */
    .inp {
        width: 100%;
        height: 32px;
        border: 1px solid #bbb;
        border-radius: 3px;
        padding: 0 8px;
        font-size: 13px;
        color: #333;
        background: #fff;
        outline: none;
        transition: border-color 0.15s;
    }
    .inp:focus { border-color: #4caf50; box-shadow: 0 0 0 2px rgba(76,175,80,0.18); }

    .inp::placeholder { color: #999; }

    .inp--readonly {
        background: #f5f5f5;
        color: #555;
        cursor: default;
    }

    .inp--select { cursor: pointer; padding-right: 4px; }

    .input-icon-wrap {
        display: flex;
        gap: 0;
    }
    .input-icon-wrap .inp {
        border-radius: 3px 0 0 3px;
        flex: 1;
    }

    .icon-btn {
        border: 1px solid #bbb;
        border-left: none;
        border-radius: 0 3px 3px 0;
        width: 32px;
        cursor: pointer;
        font-size: 14px;
        display: flex; align-items: center; justify-content: center;
        transition: background 0.15s;
        background: #e8e8e8;
        flex-shrink: 0;
    }
    .icon-btn--green { background: #4caf50; color: #fff; border-color: #4caf50; }
    .icon-btn--green:hover { background: #388e3c; }
    .icon-btn:hover { background: #d0d0d0; }

    /* ── Botón combo ─────────────────────────────────────────────────────────── */
    .btn-combo {
        height: 32px;
        background: #9e9e9e;
        color: #fff;
        border: none;
        border-radius: 3px;
        font-size: 12px;
        font-weight: 600;
        cursor: pointer;
        width: 100%;
        letter-spacing: 0.02em;
        transition: background 0.15s;
        margin-top: 18px; /* alinea con la última fila */
    }
    .btn-combo:hover { background: #757575; }

    /* ── Botones acción ──────────────────────────────────────────────────────── */
    .btn-limpiar {
        height: 34px;
        background: #9e9e9e;
        color: #fff;
        border: none;
        border-radius: 3px;
        font-size: 13px;
        font-weight: 700;
        cursor: pointer;
        width: 100%;
        transition: background 0.15s;
    }
    .btn-limpiar:hover { background: #757575; }

    .btn-agregar {
        height: 34px;
        background: #4caf50;
        color: #fff;
        border: none;
        border-radius: 3px;
        font-size: 13px;
        font-weight: 700;
        cursor: pointer;
        width: 100%;
        transition: background 0.15s;
    }
    .btn-agregar:hover { background: #388e3c; }

    /* ── Placeholder otros cargos ────────────────────────────────────────────── */
    .otros-placeholder {
        color: #888;
        font-style: italic;
        text-align: center;
        padding: 40px 0;
    }

    /* ── Tabla de líneas agregadas ───────────────────────────────────────────── */
    .lineas-tabla-wrap {
        overflow-x: auto;
        border: 1px solid #ddd;
        border-radius: 3px;
        margin-top: 4px;
    }

    .lineas-tabla {
        width: 100%;
        border-collapse: collapse;
        font-size: 12px;
    }

    .lineas-tabla th {
        background: #f0f0f0;
        text-align: left;
        padding: 6px 10px;
        font-weight: 700;
        color: #444;
        border-bottom: 1px solid #ddd;
    }

    .lineas-tabla td {
        padding: 6px 10px;
        border-bottom: 1px solid #eee;
        color: #333;
    }

    .lineas-tabla tr:last-child td { border-bottom: none; }

    .btn-eliminar-linea {
        background: none;
        border: none;
        color: #c0392b;
        cursor: pointer;
        font-size: 13px;
        font-weight: 700;
        padding: 0 4px;
    }
    .btn-eliminar-linea:hover { color: #922b21; }

    /* ── Botón Generar XML ───────────────────────────────────────────────────── */
    .generar-row {
        display: flex;
        justify-content: flex-end;
        margin-top: 4px;
    }

    .btn-generar {
        height: 36px;
        padding: 0 20px;
        background: #2a7a2a;
        color: #fff;
        border: none;
        border-radius: 3px;
        font-size: 13px;
        font-weight: 700;
        cursor: pointer;
        transition: background 0.15s;
    }
    .btn-generar:hover:not(:disabled) { background: #1f5c1f; }
    .btn-generar:disabled {
        background: #bbb;
        cursor: not-allowed;
    }

    /* ══ MODAL ════════════════════════════════════════════════════════════════ */
    .modal-overlay {
        position: fixed;
        inset: 0;
        background: rgba(0,0,0,0.45);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 1000;
    }

    .modal {
        background: #fff;
        border-radius: 6px;
        width: 560px;
        max-width: 96vw;
        max-height: 90vh;
        overflow-y: auto;
        box-shadow: 0 8px 32px rgba(0,0,0,0.22);
        padding: 0 0 20px;
    }

    .modal-section {
        padding: 14px 18px 0;
        display: flex;
        flex-direction: column;
        gap: 4px;
    }

    .modal-sep {
        display: flex; align-items: center; gap: 8px;
        margin: 14px 18px 4px;
        color: #2a7a2a; font-size: 12px; font-weight: 700;
        text-transform: uppercase; letter-spacing: 0.05em;
    }
    .modal-sep::before, .modal-sep::after {
        content: ''; flex: 1; height: 1px; background: #c8e6c9;
    }

    .modal-nota {
        font-size: 12px; color: #666; font-style: italic;
        margin: 0 18px 6px; line-height: 1.4;
    }

    .modal-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        padding: 6px 18px 0;
    }

    .modal-field {
        display: flex; flex-direction: column; gap: 3px;
    }
    .modal-field--full { grid-column: 1 / -1; }

    .modal-label {
        font-size: 12px; font-weight: 600; color: #444;
    }

    .modal-inp {
        height: 30px;
        border: 1px solid #bbb;
        border-radius: 3px;
        padding: 0 8px;
        font-size: 13px;
        color: #333;
        outline: none;
    }
    .modal-inp:focus { border-color: #4caf50; box-shadow: 0 0 0 2px rgba(76,175,80,0.18); }
    .modal-inp--ro { background: #f5f5f5; color: #555; cursor: default; }

    .modal-select {
        height: 30px;
        border: 1px solid #bbb;
        border-radius: 3px;
        padding: 0 6px;
        font-size: 13px;
        color: #333;
        outline: none;
        cursor: pointer;
        background: #fff;
    }
    .modal-select:focus { border-color: #4caf50; }

    .modal-actions {
        display: flex;
        justify-content: flex-end;
        gap: 10px;
        padding: 16px 18px 0;
    }

    .btn-modal-cancel {
        padding: 7px 22px;
        background: #9e9e9e; color: #fff;
        border: none; border-radius: 3px;
        font-size: 13px; font-weight: 600; cursor: pointer;
    }
    .btn-modal-cancel:hover { background: #757575; }

    .btn-modal-ok {
        padding: 7px 22px;
        background: #4caf50; color: #fff;
        border: none; border-radius: 3px;
        font-size: 13px; font-weight: 600; cursor: pointer;
    }
    .btn-modal-ok:hover { background: #388e3c; }
</style>