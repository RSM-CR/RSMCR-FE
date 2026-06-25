

export const index = 7;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/tenants/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/7.Cwk8AFoq.js","_app/immutable/chunks/BLeUhhAG.js","_app/immutable/chunks/xihTtKlq.js"];
export const stylesheets = ["_app/immutable/assets/7.DQEffCF8.css"];
export const fonts = [];
