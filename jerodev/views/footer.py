import reflex as rx
import jerodev.constans as const

from jerodev.components.media import media
from jerodev.components.float_button import float_button
from jerodev.data import Media
from jerodev.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.link(
            "@2025 Jero Rm", 
            href=f"{const.INSTAGRAM_URL}", 
            is_external=True
        ),
        float_button(
            icon=rx.image(src="/coffee.svg", alt="Buy me a coffee", title="Buy me a coffee"),
            href=f"{const.BUY_ME_A_COFFEE}",
            is_external=True
        ),
        media(data),
        spacing=Size.DEFAULT.value,
        align="center",
        width="100%"
    )
