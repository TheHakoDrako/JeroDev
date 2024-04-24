import reflex as rx

from jerodev.components.media import media
from jerodev.data import Media
from jerodev.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.link("@2024 Jero Rm", href="https://www.instagram.com/jero.rm/", is_external=True),
        media(data),
        spacing=Size.SMALL.value,
        align="center",
        width="100%"
    )
