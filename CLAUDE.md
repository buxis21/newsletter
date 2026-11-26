# Correos de Westlabs AI School

Repositorio para preparar los correos HTML (anuncios y newsletter periódica) que Westlabs AI School envía a sus clientes y leads. El objetivo principal es vender formaciones.

## Marca y tono

- Remitente: Westlabs AI School. Firma Alba Ripoll salvo que se diga otra cosa.
- Idioma: castellano por defecto; catalán para los clientes que lo usan (sobre todo los de Lleida dados de alta a mano en el CRM).
- Identidad: la de la web de la escuela (www.westlabs.es/escola). Secciones oscuras alternadas con secciones blancas, títulos a dos tonos, etiquetas en mayúsculas con raya, tarjetas en tintes claros y botones en píldora con flecha. Títulos en AllRoundGothic con Poppins y Arial como alternativa; texto en Poppins. Los colores dependen de la edición de la plantilla (ver su README).
- Tono: directo, corto, en plural de Westlabs, sin fórmulas de venta. Sin emojis en los textos que se envían.

## Estructura del repositorio

- `plantillas/`: una carpeta por plantilla. Cada plantilla tiene un `README.md` con sus bloques, reglas y ediciones, y una carpeta por edición (`plantilla.html` + `img/`).
  - `plantillas/venta-formacion/`: correo para vender formaciones. Ediciones: `base` (colores de la web, todo el año) y `navidad` (pino, rojo y dorado).
  - Habrá más plantillas (por ejemplo, newsletter periódica). Cada una nueva va en su carpeta con su README.
- `assets/comun/`: lo que comparten todas las plantillas: logos de AI School (blanco y azul), logo de FUNDAE e iconos 3D de la web.
- `correos/`: un correo por carpeta, `correos/AAAA-MM-DD-tema-idioma/` con `correo.html` e `img/` con sus imágenes. Se crea copiando la edición de la plantilla que toque.
- `herramientas/preparar_borrador.py`: prepara un correo para el borrador de Gmail (ver abajo).

## Cómo se hace un correo nuevo

1. Preguntar qué plantilla y qué edición, a qué lista va y en qué idioma.
2. Pedir las imágenes (ver abajo) y el contenido: curso, fechas, precio o bonificación, enlaces.
3. Copiar la edición a `correos/AAAA-MM-DD-tema-idioma/`, rellenar los textos y quitar los bloques que no hagan falta.
4. Revisar en ordenador y móvil, y que no quede ningún [corchete].
5. Crear el borrador en Gmail para que Alba lo vea en real.

## Imágenes: siempre nuevas

- En cada correo nuevo, antes de maquetar, pedir a Alba las imágenes: la principal (1040 x 600 px) y la del bloque de empresas (1040 x 480 px), con una descripción corta para el texto alternativo. Si no hay imagen para un hueco, preguntar si se quita el bloque.
- Nunca enviar con las imágenes de muestra de la plantilla ni reutilizar las de otro correo o de otra edición.
- Cada edición de plantilla tiene sus propias imágenes (cabecera recoloreada, fotos y, si hace falta, iconos) adaptadas a sus colores.

## Envío con Gmail

- La vista previa real se hace creando un borrador en Gmail con el conector (`create_draft` con `htmlBody`). Gmail elimina las imágenes externas del borrador, así que las imágenes van adjuntas como inline y en el HTML los `src` pasan a `cid:att0`, `cid:att1`… en el orden de los adjuntos. `python3 herramientas/preparar_borrador.py <correo.html>` hace el cambio, lista los adjuntos con su sha256 y avisa de los corchetes pendientes.
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
