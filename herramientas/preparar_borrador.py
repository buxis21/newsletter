"""Prepara un correo para crear el borrador en Gmail con el conector.

Uso:  python3 herramientas/preparar_borrador.py correos/2026-12-10-claude-navidad-es/correo.html

Gmail elimina las imágenes externas de un borrador, así que las imágenes van
adjuntas como inline. Este script:
  - cambia cada src de imagen local por cid:att0, cid:att1... en orden de aparición
    (si una misma imagen sale dos veces, usa el mismo cid);
  - quita los comentarios HTML;
  - avisa si quedan [corchetes] o enlaces sin completar;
  - escribe <correo>.gmail.html y <correo>.adjuntos.json con la ruta absoluta,
    el sha256 y el tipo de cada adjunto, listos para create_draft.
"""
import hashlib
import json
import mimetypes
import os
import re
import sys


def main(ruta):
    ruta = os.path.abspath(ruta)
    base = os.path.dirname(ruta)
    html = open(ruta, encoding="utf-8").read()
    html = re.sub(r"<!--.*?-->", "", html, flags=re.S)

    adjuntos, indices = [], {}

    def cambiar(m):
        src = m.group(1)
        if src.startswith(("http:", "https:", "cid:", "data:")):
            return m.group(0)
        fichero = os.path.normpath(os.path.join(base, src))
        if fichero not in indices:
            datos = open(fichero, "rb").read()
            indices[fichero] = len(adjuntos)
            adjuntos.append({
                "ruta": fichero,
                "nombre": os.path.basename(fichero),
                "sha256": hashlib.sha256(datos).hexdigest(),
                "mimeType": mimetypes.guess_type(fichero)[0] or "application/octet-stream",
            })
        return f'src="cid:att{indices[fichero]}"'

    html = re.sub(r'src="([^"]+)"', cambiar, html)
    html = "\n".join(l.strip() for l in html.splitlines() if l.strip())

    pendientes = sorted(set(re.findall(r"\[[^\]\n]{1,80}\]", html)))
    salida = os.path.splitext(ruta)[0]
    open(salida + ".gmail.html", "w", encoding="utf-8").write(html)
    json.dump(adjuntos, open(salida + ".adjuntos.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    print(f"HTML para Gmail: {salida}.gmail.html ({len(html)} caracteres)")
    for i, a in enumerate(adjuntos):
        print(f"  cid:att{i}  {a['nombre']}  sha256:{a['sha256']}")
    if pendientes:
        print(f"\nATENCIÓN: quedan {len(pendientes)} textos entre corchetes:")
        for p in pendientes:
            print("  " + p)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
