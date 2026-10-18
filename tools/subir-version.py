#!/usr/bin/env python3
"""
Sube el número de versión de la web y lo pone en todas las direcciones de los
archivos (pantalla.css?v=..., pantalla.js?v=..., menu.js?v=...).

Para qué: un navegador, sobre todo el de un televisor, puede quedarse con una
copia vieja del JS aunque la página sea nueva, y mezclar las dos. Cambiando el
número, la dirección del archivo cambia y no le queda más remedio que pedir el
nuevo.

    python3 tools/subir-version.py           # fecha de hoy + contador
    python3 tools/subir-version.py 2026-10-18.3
"""
import datetime
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVOS = ['index.html', 'pantalla/index.html']
VERSION_TXT = os.path.join(RAIZ, 'version.txt')


def siguiente():
    hoy = datetime.date.today().isoformat()
    anterior = open(VERSION_TXT).read().strip() if os.path.exists(VERSION_TXT) else ''
    if anterior.startswith(hoy + '.'):
        return f'{hoy}.{int(anterior.split(".")[-1]) + 1}'
    return f'{hoy}.1'


def main():
    v = sys.argv[1] if len(sys.argv) > 1 else siguiente()
    for rel in ARCHIVOS:
        ruta = os.path.join(RAIZ, rel)
        s = open(ruta).read()
        # quita la versión anterior y pone la nueva en css, js y datos propios
        s = re.sub(r'((?:href|src)="(?:\.\./)?(?:assets/css/styles\.css|assets/js/app\.js|'
                   r'data/menu\.js|pantalla\.css|pantalla\.js))(\?v=[^"]*)?"',
                   lambda m: f'{m.group(1)}?v={v}"', s)
        s = re.sub(r'<meta name="version" content="[^"]*">', f'<meta name="version" content="{v}">', s)
        open(ruta, 'w').write(s)
    open(VERSION_TXT, 'w').write(v + '\n')
    print('versión', v)


if __name__ == '__main__':
    main()
