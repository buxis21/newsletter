# Correos de Westlabs AI School

Repositorio para preparar los correos HTML (anuncios y newsletter periódica) que Westlabs AI School envía a sus clientes y leads. El objetivo principal es vender formaciones.

## Marca y tono

- Remitente: Westlabs AI School. Firma Alba Ripoll salvo que se diga otra cosa.
- Idioma: castellano por defecto; catalán para los clientes que lo usan (sobre todo los de Lleida dados de alta a mano en el CRM).
- Identidad: azul corporativo `#1E355F`, acentos `#2651A8` (sobre blanco) y `#6BC3E1` (solo sobre fondo oscuro), texto `#14223D` / `#5B6472`, tarjetas `#F1F4F9` con borde `#D6DDE8`. Tipografía Poppins con Arial como alternativa. El logo completo aparece una sola vez (en el pie).
- Tono: directo, corto, en plural de Westlabs, sin fórmulas de venta. Sin emojis en los textos que se envían.

## Estructura

- `plantillas/plantilla-base.html`: plantilla base. Maquetada con tablas y estilos en línea para que funcione en Gmail, Outlook y Apple Mail. Lo que va entre [corchetes] es contenido de ejemplo o un dato pendiente. Los bloques marcados como OPCIONAL se pueden quitar.
- `assets/img/`: icono blanco (cabecera) y logo azul (pie), ya a tamaño de correo.
- Cada correo nuevo se crea copiando la plantilla a `correos/AAAA-MM-DD-tema-idioma.html`.

## Envío con Gmail

- La vista previa real se hace creando un borrador en Gmail con el conector (`create_draft` con `htmlBody`). Gmail elimina las imágenes externas del borrador: las imágenes se adjuntan como inline y en el HTML se cambian los `src` por `cid:att0`, `cid:att1`… según su posición en los adjuntos.
- Nunca enviar sin la confirmación explícita de Alba.

### Límites de Gmail (tenerlos siempre en cuenta)

- Unos 500 destinatarios al día con una cuenta de Gmail normal y unos 2.000 con Google Workspace. Si una lista los supera, repartir el envío en varios días.
- Cada correo comercial tiene que llevar una forma de darse de baja. La plantilla pide responder con la palabra BAJA. Con Google Workspace, el modo "envío múltiple" de Gmail añade el enlace de baja automáticamente y personaliza el nombre de cada destinatario.
- No poner a todos los destinatarios en "Para" ni en "CC": usar envío múltiple o CCO.

## Listas de difusión (a partir del CRM de Westlabs)

Campos que se han propuesto añadir en la ficha del cliente: lista de difusión (sí / no / baja), base legal (cliente actual / consentimiento del formulario / sin consentimiento) e idioma (castellano / catalán). Mientras no existan en la app, se llevan aparte.

| Lista | Quién entra | Qué recibe |
|---|---|---|
| Clientes | Propuesta aceptada, proyecto en marcha o entregado | Newsletter y anuncios de formaciones (venta cruzada) |
| En negociación | Contactados o con propuesta enviada, interesados | Solo la newsletter, para no interferir en el seguimiento comercial |
| Reactivación | Leads fríos | Anuncios de formación para retomar el contacto |

No entran nunca: descartados, quien haya pedido la baja, quien no tenga base legal (art. 21 LSSI), quien no tenga correo, The Bridge School (subcontratación) ni contactos particulares sin empresa.

## Después de cada envío

Revisar en Gmail las respuestas: bajas (marcarlas en el CRM y no volver a enviarles), interesados (proponer seguimiento en el CRM al responsable) y rebotes (corregir o quitar el correo). Proponer los cambios en el CRM y esperar confirmación antes de hacerlos.
