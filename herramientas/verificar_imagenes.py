"""Comprueba que cada imagen de un borrador o correo de Gmail apunta al archivo correcto.

Uso: python3 herramientas/verificar_imagenes.py <json de get_draft o get_message en formato RAW>
Imprime, para cada <img>, su texto alternativo y el archivo adjunto al que apunta.
Si una imagen no coincide con su alt (por ejemplo, la cabecera apunta a una medalla), no enviar.
"""
import json,sys,base64,email,re,hashlib
d=json.load(open(sys.argv[1])); raw=d['raw']
m=email.message_from_bytes(base64.urlsafe_b64decode(raw+'='*(-len(raw)%4)))
cid2file={}
for p in m.walk():
    if p.get('Content-ID'):
        cid2file[p.get('Content-ID').strip('<>')]=(p.get_filename(),hashlib.sha256(p.get_payload(decode=True)).hexdigest()[:8])
for p in m.walk():
    if p.get_content_type()=='text/html':
        h=p.get_payload(decode=True).decode('utf-8','replace')
        for src,alt in re.findall(r'<img[^>]*src="cid:([^"]+)"[^>]*alt="([^"]*)"',h): print(f'{alt:45} -> {cid2file.get(src)}')
