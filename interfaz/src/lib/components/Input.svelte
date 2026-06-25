<script>
    let { 
        titulo = "", 
        readonly = false, 
        value = $bindable("")
    } = $props();
</script>

<div class="grid-4">
    <div class="field">
        <div class="field__label">
            <span>{titulo}</span>
            <button class="link-btn">⊕ Agregar más cód.</button>
        </div>
        <div class="input-icon-wrap">
            <input class="inp" bind:value={value} placeholder="" readonly={readonly} />
            <button class="icon-btn icon-btn--green">🔍</button>
        </div>
    </div>
</div>

<style>
    .grid-4 {
        display: grid;
        grid-template-columns: 1fr 1fr 1.6fr 1fr;
        gap: 12px;
        align-items: end;
    }

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
</style>