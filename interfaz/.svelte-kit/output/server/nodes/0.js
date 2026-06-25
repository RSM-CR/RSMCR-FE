import * as universal from '../entries/pages/_layout.ts.js';

export const index = 0;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/_layout.svelte.js')).default;
export { universal };
export const universal_id = "src/routes/+layout.ts";
export const imports = ["_app/immutable/nodes/0.ST5ZHdGi.js","_app/immutable/chunks/BLeUhhAG.js","_app/immutable/chunks/xihTtKlq.js","_app/immutable/chunks/BXOAMTJO.js","_app/immutable/chunks/CHCuGAFo.js"];
export const stylesheets = [];
export const fonts = [];
