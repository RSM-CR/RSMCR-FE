import { a as unsubscribe_stores, i as store_get, n as ensure_array_like, y as escape_html } from "../../chunks/server.js";
import { n as websocketMessages } from "../../chunks/websockets.store.js";
//#region src/routes/+page.svelte
function _page($$renderer) {
	var $$store_subs;
	$$renderer.push(`<h1>Welcome to SvelteKit</h1> <p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p> <p>Mira <a href="./RFiles">mi pagina</a></p> <!--[-->`);
	const each_array = ensure_array_like(store_get($$store_subs ??= {}, "$websocketMessages", websocketMessages));
	for (let $$index = 0, $$length = each_array.length; $$index < $$length; $$index++) {
		let message = each_array[$$index];
		$$renderer.push(`<p>${escape_html(message.type)}</p> <pre>${escape_html(JSON.stringify(message.payload, null, 2))}</pre>`);
	}
	$$renderer.push(`<!--]-->`);
	if ($$store_subs) unsubscribe_stores($$store_subs);
}
//#endregion
export { _page as default };
