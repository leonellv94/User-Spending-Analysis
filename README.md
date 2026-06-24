User Spending Analysis (Manual Aggregation)

Este proyecto simula un conjunto de transacciones y procesa los datos usando Python puro (sin librerías como pandas).

Objetivo

Practicar la lógica de agrupación y agregación de datos desde cero, sin utilizar herramientas como groupby.

Qué hace

A partir de un dataset generado aleatoriamente, calcula por usuario:

Total gastado

Promedio de gasto
Top 3 transacciones
Categoría con mayor gasto
Categoría con menor gasto
Cantidad de transacciones
Enfoque

Se utiliza una estructura de diccionarios anidados para:

Agrupar datos dinámicamente por usuario
Manejar categorías sin hardcodearlas
Acumular métricas en una sola pasada
Motivación

El objetivo fue entender cómo funcionan estas operaciones “por debajo”, en lugar de depender directamente de librerías externas.
