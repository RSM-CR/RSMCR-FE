<script>
    let metododepago = $state('');
    let tipodoc = $state('');
    let condicionventa = $state('');
    let terminal = $state('');
    let sucursal = $state('');
    let moneda = $state('');
    let situacionenvio = $state('');
    let codigoactividad = $state('');
    let tipoidreceptor = $state('');
    let numcuentaemisor = $state('');
    let unidadmedida = $state('');
    let provincia = $state('');
    let canton = $state('');
    let distrito = $state('');
    let otrassenas = $state('');
    let numdoc = $state('hola');

    let mostrarIVA = $state(false);
    let motivoExoneracion = $state('');
    let numDocExoneracion = $state('');
    let institucion = $state('');
    let fechaExoneracion = $state('');
    let porcentajeExoneracion = $state('');
    let articulo = $state('');
    let inciso = $state('');
    let condicion = $state(false);
    let tipoIVA = $state('');
    let tarifaIVA = $state('');

    const motivosExoneracion = [
        { value: '01', label: '01 - Compras autorizadas' },
        { value: '02', label: '02 - Ventas exentas a diplomáticos' },
        { value: '03', label: '03 - Autoconsumo' },
        { value: '04', label: '04 - Ventas a diplomáticos' },
        { value: '05', label: '05 - Zona Franca' },
        { value: '06', label: '06 - Turismo' },
        { value: '07', label: '07 - Reciclaje' },
        { value: '08', label: '08 - Zona Franca (Régimen especial)' },
        { value: '09', label: '09 - Servicios complementarios exportación' },
        { value: '10', label: '10 - Órganos municipales' },
        { value: '11', label: '11 - Exención DGH - Autorización impuesto local' },
        { value: '99', label: '99 - Otros' },
    ];

    const tiposIVA = [
        { value: '01', label: 'Impuesto al valor agregado' },
        { value: '02', label: 'I.V.A (Cálculo especial)' },
        { value: '03', label: 'I.V.A régimen de bienes usados (factor)' },
        { value: '04', label: 'I.V.A cobrado a nivel de fábrica' },
    ];

    const tarifasIVA = [
        { value: '01', label: 'Tarifa 0% (Artículo 32, num 1, RLIVA)' },
        { value: '02', label: 'Tarifa reducida 1%' },
        { value: '03', label: 'Tarida reducida 2%' },
        { value: '04', label: 'Tarifa reducida 4%' },
        { value: '05', label: 'Tarifa general 13%' },
        { value: '06', label: 'Tarifa reducida 0.5%' },
        { value: '07', label: 'Tarifa Exenta' },
        { value: '08', label: 'Tarifa 0% sin derecho a crédito' },
    ];

    function mostrarArtIns() {
        if (['02', '03', '06', '07', '08'].includes(motivoExoneracion)) {
            condicion = true;
        } else {
            condicion = false;
        }
    }
</script>

