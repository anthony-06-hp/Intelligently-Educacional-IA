# INTELLIGENTLY
### Sistema Inteligente de Análisis Educativo mediante Inteligencia Artificial

INTELLIGENTLY es una plataforma educativa desarrollada con Python y Django que utiliza técnicas de inteligencia artificial y visión computacional para apoyar el control de asistencia, el análisis de la actividad en el aula y la generación de reportes educativos.

## Autor

**Anthony Hernández**
Estudiante de Ingeniería de Software  
Universidad Estatal de Milagro (UNEMI).

Proyecto académico desarrollado como parte del proceso de formación en Ingeniería de Software.

## Descripción del proyecto

INTELLIGENTLY es un sistema de apoyo educativo diseñado para facilitar el seguimiento de los estudiantes durante las sesiones educativas, mediante el uso de herramientas de inteligencia artificial, procesamiento de imágenes y aprendizaje automático.

La plataforma busca proporcionar información útil para los docentes mediante la automatización de determinadas tareas relacionadas con el registro de asistencia, el análisis de las sesiones y la generación de informes.

El sistema está orientado principalmente a entornos educativos virtuales e híbridos, donde resulta importante contar con herramientas que faciliten la gestión y el seguimiento de las actividades académicas.

## Objetivo general

Desarrollar un sistema inteligente capaz de procesar información de sesiones educativas mediante técnicas de visión computacional y aprendizaje automático, con el propósito de apoyar el seguimiento de la asistencia y la actividad de los estudiantes.

## Problemática

En los entornos educativos virtuales e híbridos, los docentes pueden enfrentar dificultades para realizar un seguimiento continuo de la asistencia y participación de los estudiantes.

Entre las principales dificultades identificadas se encuentran:

- Registro manual de la asistencia.
- Dificultad para realizar un seguimiento de las sesiones educativas.
- Limitaciones para organizar y analizar información de las clases.
- Falta de herramientas automatizadas para generar reportes.
- Necesidad de contar con información que facilite el seguimiento académico.

INTELLIGENTLY busca contribuir al tratamiento de estas dificultades mediante herramientas tecnológicas que apoyen la gestión y el análisis de la información educativa.

## Características principales

- **Gestión de usuarios:** organización de cuentas y acceso a las funcionalidades del sistema.
- **Control de asistencia:** registro y seguimiento de la asistencia estudiantil.
- **Visión computacional:** captura y procesamiento de imágenes mediante OpenCV.
- **Aprendizaje automático:** utilización de modelos de Machine Learning para tareas de reconocimiento y clasificación.
- **Gestión de sesiones:** organización de sesiones educativas y funcionalidades relacionadas con videollamadas.
- **Generación de reportes:** organización y presentación de información sobre asistencia y sesiones educativas.
- **Panel administrativo:** gestión de información y funcionalidades del sistema mediante Django.

## Tecnologías utilizadas

El proyecto utiliza diferentes tecnologías para el desarrollo web, procesamiento de imágenes, aprendizaje automático y gestión del desarrollo.

### Backend y desarrollo web

- **Python:** lenguaje de programación principal del proyecto.
- **Django:** framework utilizado para desarrollar la aplicación web, gestionar usuarios y organizar la lógica del sistema.
- **SQLite:** sistema de gestión de base de datos utilizado en el entorno de desarrollo.

### Inteligencia artificial y procesamiento de imágenes

- **OpenCV:** biblioteca utilizada para el procesamiento de imágenes y tareas de visión computacional.
- **Scikit-learn:** biblioteca empleada para implementar algoritmos de aprendizaje automático.
- **Joblib:** herramienta utilizada para guardar y cargar modelos entrenados y objetos asociados al procesamiento de datos.

### Herramientas de desarrollo y gestión

- **Git y GitHub:** control de versiones y alojamiento del código fuente.
- **PlantUML:** elaboración de diagramas para documentar la arquitectura y el funcionamiento del sistema.
- **Jira:** planificación, organización y seguimiento de tareas del proyecto.
- **Google Meet:** herramienta de comunicación y colaboración durante el desarrollo.
- **SonarQube:** herramienta de análisis estático de código para apoyar la revisión de calidad y seguridad.

## Requisitos del sistema

Para instalar y ejecutar el proyecto localmente, se recomienda contar con los siguientes recursos:

- Sistema operativo Windows, Linux o macOS.
- Python instalado y configurado en el sistema.
- Git para clonar el repositorio.
- pip para instalar las dependencias.
- Un entorno virtual de Python.
- Equipo con recursos suficientes para ejecutar la aplicación y los procesos de visión computacional.

Se recomienda utilizar una versión de Python compatible con las dependencias especificadas en el archivo `requirements.txt`.

## Instalación y ejecución

Sigue los siguientes pasos para descargar, configurar y ejecutar INTELLIGENTLY en un entorno local.

### 1. Clonar el repositorio

Desde una terminal, ingresa al directorio del proyecto:

### 2. Crear un entorno virtual

El entorno virtual permite mantener aisladas las dependencias del proyecto.

En Windows:
python -m venv venv

Activar el entorno virtual:
venv\Scripts\activate

En Linux o macOS:
python3 -m venv venv

Activar el entorno virtual:
source venv/bin/activate

### 3. Instalar las dependencias

Con el entorno virtual activado, instala las bibliotecas necesarias:
python -m pip install --upgrade pip
pip install -r requirements.txt

Este comando instalará las dependencias especificadas en el archivo `requirements.txt`.

### 4. Aplicar las migraciones de la base de datos

