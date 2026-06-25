import { S as writable } from "./server.js";
import "./index-server2.js";
//#region src/lib/stores/websockets.store.ts
var websocketMessagesStore = writable([]);
var websocketMessages = websocketMessagesStore;
function addMessage(message) {
	websocketMessagesStore.update((items) => [...items, message]);
}
//#endregion
export { websocketMessages as n, addMessage as t };
