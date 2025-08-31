# Puntos de Silla

Este proyecto es el resultado para un ejercicio de Exercism.com, una página conocida por ofrecer ejercicios para practicar cualquier idioma de programación. El ejercicio consistía en encontrar el mejor árbol para construir una casa; el más alto de este a oeste para tener la mejor vista del anochecer y el amanecer, y el más bajo de norte a sur para minimizar la cantidad de árboles a escalar. Básicamente, un típico ejercicio de Puntos de Silla (Saddle Points).
Este ejercicio avanzado en Exercism fue el último que completé antes de empezar a crear mis propios proyectos para mi portafolio. Edité el código ligeramente para que se pueda ejecutar sin necesidad de depender de todos los archivos que vienen con el test o el programa de Exercism para completar y depurar sus ejercicios; simplemente podrás ejecutar el código en la consola con Python 3.

## Habilidades Demostradas
- Manejo de matrices y estructuras de datos.
- Algoritmos para encontrar máximos y mínimos.
- Resolución de problemas lógicos.

## Cómo Ejecutarlo
1. Tener Python 3 instalado y clonar el repo.
2. Navegar al directorio del archivo.
3. Ejecutar el comando de `python`, `py` o `python3` seguido del nombre del archivo y la matriz en formato de lista de listas. Por ejemplo:
    ```bash
    python saddle_points.py "[matriz]"
    ```

## Notas importantes

- Formato de la entrada:

    - La matriz debe estar en formato de lista de listas de Python, con corchetes y comas, como `"[[6, 7, 8], [5, 5, 5], [7, 5, 6]]"`.
    - Asegarate de encerrar la matriz entre comillas dobles en la consola para que se pase como un solo argumento.
    - Los elementos de la matriz deben ser números (enteros o flotantes).

Por ejemplo:

    ```bash
    python saddle_points.py "[[9, 8, 7], [5, 3, 2], [6, 6, 7]]"
    ```

![Ejemplo 1](https://files.catbox.moe/v39d4i.png)

    ```bash
    python saddle_points.py "[[6, 7, 8], [5, 5, 5], [7, 5, 6]]"
    ```

![Ejemplo 2](https://files.catbox.moe/lndyzq.png)







