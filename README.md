<p align="center"><img src="guia/assets/corona.png" width="84" alt="Imperio Agéntico"></p>

<h1 align="center">La Fábrica de Gráficos</h1>
<p align="center"><b>212 formatos de anuncios estáticos de Imperio (71 ya probados con plata real), recreados para tu marca.</b><br>
Un recurso de <b>Imperio Agéntico</b> para el curso <i>Claude para Meta Ads</i>. Con Claude Code, Higgsfield y GPT Image 2.5.</p>

---

Esta es la biblioteca de formatos que Imperio Agéntico diseñó para su laboratorio de anuncios en Meta: 212 formatos, de los que 71 ya corrieron con plata real. Cada formato trae el anuncio real, por qué funciona, cuándo usarlo, el texto que llevó y el prompt con que se hizo. Claude conoce tu marca, recrea cada formato para tu negocio con GPT Image 2.5 dentro de Higgsfield y revisa cada imagen antes de mostrártela.

**Con plata real:** entre el 28 de agosto y el 5 de octubre de 2026, los gráficos de Imperio promediaron **$54 por compra** (237 compras), mientras las campañas de compra de toda la cuenta promediaron unos $83. Los que mejor rindieron están en [`formatos/RANKING-META.md`](formatos/RANKING-META.md).

## Qué necesitas

- Un computador (Mac o Windows).
- La app de Claude con un plan pagado (Pro o Max), para usar Claude Code.
- Una cuenta de [Higgsfield](https://higgsfield.ai) con créditos, conectada a Claude. Cada gráfico final cuesta unos 2,75 créditos (un borrador, unos 0,5).
- Unos 20 minutos la primera vez.

## Cómo se instala: 3 pasos

1. **Claude y Higgsfield.** Descarga la app de Claude desde [claude.com/download](https://claude.com/download) e inicia sesión. Conecta Higgsfield: **Configuración → Conectores → busca "Higgsfield" → Conectar**.
2. **Pega la caja de abajo** en un chat nuevo de la pestaña **Code**. El link de este repositorio ya va adentro.
3. **Responde sus preguntas.** Te pregunta por tu marca, te pide tu logo y tus fotos, te dice cuánto va a costar y recrea los 10 formatos que mejor le funcionaron a Imperio.

### La caja para pegar

```text
Vas a instalar la "Fábrica de Gráficos" de Imperio Agéntico en este computador. NO soy
técnico: haz todo tú, nunca me pidas correr un comando ni editar un archivo a mano, y
explícame cada paso en español simple. Mantén una lista de tareas visible y ve marcando
lo que terminas.

1) DESCARGA EL KIT (en mi carpeta Documentos)
   git clone https://github.com/benjacord/imperio-fabrica-graficos.git
   Si no hay git, baja este ZIP y descomprímelo ahí:
   https://github.com/benjacord/imperio-fabrica-graficos/archive/main.zip
   Trabaja siempre dentro de esa carpeta y lee su CLAUDE.md antes de seguir.

2) REVISA HIGGSFIELD
   Confirma que tienes las herramientas de Higgsfield. Si no están, guíame para
   conectarlo y espera a que te avise. Dime cuántos créditos tengo.

3) CONOCE MI MARCA (UNA pregunta a la vez)
   Qué vendo y a cuánto, a quién, mis colores, mis pruebas reales y cómo hablo.
   Pídeme el logo y mis fotos (los arrastro aquí). Guárdalo todo en la carpeta marca.

4) RECREA PARA MI NEGOCIO LOS 10 QUE MEJOR LE FUNCIONARON A IMPERIO
   Antes de generar, dime cuántos créditos cuesta. Muéstrame cada gráfico, corrige
   lo que esté mal y guárdalos en la carpeta salida.

5) SIGUE CON EL RESTO
   Cuando apruebe esos 10, ofréceme seguir por familias hasta recrear toda la
   biblioteca, en 4:5 y en 9:16.

Ten paciencia, asume que nunca he usado una terminal y usa solo este kit.
```

## Ya instalado: solo háblale

| Le dices | Qué pasa |
|---|---|
| "recrea los 10 que mejor le funcionaron a Imperio" | Tus versiones de los formatos con más compras |
| "hazme toda la familia de objetos físicos" | Recrea una familia completa de la biblioteca |
| "pásalo a 9:16" | Lo rehace en vertical para Stories y Reels |
| "hazme 5 variaciones de este ganador" | El mismo ángulo con otro titular, fondo o persona |
| "escribe los textos para Meta" | Texto principal y titular para cada gráfico |
| "muéstrame la galería" | Tus gráficos al lado del formato que los inspiró |

## Qué hay adentro

| Carpeta | Para qué |
|---|---|
| `formatos/` | La biblioteca: una carpeta por formato con `ejemplo.jpg` y `ficha.md`. Empieza por [`INDICE.md`](formatos/INDICE.md) |
| `buenas-practicas.md` | Las reglas para que un gráfico venda (y lo que nunca se hace) |
| `CLAUDE.md` | El manual que lee Claude: entrevista, prompts, costos y revisión |
| `data/formatos.json` | La biblioteca en formato de datos, ordenada por familia y por resultado |
| `marca/` | Tu marca: lo que Claude aprende de tu negocio, tu logo y tus fotos |
| `salida/` | Tus gráficos, el registro de lo que costó y la galería |
| `guia/` | La guía en PDF |

Nunca inventa testimonios, reseñas, capturas de clientes ni cifras: si un formato necesita prueba real y no la tienes, te lo dice y lo salta.

---

<p align="center"><sub>Imperio Agéntico · skool.com/imperio · Curso Claude para Meta Ads de Benja (@bencord)</sub></p>
