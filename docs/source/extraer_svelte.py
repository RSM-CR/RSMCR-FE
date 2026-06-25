import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

SVELTE_DIRS = [Path(r"C:\Users\AlexaVillalobosAraya\Desktop\RSM\RSMCR-FE\interfaz\src\routes\editor\+page.svelte")]
OUTPUT_DIR = Path(r"C:\Users\AlexaVillalobosAraya\Desktop\RSM\RSMCR-FE\docs\source\svelte_docs")

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
    for svelte_path in SVELTE_DIRS:
        if svelte_path.is_file():
            contenido = extraer_comentarios(svelte_path)
            print(f"Contenido extraído:\n{repr(contenido[:300])}")
            if contenido:
                nombre = f"{svelte_path.parent.name}_{svelte_path.stem}"
                salida = OUTPUT_DIR / (nombre + ".md")
                salida.write_text(contenido, encoding="utf-8")
                print(f"  ✓ {svelte_path.name} → {salida}")
        else:
            print(f"  ✗ No encontrado: {svelte_path}")

if __name__ == "__main__":
    main()
