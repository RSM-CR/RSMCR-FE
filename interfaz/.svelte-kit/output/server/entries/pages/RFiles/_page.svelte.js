import { n as ensure_array_like, v as attr, y as escape_html } from "../../../chunks/server.js";
//#region src/routes/RFiles/+page.svelte
function _page($$renderer) {
	const items = [
		"XML 1",
		"XML 2",
		"XML 3",
		"XML 4",
		"XML 5",
		"XML 6",
		"XML 7",
		"XML 8",
		"XML 9",
		"XML 10"
	];
	let showItems = true;
	let i = 5;
	$$renderer.push(`<div class="shell svelte-df384e"><header class="svelte-df384e"><h1 class="svelte-df384e">Panel de documentos recientes</h1></header> <div class="divider svelte-df384e"></div> <main class="svelte-df384e"><div class="controls svelte-df384e"><label class="toggle-label svelte-df384e"><span class="toggle svelte-df384e"><input type="checkbox"${attr("checked", showItems, true)} class="svelte-df384e"/> <span class="slider-t svelte-df384e"></span></span> Mostrar documentos</label> <div class="range-wrap svelte-df384e"><span>Número de elementos a mostrar</span> <input type="range"${attr("value", i)} min="1" max="10" step="1" class="svelte-df384e"/></div></div> <div class="doc-list svelte-df384e">`);
	{
		$$renderer.push("<!--[0-->");
		$$renderer.push(`<!--[-->`);
		const each_array = ensure_array_like(items.slice(0, i));
		for (let $$index = 0, $$length = each_array.length; $$index < $$length; $$index++) {
			let doc = each_array[$$index];
			$$renderer.push(`<div class="doc-row svelte-df384e">${escape_html(doc)}</div>`);
		}
		$$renderer.push(`<!--]-->`);
	}
	$$renderer.push(`<!--]--></div></main></div>`);
}
//#endregion
export { _page as default };
