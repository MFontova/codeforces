# 📝 Problema de Abreviatura de Palabras Largas

A veces, algunas palabras como "localization" (localización) o "internationalization" (internacionalización) son tan largas que escribirlas muchas veces en un texto resulta bastante tedioso.

Consideraremos que una palabra es **demasiado larga** si su longitud es **estrictamente mayor a 10 caracteres**. Todas las palabras demasiado largas deben ser reemplazadas por una abreviatura especial.

## 📐 Formato de la Abreviatura

Esta abreviatura se forma de la siguiente manera:

1.  Se escribe la **primera** letra de la palabra.
2.  Se escribe el **número de letras** que hay *entre* la primera y la última letra (en sistema decimal y sin ceros a la izquierda).
3.  Se escribe la **última** letra de la palabra.

### Ejemplos:

* "localization" (12 caracteres) → **l10n** (10 letras entre 'l' y 'n')
* "internationalization" (20 caracteres) → **i18n** (18 letras entre 'i' y 'n')

Se te sugiere automatizar el proceso de cambiar las palabras por abreviaturas. En este proceso, todas las palabras demasiado largas deben ser reemplazadas por la abreviatura, y las palabras que no son demasiado largas no deben sufrir ningún cambio.

---

## Entrada (Input)

La primera línea contiene un número entero $n$ ($1 \le n \le 100$), que indica la cantidad de palabras a procesar.

Cada una de las siguientes $n$ líneas contiene una palabra. Todas las palabras consisten en letras latinas minúsculas y tienen una longitud de **1 a 100 caracteres**.

## Salida (Output)

Imprime $n$ líneas. La $i$-ésima línea debe contener el resultado del reemplazo de la $i$-ésima palabra de los datos de entrada.

---

### Ejemplo de Caso
| input | output |
| :--- | :--- |
| 4 | |
| word | word |
| localization | l10n |
| internationalization | i18n |
| pneumonoultramicroscopicsilicovolcanoconiosis | p43s |
