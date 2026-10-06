# CLAUDE.md · Fábrica de Gráficos

Este archivo es para ti, Claude. Explica qué hace este kit, cómo lo operas y las reglas que no se rompen.
Es un recurso de Imperio Agéntico para el curso "Claude para Meta Ads" de Benja (@bencord).

## A quién estás ayudando

A una persona que NO es técnica.

- Haz todo tú. Nunca le pidas que escriba un comando ni que edite un archivo a mano.
- Habla en español simple y en tú. Antes de cada paso, dile en una frase qué vas a hacer.
- Mantén una lista de tareas visible y ve marcando lo que terminas.
- Pregunta UNA cosa a la vez.
- Antes de gastar créditos, dile cuánto va a costar y espera su OK.

## Qué hace el kit

`formatos/` tiene la biblioteca de anuncios estáticos que Imperio Agéntico diseñó para Meta: 212 formatos, de los que 71 ya corrieron con plata real (ver `formatos/RANKING-META.md`). Cada formato trae:
- `ejemplo.jpg`: el anuncio de Imperio.
- `ficha.md`: qué es, por qué funciona, cuándo usarlo, el texto que llevó, una receta con espacios para la marca y el prompt con que se hizo (GPT Image 2.5).

Tu trabajo: entender la marca de la persona y **recrear cada formato para SU negocio** con Higgsfield (modelo GPT Image 2.5), revisar cada imagen y dejarla lista en `salida/`.

Archivos de apoyo:
- `data/formatos.json`: la lista de todos los formatos, ordenada por familia y por resultado real.
- `formatos/INDICE.md`: la misma lista para leer.
- `formatos/RANKING-META.md`: los formatos que corrieron en la cuenta de Imperio, con su costo por compra.
- `buenas-practicas.md`: las reglas para que un gráfico venda. Léelo antes de escribir el primer prompt.

## Paso 0 · Revisar Higgsfield

1. Revisa si tienes las herramientas de Higgsfield (por ejemplo `generate_image`, `media_import_url`, `media_upload`, `media_confirm`, `jobs_wait`, `balance`). Pueden venir con un prefijo largo y, en Claude Code, a veces están "diferidas": si no las ves, búscalas con la búsqueda de herramientas (ToolSearch) usando palabras como `higgsfield generate_image` y cárgalas antes de usarlas.
2. Si no están: explícale que hay que conectar Higgsfield a Claude. En la app de Claude: **Configuración → Conectores → busca "Higgsfield" → Conectar** e inicia sesión con su cuenta de Higgsfield (higgsfield.ai). Después hay que abrir un chat nuevo en esta misma carpeta. Si usa Claude Code en la terminal, el conector se agrega con `claude mcp add --transport http higgsfield https://mcp.higgsfield.ai/mcp`.
3. Con las herramientas listas, llama a `balance` y dile cuántos créditos tiene.

## Paso 1 · Conocer la marca (una pregunta a la vez)

Llena `marca/marca.md` copiando `marca/marca.plantilla.md`. Lo mínimo:
1. Nombre del negocio y qué vende, en una frase.
2. Precio y oferta de HOY (solo lo que existe: no inventes descuentos, garantías ni "gratis").
3. Su cliente y el problema que le resuelve.
4. Pruebas reales que puede mostrar: cifras, clientes con permiso, premios, prensa. Si no hay, se anota "no hay".
5. Colores de marca (si no los sabe, sácalos del logo) y estilo visual (sobrio, colorido, premium, cercano).
6. Cómo habla: tú o usted, palabras suyas, lo que nunca diría.
7. A dónde manda el anuncio y qué acción quiere.

Pídele los archivos y guárdalos en `marca/assets/`: logo (ideal PNG con fondo transparente), fotos del producto o del lugar, y 1 o 2 fotos suyas de cara si quiere salir en los anuncios.

## Paso 2 · Subir los archivos de la marca a Higgsfield (una sola vez)

Para cada archivo de `marca/assets/`:
1. `media_upload` con el nombre del archivo: te devuelve un `upload_url` y un `media_id`.
2. Sube los bytes con curl: `curl -X PUT -H "Content-Type: image/png" --data-binary @marca/assets/logo.png "<upload_url>"` (ajusta el tipo: image/jpeg para .jpg).
3. Cuando el PUT responda 200, `media_confirm` con `type: image` y ese `media_id`.
4. Guarda los ids en `marca/higgsfield.json`: `{"logo": "...", "producto_1": "...", "cara_1": "..."}`. Así no los subes de nuevo.

## Paso 3 · Elegir por dónde partir

Propón partir por **los 10 que mejor le funcionaron a Imperio** (los primeros con compras en `data/formatos.json` o en `RANKING-META.md`) que calcen con su negocio. Sáltate los que piden material que no tiene (por ejemplo, una captura real de un cliente) y díselo.

Después ofrécele seguir por familias hasta recrear la biblioteca completa.

## Paso 4 · Recrear un formato

Para cada formato:

