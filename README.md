# Proyecto

Para proyecto final de esta materia crearemos un pequeño compilador, para un lenguaje con las siguientes funcionalidades:

## Operaciones permitidas

### Aritméticas

- Suma +
- Resta -
- Multiplicación *
- División /
- Exponenciación ^

### Comparación

- ==
- !=
- \>
- <
- \>=
- <=

### Booleanas

- and
- or

### Operaciones de bloques

- ( )
- { }

## Un sistema de tipos

- Int
- Float
- Boolean

## Operaciones permitidas entre el sistema de tipos

|         | int                      | float                    | boolean         |
|---------|--------------------------|--------------------------|-----------------|
| int     | Aritmeticas, comparacion | Aritmeticas, comparacion | ----            |
| float   | Aritmeticas, comparacion | Aritmeticas, comparacion | ----            |
| boolean | ----                     | ----                     | and, or, ==, != |

## Flujos de control existentes, deberán seguir una estructura similar al lenguaje C, por simplicidad todo deberán llevar llaves

- If, else, elif
- while ( ) { }
- for ( ; ; ) { }

Para marcar el final de una sentencia se utilizara "**;**"

Es permitido el declarar y asignar una variable en la misma linea

---

La salida de este compilador debe de ser codigo de 3 direcciones.

Para la entrega de este proyecto es un repositorio de git (puede ser de github, gitlab o bitbucket).

Para la parte de análisis sintáctico [ply](https://www.dabeaz.com/ply/ply.html)

Ejemplos: [Dabeaz examples](https://github.com/dabeaz/ply/blob/master/example/)

---
