# Sistema Experto para Logística

## Descripción

Este proyecto es un sistema experto diseñado para optimizar y gestionar operaciones logísticas utilizando lógica difusa. El sistema toma decisiones basadas en reglas predefinidas para mejorar la eficiencia en áreas como la gestión de inventarios, la disponibilidad de personal y el tiempo de entrega.

## Características

- **Gestión de Inventarios**: Ayuda a determinar cuándo y cuánto reabastecer.
- **Disponibilidad de personas**: Optimiza la disponibilidad de personal para reducir costos.
- **Tiempo de entrega**: Calcula el tiempo de entrega desde la demanda y la disponibilidad de personal.
- **Interfaz Gráfica de Usuario (GUI)**: Permite a los usuarios ingresar datos y ver los resultados de las inferencias de manera intuitiva.

## Requisitos

- Python 3.11
- Bibliotecas adicionales:
  - `numpy`
  - `matplotlib`
  - `skfuzzy`
  - `tkinter` (incluido con Python)

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/heguzman/Sistema-Experto-Logistica.git
    cd sistema-experto-logistica
    ```

2. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python3.11 -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install numpy matplotlib scikit-fuzzy
    ```

## Uso

1. Ejecuta el sistema experto:
    ```bash
    python main.py
    ```

2. Interactúa con la interfaz gráfica para ingresar los datos requeridos y obtener las recomendaciones y resultados generados por el sistema experto.

## Estructura del Proyecto

<p>sistema-experto-logistica/<br>
├── README.md <br> 
├── main.py<br>
├── SE_Pedido.py<br>
├── SE_Disponibilidad_Personal.py<br>
└── SE_Tiempo_De_Entrega.py</p>

- **main.py**: Punto de entrada principal del sistema.
- **SE_Pedido.py**: Sistema Experto de Pedidos.
- **SE_Disponibilidad_Personal.py**: Sistema Experto de Disponibilidad de personal.
- **SE_Tiempo_De_Entrega.py**: Sistema Experto de Tiempo de espera.