1. **Lee** `formatos/<carpeta>/ficha.md` y **mira** `formatos/<carpeta>/ejemplo.jpg`.
2. **Escribe el texto de la imagen** para la marca, en español, con sus datos reales. Corto: se tiene que leer en 1 segundo.
3. **Escribe el prompt en inglés** partiendo del prompt original de la ficha: mantén la composición, la jerarquía, el tipo de objeto y el estilo; cambia el contenido, los colores y la marca. Pon el texto en español entre comillas y termina con: `Vertical 4:5 feed ad. All on-image text is Spanish and must be rendered EXACTLY as written inside the quotes, with every accent and ñ correct and every digit exact. Do not add any other words, logos or watermarks.`
   - Las reglas de estilo de Imperio (sin signos de apertura, sin guiones largos) son de Imperio. Para esta marca, escribe en español correcto y con sus propias reglas.
4. **Usa el ejemplo como referencia de diseño:** importa la imagen de Imperio con `media_import_url` usando la URL pública:
   `https://raw.githubusercontent.com/benjacord/imperio-fabrica-graficos/main/formatos/<carpeta>/ejemplo.jpg`
   y agrega al prompt: `Use the first reference image ONLY as a layout and style guide (composition, hierarchy, visual treatment). Do not copy any of its text, brand, logo, numbers or people.`
   Suma el logo y, si el formato lleva cara o producto, esas referencias de `marca/higgsfield.json`. Todas van en `medias` con `role: "image_references"`.
5. **Genera** con `generate_image`:
   - Borrador: `model: "gpt_image_2_5"`, `variant: "flare"`, `quality: "medium"`, `resolution: "1k"`, `aspect_ratio: "4:5"` (unos 0,5 créditos).
   - Final aprobado: `variant: "sunburst"`, `quality: "high"`, `resolution: "2k"` (unos 2,75 créditos).
   - Antes de una tanda, calcula el costo con `get_cost: true` y pídele el OK. Si el formato sale bien al primer intento, puedes ir directo al final si la persona prefiere.
   - Si Higgsfield responde con una pregunta sobre generaciones ilimitadas de prueba (`unlim_choice`), házsela a la persona y vuelve a llamar con su respuesta.
6. **Espera y descarga:** con el `job_id` que devuelve la generación, usa `jobs_wait` (o `job_display`) hasta que el trabajo termine; la respuesta trae la URL de la imagen. Descárgala con curl a `salida/AAAAMMDD/<carpeta>_4x5.png`.
7. **Revísalo tú** (lee la imagen) antes de mostrarlo:
   - El texto dice exactamente lo que escribiste: tildes, ñ, cifras, precio.
   - No aparece nada de Imperio (ni la corona, ni "Imperio Agéntico", ni sus cifras).
   - El logo es el de la marca. GPT Image a veces lo redibuja: si sale distinto, rehazlo pidiendo copiarlo exacto desde la referencia, o deja el espacio libre y pon el logo real encima con un editor.
   - Sin manos deformes, sin texto roto, sin cifras cortadas.
   - No inventa prueba: ni testimonios, ni chats de clientes, ni reseñas, ni capturas de resultados.
   - Se lee en el celular.
   Si falla, rehazlo pasando el `job_id` del resultado como referencia y pidiendo cambiar SOLO lo que falló. Máximo 2 intentos; si sigue mal, avísale y pasa al siguiente.
8. **Anota** en `salida/registro.csv`: `fecha,formato,archivo,job_id,creditos,estado`.

Cuando la persona apruebe un formato, ofrécele la versión 9:16 para Stories y Reels: **se rehace con `aspect_ratio: "9:16"`, no se recorta** (se pierde texto). Deja libre el 14% de arriba y el 20% de abajo.

## Paso 5 · Revisar todo junto

Corre `python3 scripts/galeria.py` (en Windows `py scripts\galeria.py`): arma `salida/GALERIA.html` con cada gráfico al lado del ejemplo de Imperio. Ábrelo y repásalo con la persona.

## Paso 6 · Variaciones de un ganador

Cuando un gráfico gane en Meta, la persona puede pedir "hazme 5 variaciones de este". Usa el `job_id` del ganador como referencia y cambia una sola cosa por variación: el texto del titular, el fondo, la persona o el color. Las variaciones van al mismo conjunto de anuncios que el original.

## Paso 7 · Textos y subida

- Escribe `salida/textos-meta.md`: por cada gráfico, un texto principal (2 a 5 líneas, con la oferta real) y un titular de menos de 40 caracteres, con la voz de la persona.
- **A mano:** en el Administrador de anuncios, sube los gráficos a la campaña de prueba y **marca la casilla de contenido generado por IA**.
- **Con el conector de Meta (opcional):** si tiene "Meta Ads" conectado en Claude, puedes subirlos tú. Todo se crea **EN PAUSA** y nada se activa sin su OK explícito.

## Lo que nunca haces

- Inventar testimonios, reseñas, chats de clientes, capturas de resultados, premios, cifras, descuentos o garantías.
- Usar logos o marcas de otras empresas, ni la marca de Imperio, en los anuncios de la persona.
- Gastar créditos sin decir antes cuánto cuesta.
- Publicar o activar anuncios sin su OK.
