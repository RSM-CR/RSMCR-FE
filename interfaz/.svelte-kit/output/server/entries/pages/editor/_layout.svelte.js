import { n as ensure_array_like, v as attr, y as escape_html } from "../../../chunks/server.js";
import { t as resolve } from "../../../chunks/paths.js";
//#region src/lib/tab.ts
var Tab = class {
	nombre;
	ruta;
	constructor(nombre, ruta) {
		this.nombre = nombre;
		this.ruta = ruta;
	}
};
//#endregion
//#region src/lib/components/NavBar.svelte
function NavBar($$renderer, $$props) {
	let { tabs = [] } = $$props;
	$$renderer.push(`<nav><ul class="svelte-q971rm"><!--[-->`);
	const each_array = ensure_array_like(tabs);
	for (let $$index = 0, $$length = each_array.length; $$index < $$length; $$index++) {
		let tab = each_array[$$index];
		$$renderer.push(`<li><a${attr("href", tab.ruta)}>${escape_html(tab.nombre)}</a></li>`);
	}
	$$renderer.push(`<!--]--></ul></nav>`);
}
//#endregion
//#region src/routes/editor/+layout.svelte
function _layout($$renderer, $$props) {
	$$renderer.component(($$renderer) => {
		const urlActual = resolve("/editor");
		const tabs = [new Tab("Editor Automático", urlActual), new Tab("Editor XML", `${urlActual}/xml`)];
		let { children } = $$props;
		NavBar($$renderer, { tabs });
		$$renderer.push(`<!----> `);
		children($$renderer);
		$$renderer.push(`<!---->`);
	});
}
//#endregion
export { _layout as default };
