<script lang="ts">
    import { JSONEditor } from 'svelte-jsoneditor';
    import type { Factura } from '$lib/factura';
    import { getContext } from 'svelte';

    let factura: Factura = getContext('factura');
    // Si estás en en la pestaña de text, por alguna razón devuelve text

    let contenido = $state({
    text: undefined,
    json: factura
    });

    function AlEditarJSON(nuevoContenido, contenidoPrevio, { erroresContenido, patchResult }) 
    {
        console.log(nuevoContenido);
        let objeto = nuevoContenido.json ?? JSON.parse(nuevoContenido.text);
        Object.assign(factura, objeto); // Sería bueno hacer esto de otra forma que no permita valores inválidos
        console.log($state.snapshot(factura));
    }
</script>

<div class="editor-root">
    <JSONEditor {contenido} onChange={AlEditarJSON}/>
</div>

<style>
    .editor-root
    {
        margin: 20px;
        flex: 1 1 0;
    }
</style>