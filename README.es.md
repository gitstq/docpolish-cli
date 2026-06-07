# 🎉 DocPolish-CLI

🦞 Lightweight Markdown Document Intelligent Beautification Engine | 轻量级Markdown文档智能美化引擎

## ✨ Características Principales

- ✨ Smart Markdown formatting
- ✨ Document structure analysis
- ✨ AI content polishing
- ✨ Multi-language README generation
- ✨ Zero-dependency core
- 🚀 **Cero Dependencias** - Implementación pura en Python, sin dependencias adicionales
- 🎨 **Formateo Inteligente** - Corrige automáticamente problemas de formato Markdown
- 🤖 **Mejora con IA** - Integrado con GLM-5.1 para pulir contenido y traducir
- 🌍 **Soporte Multiidioma** - Generación de README en múltiples idiomas con un clic
- 📊 **Análisis de Documentos** - Análisis profundo de estructura y calidad del documento

## 🚀 Inicio Rápido

### Requisitos

- Python 3.8+
- pip

### Instalación

```bash
pip install docpolish
```

### Uso Básico

```bash
# Formatear un documento Markdown
docpolish format README.md

# Analizar estructura del documento
docpolish analyze document.md

# Pulir contenido con IA
docpolish polish README.md --style professional

# Generar README multiidioma
docpolish readme --project-name "MyProject" --lang es,en
```

## 📖 Guía de Uso Detallada

### Comando de Formateo

```bash
# Formatear y sobrescribir archivo original
docpolish format README.md

# Formatear y guardar en nuevo archivo
docpolish format README.md -o README_formatted.md

# Solo verificar, no modificar
docpolish format README.md --check

# Mostrar diferencias de cambios
docpolish format README.md --diff
```

### Comando de Análisis

```bash
# Análisis en formato texto
docpolish analyze document.md

# Salida en formato JSON
docpolish analyze document.md --json
```

### Pulido con IA

```bash
# Estilo profesional
docpolish polish README.md --style professional

# Estilo simple
docpolish polish README.md --style simple

# Especificar clave API
docpolish polish README.md --api-key YOUR_API_KEY
```

### Traducción

```bash
# Traducir al español
docpolish translate README.md --target es

# Traducir al inglés
docpolish translate README.md --target en
```

## 💡 Filosofía de Diseño y Hoja de Ruta

### Filosofía de Diseño

DocPolish está diseñado para resolver las inconsistencias de formato, el desorden de diseño y las dificultades de mantenimiento multilingüe que enfrentan los desarrolladores al escribir y mantener documentos Markdown. A través de la corrección inteligente de formato y las funciones de mejora con IA, la escritura de documentos se vuelve eficiente.

### Elecciones Técnicas

- **Implementación Pura en Python**: Núcleo sin dependencias garantiza compatibilidad multiplataforma
- **Motor de Expresiones Regulares**: Análisis y formateo de texto eficiente
- **Integración GLM-5.1**: Potentes capacidades de comprensión y generación en chino
- **Arquitectura Modular**: Fácil de extender y mantener

### Hoja de Ruta

- [ ] v1.1.0 - Soporte para más sintaxis de extensión Markdown (GFM, CommonMark)
- [ ] v1.2.0 - Agregar función de vista previa en tiempo real
- [ ] v1.3.0 - Soporte para reglas de formato personalizadas
- [ ] v2.0.0 - Interfaz Web UI

## 📦 Guía de Empaquetado y Despliegue

### Instalar desde el Código Fuente

```bash
git clone https://github.com/gitstq/docpolish-cli.git
cd docpolish-cli
pip install -e .
```

### Construir Paquete de Lanzamiento

```bash
python -m build
```

### Instalar Paquete Local

```bash
pip install dist/docpolish-1.0.0-py3-none-any.whl
```

## 🤝 Guía de Contribución

¡Issues y Pull Requests son bienvenidos!

### Convención de Commits

- `feat:` Nueva característica
- `fix:` Corrección de errores
- `docs:` Actualización de documentación
- `refactor:` Refactorización de código

### Flujo de Desarrollo

1. Hacer Fork de este repositorio
2. Crear una rama de características (`git checkout -b feat/amazing-feature`)
3. Confirmar tus cambios (`git commit -m 'feat: add amazing feature'`)
4. Subir a la rama (`git push origin feat/amazing-feature`)
5. Crear un Pull Request

## 📄 Licencia

Este proyecto está licenciado bajo la [MIT](LICENSE).

---

<p align="center">Made with ❤️ by Lobster AI</p>