<div class="contenedor">
    <div class="header">
        <p class="titulo">Editor de XML</p>
    </div>

    <div class="inputs1">
        <div class="informacion"><input bind:value={metododepago} placeholder="Método de pago..." /></div>
        <div class="informacion"><input bind:value={numcuentaemisor} placeholder="Número cuenta emisor..." /></div>
        <div class="informacion"><input bind:value={tipodoc} placeholder="Tipo de documento..." /></div>
        <div class="informacion"><input bind:value={numdoc} placeholder="Número de documento..." /></div>
        <div class="informacion"><input bind:value={unidadmedida} placeholder="Unidad de Medida" /></div>
        <div class="informacion"><input bind:value={condicionventa} placeholder="Condición de venta..." /></div>
        <div class="informacion"><input bind:value={provincia} placeholder="Provincia..." /></div>
        <div class="informacion"><input bind:value={sucursal} placeholder="Sucursal..." /></div>
        <div class="informacion"><input bind:value={canton} placeholder="Cantón..." /></div>
        <div class="informacion"><input bind:value={terminal} placeholder="Terminal..." /></div>
        <div class="informacion"><input bind:value={distrito} placeholder="Distrito..." /></div>
        <div class="informacion"><input bind:value={moneda} placeholder="Moneda..." /></div>
        <div class="informacion"><input bind:value={otrassenas} placeholder="Otras Señas..." /></div>
        <div class="informacion"><input bind:value={situacionenvio} placeholder="Situación del envío..." /></div>
        <div class="informacion"><input bind:value={codigoactividad} placeholder="Código de Actividad..." /></div>
        <div class="informacion"><input bind:value={tipoidreceptor} placeholder="Tipo de identificación del Receptor..." /></div>
    </div>

    <div class="boton-IVA-wrapper">
        <button class="boton-IVA" onclick={() => mostrarIVA = !mostrarIVA}>
            {mostrarIVA ? '− Ocultar I.V.A' : '+ Agregar I.V.A'}
        </button>
    </div>

    {#if mostrarIVA}
        <div class="panel-exoneracion">
            <p class="subtitulo-exoneracion">Calcular el I.V.A</p>
            <div class="inputs-exoneracion">
                <div class="informacion-ex">
                    <select bind:value={tipoIVA} class="select-ex">
                        <option value="" disabled selected>Tipo de I.V.A...</option>
                        {#each tiposIVA as tipo}
                            <option value={tipo.value}>{tipo.label}</option>
                        {/each}
                    </select>
                </div>
                <div class="informacion-ex">
                    <select bind:value={tarifaIVA} class="select-ex">
                        <option value="" disabled selected>Tarifa de I.V.A...</option>
                        {#each tarifasIVA as tarifa}
                            <option value={tarifa.value}>{tarifa.label}</option>
                        {/each}
                    </select>
                </div>
                <div class="informacion-ex"><textarea bind:value={numdoc}>B</textarea></div>
                <div class="informacion-ex"><input bind:value={fechaExoneracion} type="date" class="input-fecha" /></div>
                <div class="informacion-ex"><input bind:value={porcentajeExoneracion} type="number" min="0" max="100" placeholder="Porcentaje a exonerar (%)..." /></div>
            </div>
        </div>




        <div class="panel-exoneracion">
            <p class="subtitulo-exoneracion">Exonerar el I.V.A</p>
            <div class="inputs-exoneracion">
                <div class="informacion-ex">
                    <select bind:value={motivoExoneracion} class="select-ex">
                        <option value="" disabled selected>Motivo de exoneración...</option>
                        {#each motivosExoneracion as motivo}
                            <option value={motivo.value}>{motivo.label}</option>
                        {/each}
                    </select>
                </div>
                   
                {#if ['02', '03', '06', '07', '08'].includes(motivoExoneracion)}
                    <div class="informacion-ex">
                        <input bind:value={articulo} placeholder="Número de artículo..." type="number" />
                    </div>
                {/if}
                  
                {#if ['02', '03', '06', '07', '08'].includes(motivoExoneracion)}
                    <div class="informacion-ex">
                        <input bind:value={inciso} placeholder="Númerod de inciso..." type="number"/>
                    </div>
                {/if}    
                <div class="informacion-ex"><input bind:value={numDocExoneracion} placeholder="Número de documento (17 caracteres)..." maxlength="17" /></div>
                <div class="informacion-ex"><input bind:value={institucion} placeholder="Institución emisora..." /></div>
                <div class="informacion-ex"><input bind:value={fechaExoneracion} type="date" class="input-fecha" /></div>
                <div class="informacion-ex"><input bind:value={porcentajeExoneracion} type="number" min="0" max="100" placeholder="Porcentaje a exonerar (%)..." /></div>
            </div>
        </div>
    {/if}
</div>

<style>
    :global(body) {
        background-color: #b2e1f5;
        margin: 0;
    }

    .contenedor {
        background-color: #d6eef8;
        border: 2px solid #b0d8ec;
        border-radius: 20px;
        padding: 30px 40px;
        width: 640px;
        margin: 30px auto;
    }

    .header {
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
        margin-bottom: 25px;
    }

    .titulo {
        color: #ffffff;
        border: 2px solid #4A8EAC;
        border-radius: 10px;
        background-color: #4A8EAC;
        padding: 6px 40px;
        font-size: 20px;
        margin: 0;
        text-align: center;
    }

    .inputs1 {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
    }

    .informacion {
        background: #4AB265;
        border: 2px solid #4AB265;
        border-radius: 10px;
    }

    input {
        background: transparent;
        border: none;
        outline: none;
        color: white;
        font-size: 15px;
        padding: 8px 12px;
        width: 100%;
        box-sizing: border-box;
    }

    input::placeholder {
        color: rgba(255, 255, 255, 0.95);
    }

    /* Botón */
    .boton-IVA-wrapper {
        display: flex;
        justify-content: center;
        margin-top: 18px;
    }

    .boton-IVA {
        background-color: #4A8EAC;
        color: white;
        border: 2px solid #3a7a97;
        border-radius: 10px;
        padding: 8px 32px;
        font-size: 15px;
        cursor: pointer;
        transition: background-color 0.2s;
    }

    .boton-IVA:hover {
        background-color: #3a7a97;
    }

    .panel-exoneracion {
        margin-top: 16px;
        background-color: #c3e4f3;
        border: 2px solid #9acde8;
        border-radius: 14px;
        padding: 18px 20px;
    }

    .subtitulo-exoneracion {
        color: #4A8EAC;
        font-size: 16px;
        font-weight: bold;
        text-align: center;
        margin: 0 0 14px 0;
    }

    .inputs-exoneracion {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
    }

    .inputs-exoneracion .informacion-ex:last-child:nth-child(odd) {
        grid-column: 1 / -1;
    }

    .informacion-ex {
        background: #4A8EAC;
        border: 2px solid #4A8EAC;
        border-radius: 10px;
        display: flex;
        align-items: center;
    }

    .informacion-ex input,
    .informacion-ex select {
        background: transparent;
        border: none;
        outline: none;
        color: white;
        font-size: 14px;
        padding: 8px 12px;
        width: 100%;
        box-sizing: border-box;
    }

    .informacion-ex input::placeholder {
        color: rgba(255, 255, 255, 0.9);
    }

    .select-ex {
        appearance: none;
        cursor: pointer;
    }

    .select-ex option {
        background-color: #3a7a97;
        color: white;
    }

    .input-fecha::-webkit-calendar-picker-indicator {
        filter: invert(1);
        cursor: pointer;
    }
</style>