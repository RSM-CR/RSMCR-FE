<script lang="ts">
    import NavBar from "$lib/components/NavBar.svelte";
    import { Tab } from "$lib/tab";
    import { resolve } from "$app/paths";
    import { setContext } from "svelte";
    import { NuevaFactura } from "$lib/factura";
    import type { LayoutProps } from './$types';
    import type { Factura } from "$lib/factura";

    const urlActual = resolve("/editor");

    const tabs = [new Tab("Editor Automático", urlActual), new Tab("Editor JSON", `${urlActual}/json`)]

    let { data, children }: LayoutProps = $props();

    const factura = $state(NuevaFactura())

    setContext('factura', factura);

    async function enviarDatos()
    {
        const respuesta = await fetch("http://localhost:8000/enviar-json", {
            method: "POST",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify(factura)
        })
    }

</script>

<NavBar tabs={tabs}/>

{@render children()}

<button style="background-color: #4caf50;" onclick={enviarDatos}><p>Enviar factura</p></button>