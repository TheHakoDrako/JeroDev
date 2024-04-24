import reflex as rx

from jerodev.components.media import media
from jerodev.data import Media
from jerodev.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.text("Nombre"),
        media(data),
        spacing=Size.SMALL.value
    )
