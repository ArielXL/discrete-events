# Poblado en Evolución

## Sobre el Autor

| **Nombre y Apellidos** | Grupo |              **Correo**              |              **GitHub**               |
| :--------------------: | :---: | :----------------------------------: | :-----------------------------------: |
|  Ariel Plasencia Díaz  | C-412 | a.plasencia@estudiantes.matcom.uh.cu | [ArielXL](https://github.com/ArielXL) |

## Sobre el Proyecto

El objetivo de este proyecto es conocer la evolución de la población en una determinada región. Este cambio de la población está marcado por las distribuciones de probabilidades tanto uniforme como exponencial en diferentes acciones a realizar.

## Sobre la Implementación

La implementación se encuentra totalmente en `python 3`. Es recomendable tener conocimientos avanzados de este lenguaje de programación para un mejor y mayor entendimiento de las implementaciones propuestas. 
Para instalar todas las librerías usadas escriba la siguiente línea: 

```bash
pip3 install -r requirements.txt
```

## Sobre la Ejecución

Para la ejecución, escriba las siguientes líneas en una terminal abierta en este directorio:

```python
cd src/
python3 main.py -w <count_women> -m <count_men>
```

Los parámetros `count_women` y `count_men` representan la cantidad de mujeres y de hombres inicial de nuestra población respectivamente. Sus valores por defectos son $50$ para cada uno.

Ademas, proveemos un `makefile`, el cual, nos ofrece una mayor interacción con nuestro proyecto. A continuación, mostramos sus funcionalidades.

```bash
run                            Run the project :)
info                           Display project description
version                        Show the project version
install                        Install the project dependencies
clean                          Remove temporary files
help                           Show this help
```

## Sobre el Informe

El informe de trabajo debe contener los siguientes elementos:

* Generales del estudiante (nombre, apellidos, grupo y correo).
* Orden del problema asignado.
* Principales ideas seguidas para la solución del problema.
* Modelo de simulación de eventos discretos desarrollado para resolver el problema.
* Consideraciones obtenidas a partir de la ejecución de las simulaciones del problema.
* Enlace al repositorio del proyecto en GitHub.

## Sobre las Referencias

1. [Conferencia de Eventos Discretos](./doc/eventos-discretos.pdf)
2. [Libro de Simulación](./doc/temas-de-simulacion.pdf)
3. [Orientaciones](./doc/proyecto-eventos-discretos.pdf)

