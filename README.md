# Sistema de Gestión de Restaurante

**Estudiante:** Antony Jordano Defaz Diaz  
**Materia:** Programación Orientada a Objetos  
**Semestre:** Segundo Semestre - UEA Tecnologías de la Información  

---

# Sistema de Gestión de Restaurante - Semana 12

Este proyecto implementa un **Sistema de Gestión de Restaurante** desarrollado en Python, estructurado bajo los principios fundamentales de la **Programación Orientada a Objetos (POO)** y patrones de arquitectura de software desacoplados.

En esta entrega (Semana 12), el sistema ha sido refactorizado para garantizar un rendimiento óptimo de búsqueda $O(1)$, eliminar el código duro (*hardcoding*) en la interfaz y cumplir con los más altos estándares de calidad arquitectónica.

---

## 🛠️ Arquitectura del Proyecto

El sistema aplica el principio de **separación de responsabilidades** (SoC) organizándose en las siguientes capas:

```text
restaurante_app/
│
├── datos/                      # Capa de Persistencia (Archivos JSON)
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/                    # Capa de Dominio (Entidades POO)
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/                  # Capa de Lógica de Negocio y Servicios
│   ├── archivo_servicio.py     # Manejo de I/O y lectura/escritura JSON
│   └── restaurante.py          # Gestor principal e indexación en memoria
│
└── main.py                     # Capa de Presentación (Interfaz de Consola)