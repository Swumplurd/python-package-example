# python-package-example

<img align="right" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" height="150px">

Ejemplo para crear un paquete en python y posteriormente poderlo instalar usando `pip`

### Uso

Dentro del directorio del proyecto abrir una terminal y correr el siguiente comando:

```bash
python setup.py sdist
```

Posteriormente se crearan los siguientes directorios dentro de nuestra carpeta de proyecto con lo cual la nueva estructura de carpetas es la siguiente:

```
python-package-example/
|-- README
|-- setup.py
|-- basicops.egg-info/
|-- dist/
|-- basicops/
|   |-- __init__.py
|   |-- division.py
|   |-- multiplicacion.py
|   |-- resta.py
|   |-- suma.py
|-- tests/
```

Ahora tenemos que movernos dentro de la carpeta `dist/` y correr el siguiente comando:

```bash
pip install <nombre_del_comprimido>
```

El nombre del comprimido en este caso es: `basicops-0.0.1.tar.gz`

Y finalmente nuestro paquete `basicops` estara disponible localmente para su uso.

---

Cualquier duda o sugerencia al contenido del precente repositorio contactame en Discord: Swumplurd#3977
