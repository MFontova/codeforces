# 📝 Problema: Formación de Equipos (Team)

Un día, tres mejores amigos, Petya, Vasya y Tonya, decidieron formar un equipo y participar en concursos de programación. Generalmente, a los participantes se les ofrecen varios problemas durante los concursos. Mucho antes del inicio, los amigos decidieron que implementarán una solución a un problema si **al menos dos** de ellos están seguros de la solución. De lo contrario, los amigos no escribirán la solución del problema.

Este concurso ofrece $n$ problemas a los participantes. Para cada problema, se sabe qué amigo está seguro de la solución. Ayuda a los amigos a encontrar el número de problemas para los cuales escribirán una solución.

## Entrada (Input)

La primera línea de entrada contiene un único número entero $n$ ($1 \le n \le 1000$), que es el número de problemas en el concurso.

Luego, siguen $n$ líneas, cada una conteniendo **tres números enteros** separados por espacios, donde cada entero es $0$ o $1$.

* Si el primer número en la línea es $1$, Petya está seguro de la solución del problema; de lo contrario, no lo está.
* El segundo número muestra la opinión de Vasya sobre la solución.
* El tercer número muestra la opinión de Tonya sobre la solución.

## Salida (Output)

Imprime un único número entero: la cantidad total de problemas que los amigos implementarán en el concurso.

---

### Ejemplo de Caso

| Entrada | Salida Esperada |
| :--- | :--- |
| 3 | 2 |
| 1 1 0 | |
| 1 1 1 | |
| 0 0 0 | |

**Explicación del Ejemplo:**

1.  **Problema 1 (1 1 0):** Hay 2 votos seguros ($\ge 2$), **se resuelve**.
2.  **Problema 2 (1 1 1):** Hay 3 votos seguros ($\ge 2$), **se resuelve**.
3.  **Problema 3 (0 0 0):** Hay 0 votos seguros ($< 2$), **no se resuelve**.

Total de problemas resueltos: **2**.