Ejecuta las migraciones para preparar la base de datos:
python manage.py migrate

Si se han realizado modificaciones en los modelos de Django que todavía no tienen migraciones, ejecuta primero:
python manage.py makemigrations
python manage.py migrate


### 5. Crear un superusuario

Este paso es opcional y permite acceder al panel administrativo de Django.
python manage.py createsuperuser

Sigue las instrucciones de la terminal para configurar el nombre de usuario, correo electrónico y contraseña.

### 6. Ejecutar el servidor de desarrollo

Inicia el servidor local de Django:

python manage.py runserver

## Módulos del sistema

INTELLIGENTLY se organiza en módulos que permiten separar las principales funcionalidades de la plataforma.

### 1. Gestión de usuarios

Módulo destinado a la administración de cuentas y usuarios, así como a la organización del acceso a las funcionalidades del sistema.

### 2. Control de asistencia

Permite organizar el registro y seguimiento de la asistencia de los estudiantes durante las sesiones educativas.

El sistema contempla el uso de técnicas de reconocimiento para apoyar la automatización de este proceso.

### 3. Visión computacional y aprendizaje automático

Incluye componentes para la captura y procesamiento de imágenes, así como la implementación de modelos de aprendizaje automático.

Estas tecnologías se utilizan para desarrollar funcionalidades relacionadas con la detección y clasificación de información visual.

### 4. Calendario y sesiones educativas

Módulo orientado a la organización de actividades y sesiones educativas mediante funcionalidades de calendario y planificación.

### 5. Videollamadas

Contempla funcionalidades relacionadas con la gestión de sesiones educativas virtuales y el uso de recursos audiovisuales.

### 6. Reportes

Módulo destinado a organizar y presentar información relacionada con la asistencia y las sesiones educativas, facilitando la consulta de datos por parte de los docentes.

## Objetivos específicos

Los objetivos específicos del proyecto son:

- Implementar mecanismos de captura y procesamiento de imágenes de sesiones educativas.
- Aplicar técnicas de visión computacional para apoyar el reconocimiento de estudiantes.
- Desarrollar funcionalidades para facilitar el registro y seguimiento de la asistencia.
- Incorporar modelos de aprendizaje automático para tareas de reconocimiento y clasificación.
- Facilitar la generación de reportes relacionados con las sesiones educativas.
- Proporcionar herramientas que apoyen el seguimiento académico por parte de los docentes.

## Criterios de evaluación

Para evaluar el funcionamiento del sistema se consideran los siguientes aspectos:

- **Precisión de los modelos:** evaluar el desempeño de los algoritmos de detección y reconocimiento mediante pruebas experimentales.
- **Generación de reportes:** comprobar que la información procesada pueda organizarse y presentarse correctamente.
- **Usabilidad:** evaluar la facilidad de uso de la plataforma por parte de los docentes.
- **Rendimiento:** analizar los tiempos de procesamiento y el consumo de recursos computacionales.
- **Funcionamiento general:** verificar la correcta integración de los módulos y las funcionalidades implementadas.

Los porcentajes de precisión y los tiempos de respuesta deberán establecerse a partir de pruebas y resultados obtenidos durante la evaluación del sistema.

## Público objetivo

INTELLIGENTLY está dirigido principalmente a:

- Docentes que requieren herramientas de apoyo para el seguimiento de la asistencia.
- Instituciones educativas que desarrollan actividades virtuales o híbridas.
- Centros educativos interesados en utilizar herramientas tecnológicas para organizar información académica.
- Equipos educativos que necesitan facilitar la generación y consulta de reportes de sesiones.

La plataforma tiene como finalidad apoyar las actividades docentes y complementar los procesos de seguimiento educativo mediante herramientas tecnológicas.

## Privacidad y uso responsable

Debido a que el sistema puede trabajar con imágenes, información educativa y datos biométricos, es importante considerar medidas de privacidad y seguridad durante su implementación.

Se deben contemplar los siguientes aspectos:

- Obtener las autorizaciones y el consentimiento que correspondan para el tratamiento de imágenes y datos personales.
- Proteger la información almacenada y restringir el acceso a usuarios autorizados.
- Evitar la publicación de información personal o datos sensibles en repositorios públicos.
- Utilizar los resultados generados por los modelos de inteligencia artificial de manera responsable.
- Considerar la validación humana antes de utilizar los resultados automatizados en decisiones educativas.

Las estimaciones generadas mediante inteligencia artificial deben interpretarse considerando las limitaciones de los modelos y no deben utilizarse como evaluaciones definitivas del comportamiento, la atención o el desempeño de los estudiantes.

## Recursos tecnológicos utilizados

Para el desarrollo y las pruebas del proyecto se consideran los siguientes recursos:

- Computadoras personales con capacidad de procesamiento moderada.
- Cámaras estándar para la captura de imágenes y grabación de sesiones educativas.
- Herramientas de desarrollo de software y procesamiento de datos.
- Recursos de almacenamiento y procesamiento para los componentes del sistema.

Los recursos específicos pueden variar según el entorno de ejecución y las necesidades de cada funcionalidad.

## Estado del proyecto

Proyecto académico desarrollado como parte de la formación en Ingeniería de Software.
Las funcionalidades disponibles dependen de la versión actual del código fuente y de los componentes implementados.

## Licencia

Este proyecto es de carácter académico.
Los términos de uso, distribución y reutilización del código deberán establecerse mediante una licencia incluida en el repositorio.

**Desarrollado por Anthony Hernández**  
Estudiante de Ingeniería de Software  
Universidad Estatal de Milagro (UNEMI).