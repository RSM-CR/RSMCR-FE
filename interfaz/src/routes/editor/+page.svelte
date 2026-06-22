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
    import NavBar from "$lib/components/NavBar.svelte";
</script>

<p class="titulo">Editor de XML</p>

<NavBar />

<div class="inputs1">
    <div class="pago">
        <input bind:value={metododepago} placeholder="Método de pago:" />
    </div>
    <div class="doc">
        <input bind:value={tipodoc} placeholder="Tipo de documento:" />
    </div>
    <div class="numdoc">
        <input bind:value={numdoc} placeholder="Número de documento:" />
    </div>
    <div class="venta">
        <input bind:value={condicionventa} placeholder="Condición de venta:" />
    </div>
    <div class="terminal">
        <input bind:value={terminal} placeholder="Terminal:" />
    </div>
    <div class="sucursal">
        <input bind:value={sucursal} placeholder="Sucursal:" />
    </div>
    <div class="moneda">
        <input bind:value={moneda} placeholder="Moneda utilizar:" />
    </div>
    <div class="envio">
        <input bind:value={situacionenvio} placeholder="Situación de envío:" />
    </div>
    <div class="actividad">
        <input bind:value={codigoactividad} placeholder="Código de actividad:" />
    </div>
    <div class="idreceptor">
        <input bind:value={tipoidreceptor} placeholder="Tipo identificación receptor:" />
    </div> 
    <div class="numemisor">
        <input bind:value={numcuentaemisor} placeholder="Número de cuenta emisor:" />
    </div>
    <div class="unidad">
        <input bind:value={unidadmedida} placeholder="Unidad de medida:" />
    </div>
    <div class="provin">
        <input bind:value={provincia} placeholder="Provincia:" />
    </div>
    <div class="canto">
        <input bind:value={canton} placeholder="Cantón:" />
    </div>
    <div class="district">
        <input bind:value={distrito} placeholder="Distrito:" />
    </div>
    <div class="senas">
        <input bind:value={otrassenas} placeholder="Otras señas:" />
    </div>
</div> 


<style>
    .titulo {
        color: #ffffff;
        border: 2px solid #4A8EAC;
        border-radius: 10px;
        background-color: #4A8EAC;
        width: 300px;
        text-align: center;
        margin: 0 auto;
        font-size: 20px;
    }

    .inputs1 {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 350px;
        margin: 0 auto;
        margin-top: 25px;
        font-size: 18px;
        color: #ffffff
        background-color: #DFE9FF

    }

    .pago {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    .doc {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px; 
        margin-bottom: 10px; 
    }

    .venta {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    .numdoc {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    .terminal {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    .sucursal {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    .moneda {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px;
        margin-bottom: 10px;  
    }

    .envio {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px;
        margin-bottom: 10px;  
    }

    .actividad {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px;
        margin-bottom: 10px;  
    }

    .idreceptor {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px;
        margin-bottom: 10px;  
    }

    .numemisor {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px;
        margin-bottom: 10px;  
    }

    .unidad {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px;
        margin-bottom: 10px;  
    }

    .provin {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px;
        margin-bottom: 10px;  
    }

    .canto {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px;
        margin-bottom: 10px;  
    }

    .district {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px;
        margin-bottom: 10px;  
    }

    .senas {
        background: #4AB265;
        border: 2px solid #4AB265;;
        border-radius: 10px;
        margin-bottom: 10px;  
    }


    :global(body) {
        background-color: #b2e1f5;
    }
</style>