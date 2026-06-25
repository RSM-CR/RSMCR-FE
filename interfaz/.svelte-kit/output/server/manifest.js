export const manifest = (() => {
function __memo(fn) {
	let value;
	return () => value ??= (value = fn());
}

return {
	appDir: "_app",
	appPath: "app/_app",
	assets: new Set(["robots.txt"]),
	mimeTypes: {".txt":"text/plain"},
	_: {
		client: {start:"_app/immutable/entry/start.wwIYWFwu.js",app:"_app/immutable/entry/app.yJfy-wQs.js",imports:["_app/immutable/entry/start.wwIYWFwu.js","_app/immutable/chunks/BEW6gpiD.js","_app/immutable/chunks/BLeUhhAG.js","_app/immutable/chunks/CHCuGAFo.js","_app/immutable/entry/app.yJfy-wQs.js","_app/immutable/chunks/BLeUhhAG.js","_app/immutable/chunks/kNaey6uv.js","_app/immutable/chunks/xihTtKlq.js"],stylesheets:[],fonts:[],uses_env_dynamic_public:false},
		nodes: [
			__memo(() => import('./nodes/0.js')),
			__memo(() => import('./nodes/1.js'))
		],
		remotes: {
			
		},
		routes: [
			
		],
		prerendered_routes: new Set(["/app/","/app/RFiles/","/app/editor/","/app/editor/xml/","/app/tenants/"]),
		matchers: async () => {
			
			return {  };
		},
		server_assets: {}
	}
}
})();
