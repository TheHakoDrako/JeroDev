import reflex as rx

from jerodev.components.media import media
from jerodev.components.float_button import float_button
from jerodev.data import Media
from jerodev.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.link(
            "@2024 Jero Rm", 
            href="https://www.instagram.com/jero.rm/", 
            is_external=True
        ),
        float_button(
            icon=rx.image(src="/coffee.svg", alt="Buy me a coffee"),
            href="https://buymeacoffee.com/jerorm"
        ),
        media(data),
        spacing=Size.DEFAULT.value,
        align="center",
        width="100%"
    )
