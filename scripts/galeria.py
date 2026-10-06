"""Arma salida/GALERIA.html: cada gráfico tuyo al lado del ejemplo de Imperio que lo inspiró.

Uso:  python3 scripts/galeria.py      (en Windows: py scripts\\galeria.py)
No necesita instalar nada.
"""
import html
import json
import os
import re
import webbrowser
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "salida"
FORMATOS = RAIZ / "formatos"
EXT = {".png", ".jpg", ".jpeg", ".webp"}


def carpeta_de(nombre):
    """salida/20261007/007-native_4x5.png -> 007-native"""
    m = re.match(r"^(\d{3}-[a-z0-9-]+?)(?:_(?:4x5|9x16|1x1)(?:_v\d+)?)?$", Path(nombre).stem)
    return m.group(1) if m else None


def main():
    datos = {}
    catalogo = RAIZ / "data" / "formatos.json"
    if catalogo.exists():
        for f in json.loads(catalogo.read_text(encoding="utf-8")):
            datos[f["carpeta"]] = f
    imagenes = sorted(p for p in SALIDA.rglob("*") if p.suffix.lower() in EXT)
    if not imagenes:
        print("Todavía no hay gráficos en salida/.")
        return
    filas = []
    for img in imagenes:
        carpeta = carpeta_de(img.name)
        info = datos.get(carpeta, {})
        ejemplo = FORMATOS / carpeta / "ejemplo.jpg" if carpeta else None
        rel_img = os.path.relpath(img, SALIDA).replace(os.sep, "/")
        rel_ej = os.path.relpath(ejemplo, SALIDA).replace(os.sep, "/") if ejemplo and ejemplo.exists() else ""
        titulo = html.escape(info.get("nombre", img.stem))
        familia = html.escape(info.get("familia", ""))
        filas.append(f"""
<div class="par">
  <div class="cab"><b>{titulo}</b><span>{familia}</span><code>{html.escape(rel_img)}</code></div>
  <div class="imgs">
    <figure><img src="{html.escape(rel_img)}"><figcaption>Tu versión</figcaption></figure>
    {f'<figure class="ej"><img src="{html.escape(rel_ej)}"><figcaption>Ejemplo de Imperio</figcaption></figure>' if rel_ej else ''}
  </div>
</div>""")
    pagina = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Galería · Fábrica de Gráficos</title>
<style>
body{{margin:0;background:#0B0B0A;color:#EDE6D3;font-family:Inter,Helvetica,Arial,sans-serif}}
h1{{font-weight:800;letter-spacing:.5px;padding:24px 28px 4px;margin:0;color:#E9C876}}
p.s{{padding:0 28px 18px;margin:0;color:#A79F8A}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(460px,1fr));gap:18px;padding:0 28px 40px}}
.par{{background:#15140F;border:1px solid #2A271F;border-radius:12px;padding:14px}}
.cab{{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;margin-bottom:10px}}
.cab span{{color:#CDBF98;font-size:12px}} .cab code{{color:#8E8672;font-size:11px;margin-left:auto}}
.imgs{{display:grid;grid-template-columns:2fr 1fr;gap:10px;align-items:start}}
figure{{margin:0}} img{{width:100%;border-radius:8px;display:block}}
figcaption{{font-size:11px;color:#A79F8A;margin-top:4px}} .ej img{{opacity:.85}}
</style></head><body>
<h1>Tus gráficos</h1><p class="s">{len(imagenes)} gráficos en salida/. A la izquierda el tuyo, a la derecha el formato de Imperio que lo inspiró.</p>
<div class="grid">{''.join(filas)}</div></body></html>"""
    destino = SALIDA / "GALERIA.html"
    destino.write_text(pagina, encoding="utf-8")
    print(f"Listo: {destino} ({len(imagenes)} gráficos)")
    try:
        webbrowser.open(destino.as_uri())
    except Exception:
        pass


if __name__ == "__main__":
    main()
