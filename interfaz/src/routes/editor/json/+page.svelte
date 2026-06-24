<script lang="ts">
    import { JSONEditor } from 'svelte-jsoneditor'
    import type { Factura } from '$lib/factura';
    import { getContext } from 'svelte';

    let factura: Factura = getContext('factura');
    let contenido = $state({
    text: undefined,
    json: factura
    })
</script>

<div class="editor-root">
    <JSONEditor bind:content={contenido}/>
</div>

<style>
    .editor-root
    {
        margin: 20px;
        flex: 1 1 0;
    }
</style>