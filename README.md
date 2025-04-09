# 🎶 Jellyfin Lyrics Fetcher (Fork Mejorado)

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Este repositorio nació como un fork del proyecto original de [Jellyfin-lyrics](https://github.com/sai80082/Jellyfin-lyrics). En su momento lo requería para poder incorporar archivos .lrc a mi biblioteca de música de Jellyfin (en aquel momento aún no incorporaban la búsqueda automática). A pesar de que Jellyfin ya cuenta con la función de obtener lyrics sincronizadas, sigo empleando este repositorio y, con el tiempo, lo he ido mejorando. Algunas de las mejoras son:
- **Interfaz CLI enriquecida** (Rich + Click)
- **Búsqueda inteligente** de letras (LRCLib)
- **Logging avanzado** con salida colorida

## 📜 Créditos y Origen
Este proyecto es un fork de:
```text
https://github.com/sai80082/Jellyfin-lyrics.git
```
Gracias por haber creado ese script, de verdad me ayudó mucho!

**Mejoras implementadas en este fork**:
- Refactorización completa del código (POO + type hints)
- Sistema de logging circular con colores (últimos 15 mensajes)
- Panel de estadísticas interactivo (Rich)

## 🚀 Instalación
```bash
pip install git+https://github.com/gabrielbaute/Jellyfin-lyrics-v
```
*O con Poetry:*
```bash
poetry add lyrics-fetcher
```
También puedes ejecutar:
```bash
pip install -e .
```

## 💻 Uso Básico
```bash
lfetcher fetch "ruta/a/tu/música" --verbose
```
**Opciones**:
- `--timeout`: Establece timeout para peticiones API (default: 10s)
- `--verbose`: Muestra detalles del procesamiento

## 📊 Estadísticas de Salida
```text
╭──────────────────────────────╮
│       Lyrics Fetcher Stats   │
│                              │
│  Total processed: 42         │
│  Lyrics found: 38 (90.5%)    │
│  Lyrics missing: 4           │
╰──────────────────────────────╯
```


## 🤝 Contribuir
1. Siéntete libre de hacer tu propio fork del proyecto
2. Crea tu rama (`git checkout -b feature/nueva-funcion`)
3. Commit (`git commit -m 'Añade x función'`)
4. Push (`git push origin feature/nueva-funcion`)
5. Abre un Pull Request

## 📄 Licencia
MIT © [Gabriel Baute](LICENSE) - Basado en el trabajo de [sai80082](https://github.com/sai80082)