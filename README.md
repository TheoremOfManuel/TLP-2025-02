# BrickLang — Lenguaje para juegos de “ladrillos” (Tetris-like)
**Materia:** Teoría de Lenguajes de Programación · **Semestre:** 2025-2

Este repositorio alberga el diseño, especificación e implementación inicial de **BrickLang**, un lenguaje **simple y declarativo** para definir mecánicas de juegos tipo “ladrillos” (p. ej., Tetris y variantes). Su propósito es académico: conectar **conceptos formales de lenguajes** (léxico, sintaxis, semántica, gramáticas, AST) con una **aplicación práctica** y entretenida.

---

## Objetivos del repositorio
- **Diseñar** una sintaxis mínima, legible y fácil de enseñar.
- **Formalizar** una gramática compacta y su semántica operacional.
- **Implementar** un intérprete de referencia (runtime) y un verificador estático básico.
- **Ilustrar** patrones de construcción de lenguajes: *lexer → parser → AST → semántica → ejecución*.
- **Proveer** ejemplos reproducibles y casos de prueba.

---

## Principios de diseño del lenguaje
- **Legible primero:** cercano a configuración humana (clave=valor, listas, secciones).
- **Declarativo:** describir *qué* reglas existen y *cuándo* se activan (eventos), no *cómo* se implementan internamente.
- **Seguro y mínimo:** tipos básicos, validación de esquema y límites (p. ej., tamaño de tablero).
- **Portabilidad:** intérprete de referencia en **Python**; gramática agnóstica a la plataforma.
- **Extensible:** nuevas piezas, eventos y acciones sin romper compatibilidad.
---


