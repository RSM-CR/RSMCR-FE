import "../../../chunks/index-server.js";
import "../../../chunks/server.js";
//#region src/routes/tenants/+page.svelte
function _page($$renderer, $$props) {
	$$renderer.component(($$renderer) => {
		let tenantSelector;
		let selectorValue = "";
		$$renderer.push(`<div class="root svelte-vgi3i"><div class="card svelte-vgi3i"><div class="content svelte-vgi3i"><h1 class="svelte-vgi3i">Selector de Tenant</h1> <p class="desc svelte-vgi3i">Por favor, selecciona un tenant:</p> `);
		$$renderer.select({
			id: "tenantSelector",
			value: selectorValue,
			this: tenantSelector,
			class: ""
		}, ($$renderer) => {
			$$renderer.option({
				value: "",
				class: ""
			}, ($$renderer) => {
				$$renderer.push(`Selecciona un tenant`);
			}, "svelte-vgi3i");
		}, "svelte-vgi3i");
		$$renderer.push(` <button class="svelte-vgi3i">Seleccionar Tenant</button></div></div></div>`);
	});
}
//#endregion
export { _page as default };
