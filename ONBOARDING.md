# Guía completa · La Fábrica de Gráficos

> La versión corta está en el PDF (`guia/`). Aquí está todo.

## 1. La idea

En Meta, los anuncios se cansan: cuando la gente ya vio tu creativo muchas veces, el costo por cliente sube. La salida es tener creativos nuevos todo el tiempo, y los estáticos son los más rápidos de producir.

Esta biblioteca reúne 212 formatos que Imperio Agéntico diseñó para sus anuncios. 71 ya corrieron en Meta con plata real (sus resultados están en `formatos/RANKING-META.md`); los demás todavía no se prueban. No son plantillas para copiar: son **estructuras** que funcionan (una boleta, una nota del celular, una tier list, una foto que no parece anuncio) y que Claude rellena con tu marca, tu oferta y tus pruebas reales.

## 2. Instalación

1. Descarga la app de Claude desde [claude.com/download](https://claude.com/download) e inicia sesión (plan pagado: Pro o Max).
2. Crea tu cuenta en [higgsfield.ai](https://higgsfield.ai) y carga créditos.
3. En la app de Claude: **Configuración → Conectores → busca "Higgsfield" → Conectar** e inicia sesión.
4. Entra a la pestaña **Code**, abre un chat nuevo y pega la caja del `README.md` (o de la página de la caja en el PDF).

Claude descarga la biblioteca en tu carpeta Documentos, revisa que Higgsfield esté conectado y te dice cuántos créditos tienes.

## 3. Tu marca

Claude te pregunta, una cosa a la vez: qué vendes, a cuánto, a quién, tus colores, tus pruebas reales y cómo hablas. Te pide tu logo (ideal en PNG con fondo transparente), fotos de tu producto o tu local, y si quieres salir en los anuncios, 1 o 2 fotos tuyas. Lo guarda en la carpeta `marca/` y sube esos archivos a tu cuenta de Higgsfield una sola vez.

## 4. Recrear los formatos

Parte por los 10 que mejor le funcionaron a Imperio (están en `formatos/RANKING-META.md`). Para cada uno, Claude:

1. Lee la ficha y mira el ejemplo de Imperio.
2. Escribe el texto para tu marca, con tus datos reales.
3. Usa el anuncio de Imperio solo como guía de diseño (composición, jerarquía, estilo) y genera tu versión con GPT Image 2.5.
4. La revisa antes de mostrártela: tildes, cifras, precio, manos, que no se cuele nada de Imperio y que no invente pruebas.
5. La guarda en `salida/` y anota cuánto costó.

Antes de cada tanda te dice cuántos créditos va a gastar. Puedes partir con borradores baratos (unos 0,5 créditos) y pasar a la versión final (unos 2,75) solo los que te gusten.

Después puedes seguir por familias: objetos físicos con texto, tipografía dura, pantallas creíbles, fotos nativas, diagramas y datos, humor, prueba social y oferta.

## 5. Revisar y subir

Dile "muéstrame la galería": abre todos tus gráficos al lado del formato que los inspiró. Pide cambios con palabras normales ("el titular más grande", "sin la persona", "más sobrio").

Para subirlos:
- **A mano:** en el Administrador de anuncios, dentro de tu campaña de prueba. Marca la casilla de **contenido generado por IA**.
- **Con el conector de Meta Ads** (si lo tienes conectado en Claude): Claude los sube y quedan **en pausa** hasta que tú los actives.

Lee `buenas-practicas.md` antes de tu primera tanda: ahí está cómo testear, cuándo apagar y cuándo refrescar.

## 6. Preguntas frecuentes

**Necesito saber diseñar?** No. Tú decides qué te gusta; Claude y GPT Image 2.5 hacen el resto.

**Cuánto cuesta?** El kit es gratis. Pagas tu plan de Claude y los créditos de Higgsfield que uses: unos 2,75 por gráfico final.

**Se van a parecer a los de Imperio?** La estructura sí, el contenido no. Claude usa el ejemplo solo como guía de composición y revisa que no se cuele nada de Imperio.

**Puedo usar testimonios?** Solo reales y con permiso. Si un formato necesita una captura de un cliente y no la tienes, Claude te lo dice y pasa al siguiente.

**Y los videos?** Para videos está la Fábrica de Videos (el sistema Lego): github.com/benjacord/imperio-fabrica-videos

---

Imperio Agéntico · Curso Claude para Meta Ads · skool.com/imperio
