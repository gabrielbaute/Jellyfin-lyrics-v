# lyrics_fetcher/log_config.py
import logging
from pathlib import Path
from typing import Optional, List
from rich.console import Console
from rich.text import Text
from rich.theme import Theme

class ColorfulCircularHandler(logging.Handler):
    """Muestra solo los últimos 15 mensajes con colores por nivel."""
    def __init__(self, capacity: int = 15):
        super().__init__()
        self.capacity = capacity
        self.buffer: List[Text] = []
        self.console = Console(theme=Theme({
            "info": "dim cyan",
            "warning": "bold yellow",
            "error": "bold red",
            "success": "bold green"
        }))

    def emit(self, record):
        # Acortamos el mensaje a 50 caracteres y añadimos iconos
        msg = self.format(record)
        short_msg = (msg[:47] + '...') if len(msg) > 50 else msg
        
        # Color por nivel
        if record.levelno == logging.INFO:
            if "✓" in msg:
                text = Text(f"✓ {short_msg}", style="success")
            else:
                text = Text(f"ℹ {short_msg}", style="info")
        elif record.levelno == logging.WARNING:
            text = Text(f"⚠ {short_msg}", style="warning")
        elif record.levelno == logging.ERROR:
            text = Text(f"✗ {short_msg}", style="error")
        
        self.buffer.append(text)
        if len(self.buffer) > self.capacity:
            self.buffer.pop(0)
        self._refresh_console()

    def _refresh_console(self):
        self.console.clear()
        for text in self.buffer:
            self.console.print(text)

def setup_logging(log_dir: Optional[str] = None, log_level: int = logging.INFO):
    """Configura logging con colores y mensajes acortados."""
    log_dir = log_dir or "logs"
    Path(log_dir).mkdir(exist_ok=True)
    
    log_file = Path(log_dir) / "lyrics_fetcher.log"
    
    # Formato simplificado para archivo
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    # Handler colorido para consola
    console_handler = ColorfulCircularHandler(capacity=15)
    console_handler.setFormatter(logging.Formatter("%(message)s"))

    logging.basicConfig(
        level=log_level,
        handlers=[file_handler, console_handler],
    )