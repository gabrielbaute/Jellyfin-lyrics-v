# lyrics_fetcher/cli.py
import click
import logging
from rich import print as rprint
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from pathlib import Path
from typing import Optional
from .core.lrclib_fetcher import LRCLibClient
from .core.utils import collect_audio_files, get_song_details
from .log_config import setup_logging

@click.group()
def cli():
    """Fetch synced lyrics for your audio files using LRCLib."""
    setup_logging()  # Configura logging al iniciar

@cli.command()
@click.argument("directory_path", type=click.Path(exists=True, path_type=Path))
@click.option("--timeout", default=10, help="Timeout for API requests in seconds.")
@click.option("--verbose", is_flag=True, help="Show detailed processing info.")
def fetch(directory_path: Path, timeout: int, verbose: bool):
    """
    Fetch lyrics for all audio files in a directory.
    """
    setup_logging() 

    client = LRCLibClient(timeout=timeout)
    audio_files = collect_audio_files(str(directory_path))
    total_files = len(audio_files)
    found, missing = 0, 0
    try:
        with Progress(
            TextColumn("[bold blue]{task.description}"),
            BarColumn(bar_width=None),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            transient=True,  # La barra desaparece al terminar
        ) as progress:
            task = progress.add_task("[cyan]Processing songs...", total=total_files)

            for file_path in audio_files:
                album, title, artist, duration = get_song_details(file_path)
                if None in (album, title, artist, duration):
                    logging.warning(f"Skipping {file_path}: Invalid metadata.")
                    missing += 1
                    progress.update(task, advance=1)
                    continue

                lyrics = client.get_lyrics(artist, title, album, duration)
                if lyrics:
                    lrc_path = Path(file_path).with_suffix(".lrc")
                    lrc_path.write_text(lyrics, encoding="utf-8")
                    found += 1
                    if verbose:
                        logging.info(f"✓ Lyrics saved for {title[:30]} (Album: {album[:20]}...)...")
                else:
                    logging.warning(f"✗ Lyrics not found for {title[:30]}...")
                    missing += 1

                progress.update(task, advance=1)

        # Mostrar estadísticas al final
        success_rate = (found / total_files) * 100 if total_files > 0 else 0
        stats = (
            f"[bold]Total processed:[/bold] {total_files}\n"
            f"[bold green]Lyrics found:[/bold green] {found}\n"
            f"[bold red]Lyrics missing:[/bold red] {missing}\n"
            f"[bold cyan]Success rate:[/bold cyan] {success_rate:.2f}%"
        )

        rprint(
            Panel.fit(
                stats,
                title="[bold magenta]Lyrics Fetcher Stats[/bold magenta]",
                subtitle=f"[italic]Directory: {directory_path}[/italic]",
                border_style="blue",
                padding=(1, 4),
            )
        )
    except Exception as e:
        logging.error(f"API Error: {str(e)[:50]}")
        #rprint(f"[red]Error:[/red] {e}")

if __name__ == "__main__":
    cli()