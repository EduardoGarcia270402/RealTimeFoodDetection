# 🥗🍽️ Sistema Inteligente de Recomendación Nutricional con Visión por Computadora

Este proyecto consiste en el desarrollo de un sistema inteligente que combina **visión por computadora** y **procesamiento de lenguaje natural (PLN)** para detectar alimentos en tiempo real y generar **recomendaciones nutricionales personalizadas**. El sistema está orientado principalmente a deportistas, especialmente peleadores de artes marciales mixtas (MMA/UFC), durante procesos de control y corte de peso.

La aplicación fue desarrollada como una aplicación web utilizando **Flask**, integrando un modelo **YOLO** para la detección automática de alimentos a través de imágenes o cámara web, y un sistema experto que analiza el impacto nutricional de los alimentos detectados.

---

## 🎯 Objetivo del Sistema

El objetivo principal del sistema es apoyar la toma de decisiones alimenticias mediante el reconocimiento automático de alimentos y la generación de recomendaciones nutricionales basadas en el perfil del usuario y su objetivo físico (corte de peso, mantenimiento o ganancia).

El sistema no busca reemplazar a un profesional de la salud, sino brindar una **guía informativa y tecnológica** que facilite el control nutricional diario.

---

## 🥦 Alimentos Detectables

El sistema puede detectar los siguientes alimentos, los cuales forman parte de una base de conocimiento nutricional:

- **Banana**
- **Black Beans**
- **Grilled Chicken Breast**
- **Milk**
- **Orange Juice**
- **Pizza**
- **Potato**
- **Salad**
- **Spaghetti**
- **White Rice**

Cada alimento cuenta con información asociada como calorías, macronutrientes, beneficios, desventajas y un menú sugerido, lo que permite generar recomendaciones más completas.

---

## 🧠 Sistema de Recomendación Nutricional

Una vez detectados los alimentos, el sistema evalúa su impacto nutricional utilizando reglas semánticas y una ponderación definida para cada clase. Las recomendaciones se generan considerando:

- Perfil del usuario (peso, estatura, objetivo)
- Calorías aproximadas
- Beneficios y contras del alimento
- Compatibilidad con el objetivo físico del usuario

El resultado es una recomendación clara y entendible que apoya el control alimenticio del deportista.

---

## 🎥 Visión por Computadora y Funcionamiento

- **Captura de Video**: Uso de OpenCV para capturar imágenes desde la cámara o archivos locales.
- **Detección**: Modelo YOLO entrenado para reconocer alimentos en tiempo real.
- **Visualización**: Se muestran bounding boxes, nombres de alimentos y resultados del análisis nutricional.
- **Interacción**: El usuario puede ingresar su perfil y recibir recomendaciones dinámicas.

---

## 🏗️ Arquitectura del Sistema

1. **Visión por Computadora**: YOLO para detección de alimentos.
2. **Procesamiento de Imágenes**: OpenCV.
3. **Backend Web**: Flask.
4. **Sistema Experto**: Reglas nutricionales y base de conocimiento.
5. **Interfaz Web**: Visualización del video y recomendaciones.

---

## 🛠️ Herramientas y Tecnologías Utilizadas

- **Python** – Lenguaje principal del proyecto.
- **YOLO (Ultralytics)** – Detección de objetos en tiempo real.
- **OpenCV** – Procesamiento de imágenes y video.
- **Flask** – Desarrollo de la aplicación web.
- **Flask-SocketIO** – Comunicación en tiempo real.
- **HTML/CSS/JavaScript** – Interfaz de usuario.

---

## 🚀 Ejecución del Proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/EduardoGarcia270402/RealTimeFoodDetection.git

Install dependencies: pip install -r requirements.txt
Run the application: python app.py
Navigate to http://localhost:5000/
