# Plantilla: venta de formación

Correo promocional para vender formaciones de Westlabs AI School (convocatorias abiertas, cursos concretos, formación para empresas). Sigue el estilo de la web de la escuela: www.westlabs.es/escola.

## Ediciones

Todas las ediciones tienen **la misma estructura y los mismos bloques**. Solo cambian los colores, las imágenes y los textos de ejemplo.

| Edición | Carpeta | Cuándo usarla | Fondo oscuro | Acento sobre blanco | Acento sobre oscuro | Panel de fechas | Banda FUNDAE |
|---|---|---|---|---|---|---|---|
| Base | `base/` | Todo el año | Noche `#07080C` / `#111A33` | Azul `#2563EB` | Celeste `#5BC8F5` | Azul `#1B3F94` → `#2563EB` | Azul → celeste |
| Navidad | `navidad/` | Diciembre y campaña de enero | Pino oscuro `#06150E` / `#0B2217` | Granate `#7A1F2B` | Dorado `#F2C14E` | Verde pino muy oscuro `#0F2A1C` → `#163824`, fechas en granate | Granate `#4A0F18` → `#9E3442` |

En la edición de Navidad no se usan verdes claros: todo el verde es pino oscuro y los tintes de las tarjetas son crema y rosa granate.

Cada edición tiene su carpeta con `plantilla.html` y `img/`. Lo común a todas (logos de AI School y de FUNDAE, iconos 3D de la edición base) está en `assets/comun/`.

### Crear una edición nueva

1. Copiar la carpeta `base/` con el nombre de la edición (por ejemplo, `verano/`).
2. Cambiar los colores con una tabla de equivalencias, color por color, como la de arriba. La estructura no se toca.
3. Hacer **imágenes propias de la edición**: la cabecera (galaxia con el logo, recoloreada con la paleta de la edición), las fotos de muestra y los iconos si no encajan con los colores. Nunca reutilizar las imágenes de otra edición.
4. Adaptar los textos de ejemplo (etiqueta del hero, titular, preheader).
5. Añadir la edición a la tabla de arriba.

## Bloques (en orden)

| # | Bloque | Qué lleva | ¿Se puede quitar? |
|---|---|---|---|
| 1 | Cabecera | Imagen con la galaxia y el logo de AI School (`img/cabecera.jpg`, 1200 x 300) | No |
| 2 | Hero oscuro | Etiqueta en mayúsculas con rayas, titular a dos tonos, texto corto, tres sellos con check y dos botones (principal blanco y secundario con borde) | No |
| 3 | Imagen principal | Foto a caballo entre el fondo oscuro y el blanco (1040 x 600) | No |
| 4 | Convocatorias | Etiqueta, título a dos tonos, texto y panel con las filas de curso (nombre, sesiones, fecha) y un botón | Sí, si el correo no vende convocatorias con fecha |
| 5 | Tarjetas de curso | Dos tarjetas en tintes claros con icono 3D, categoría, nombre, tres puntos y etiquetas de modalidad | No |
| 6 | Banda FUNDAE | Logo de FUNDAE, título, texto y botón | Sí, si la formación no es bonificable |
| 7 | Formación para empresas | Bloque oscuro con foto (1040 x 480), etiqueta, título a dos tonos, texto y botón | Sí (OPCIONAL) |
| 8 | Firma | Línea de dudas, saludo y firma | No |
| 9 | Pie | Logo, dirección, enlaces, sellos, datos legales y baja (BAJA) | No |

## Reglas de diseño

- Títulos a dos tonos: la segunda parte en el acento de la edición (sobre blanco, el acento claro; sobre oscuro, el acento luminoso).
- Etiquetas en mayúsculas, pequeñas, con espaciado y una raya delante (y detrás si están centradas).
- Botones en píldora con flecha (→). Sobre fondo oscuro o de color: blancos con la letra del color de la edición. Botón secundario: borde fino y letra blanca.
- Tarjetas con esquinas redondeadas (16-18 px) y borde fino.
- Ancho de 600 px; en el móvil las columnas se apilan y las filas de curso ponen la fecha debajo.
- Títulos en AllRoundGothic con Poppins y Arial como alternativa. Gmail no carga fuentes propias: en Gmail se ven en Arial.
- Sin emojis en el texto, salvo los de la edición: la de Navidad lleva dos, discretos (árbol en la etiqueta del hero y regalo en el título de FUNDAE). No añadir más.

## Imágenes: siempre nuevas

En cada correo se piden a Alba las imágenes antes de maquetar:

- **Imagen principal:** 1040 x 600 px.
- **Imagen del bloque de empresas:** 1040 x 480 px (si se usa el bloque 7).
- Una descripción corta de cada una para el texto alternativo.

Las fotos que hay ahora en `img/` son de muestra (de la web, con retoque en la edición de Navidad). No se envía nunca un correo con las fotos de muestra ni con las de otro correo. Cada correo guarda sus imágenes junto a él, en `correos/`.

## Textos

- Lo que va entre [corchetes] es un ejemplo o un dato pendiente. Antes de enviar no puede quedar ningún corchete.
- Tono: directo, corto, en plural de Westlabs, sin fórmulas de venta.
