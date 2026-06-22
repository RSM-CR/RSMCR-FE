<script>
    let metododepago = ('');
    let tipodoc = ('');
    let condicionventa = ('');
    let terminal = ('');
    let sucursal = ('');
    let moneda = ('');
    let situacionenvio = ('');
    let codigoactividad = ('');
    let tipoidreceptor = ('');
    let numcuentaemisor = ('');
    let unidadmedida = ('');
    let provincia = ('');
    let canton = ('');
    let distrito = ('');
    let otrassenas = ('');
    let numdoc = ('');
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
</style>