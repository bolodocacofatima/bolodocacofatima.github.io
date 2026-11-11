# Pantalla del stand

Bucle en 16:9 para el televisor del stand. Ahora mismo son doce pantallas y
82 segundos: portada; Fátima, con la Virgen y las banderas de Portugal y de
Madeira; el bolo solo; la promoción de dos; el de margarina de ajo; el prego
(solo, mientras la bifana no se venda); los dos chorizos juntos; el de Nutella; el bolo de mel con las broas; el chorizo por
kilo con la margarina; el evento del día; y el cierre con el Instagram.

Los productos marcados con `hidden: true` en `data/menu.js` (hoy: la
bifana y las dos espetadas) no salen ni aquí ni en el menú del QR. Al
quitarles la marca vuelven solos, cada uno con su pareja: prego con bifana,
y las dos espetadas juntas.

La Virgen y las banderas también quedan fijas arriba a la derecha, haciendo
pareja con el logo de la izquierda, en todas las pantallas salvo la de
Fátima, donde ya salen en grande. La Virgen de la esquina va en negro sobre
las pantallas claras y en crema sobre las oscuras (portada y cierre).

El evento del día tiene su propio interruptor aquí, independiente del menú
del QR: `MOSTRAR_EVENTO` en `pantalla/pantalla.js`. Ahora está en `true`:
el evento sale en una pantalla de 12 segundos antes del cierre. Si el evento
trae `note` en `data/menu.js` (como el de Parceiros Banda Show), esa pantalla
es la de agradecimiento, con el logo de los invitados; si no, la de siempre,
con el nombre, el texto y los datos (hora, lugar…). Para quitarla del
televisor sin tocar el menú, pon `MOSTRAR_EVENTO = false`.

Los productos que se comparan entre sí comparten pantalla: así se ve la
diferencia de precio de un vistazo, sin tener que recordar la anterior.

## Dos formas de usarlo

**Televisor con pendrive** → copia `menu-pantalla-1080p.mp4` al pendrive,
conéctalo al televisor y activa la repetición automática (en el menú del
televisor suele llamarse *Repeat* o *Repetir todo*). 1920×1080, H.264, sin
audio: lo reproduce cualquier televisor de los últimos quince años.

**Televisor con navegador, o laptop conectada** → abre
**https://bolodocacofatima.github.io/pantalla/** y pulsa el botón de pantalla
completa que sale abajo a la derecha (en una laptop, también sirve **F11**).
El botón se esconde solo a los cuatro segundos y vuelve al mover el ratón o
pulsar cualquier tecla del control.

Es la mejor opción de las dos: se ve más nítido que el video, los precios
salen directamente de `data/menu.js` y se actualizan solos. La página pide
además que la pantalla no se apague mientras corre el bucle.

Una vez cargada no necesita internet: todo queda descargado y el bucle sigue
aunque se caiga la conexión.

## Se pone al día sola

Con la página abierta, cada cinco minutos mira `version.txt`. Si se publicó
una versión nueva, descarga los datos y los estilos sin recargar (así no se
pierde la pantalla completa) y los estrena al terminar la vuelta, desde la
portada. Un cambio en el evento, un producto o un precio llega solo al
televisor en unos minutos.

Lo único que no llega solo es un cambio en `pantalla.js`: ese pide recargar
la página una vez.

## Si algo nuevo no aparece en el televisor

Pulsa cualquier tecla del control: junto al botón de pantalla completa sale
la **versión** que tiene cargada. Si no coincide con la última, el televisor
está usando una copia vieja: recarga la página, y si sigue igual, espera diez
minutos (lo que tarda GitHub en dejar de servir la anterior) y vuelve a
recargar.

## Si se ve oscura

La pantalla solo tiene versión clara y le dice al navegador que no la
oscurezca. Si aun así sale con fondo gris oscuro y la Virgen casi invisible,
el navegador del televisor tiene forzado su propio **modo oscuro**: hay que
desactivarlo en sus ajustes (suele llamarse «Modo oscuro», «Tema oscuro» o
«Forzar modo oscuro en sitios web»).

Cada vez que se cambia algo hay que subir la versión, para que los navegadores
no mezclen archivos nuevos con viejos:

```bash
python3 tools/subir-version.py
```

## Cuando cambien los precios

La página se actualiza sola. **El video no**: hay que volver a generarlo.

```bash
npm install playwright
pip install imageio-ffmpeg

python3 -m http.server 8340            # desde la raíz del proyecto
node tools/generar-video.js http://localhost:8340 pantalla/menu-pantalla-1080p.mp4
```

Tarda unos cuatro minutos. Dibuja el bucle fotograma a fotograma en vez de
grabar en tiempo real, así que sale idéntico en cualquier equipo y no se
pierde ningún cuadro.

## Ajustes

En `pantalla/pantalla.js`, arriba del todo:

| Variable | Qué hace |
|---|---|
| `DURACION` | Segundos de cada tipo de pantalla: portada, producto, pareja, evento y cierre |
| `FUNDIDO` | Segundos de cruce entre una y la siguiente |
| `PAREJAS` | Qué productos comparten pantalla, por su `id` |
| `MOSTRAR_EVENTO` | Si el evento del día sale también en el televisor |
| `LANG` | `'es'` o `'pt'` — el idioma de la pantalla del stand |

Al añadir un producto en `data/menu.js` aparece solo, en su propia pantalla.
Para que comparta pantalla con otro, añade la pareja a `PAREJAS`. Si un
producto de una pareja se borra, el otro pasa a mostrarse solo: no se rompe
nada.
