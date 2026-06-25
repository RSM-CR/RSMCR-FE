import re
from pathlib import Path

SVELTE_DIRS = [Path("routes/editor/+page.svelte")]
OUTPUT_DIR = Path("docs/build/index.html")

def extraer_comentarios(svelte_path: Path) -> str:
    texto = svelte_path.read_text(encoding="utf-8")
    comentarios = re.findall(r'<!--(.*?)-->', texto, re.DOTALL)
    if not comentarios:
        return ""
    
    nombre = f"{svelte_path.parent.name}_{svelte_path.stem}"
    
    lineas = [f"# `{nombre}.svelte`\n"]
    for bloque in comentarios:
        lineas.append(bloque.strip())
        lineas.append("")
    return "\n".join(lineas)

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    for directorio in SVELTE_DIRS:
        for svelte in directorio.rglob("*.svelte"):
            contenido = extraer_comentarios(svelte)
            if contenido:
                # mismo cambio aquí
                nombre = f"{svelte.parent.name}_{svelte.stem}"
                salida = OUTPUT_DIR / (nombre + ".md")
                salida.write_text(contenido, encoding="utf-8")
                print(f"  ✓ {svelte.name} → {salida}")

if __name__ == "__main__":
    main()
