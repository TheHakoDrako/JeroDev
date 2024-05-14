import reflex as rx

from jerodev.data import Extra
from jerodev.styles.styles import IMAGE_HEIGHT, Size


def card_detail(extra: Extra) -> rx.Component:
    return rx.card(
        rx.link(
            rx.inset(
                rx.image(
                    src=extra.image,
                    height=IMAGE_HEIGHT,
                    width="auto",
                    margin="auto",
                    padding="14px",
                    opacity="0.4",
                    _hover={
                        "opacity": 1,  # Cambia la opacidad cuando el mouse esté por encima
                    },
                ),
                pb=Size.DEFAULT.value
            ),
            rx.text.strong(extra.title),
            rx.text(
                extra.description,
                size=Size.SMALL.value,
                color_scheme="gray"
            ),
            href=extra.url,
            is_external=True
        ),
        background="radial-gradient(black, transparent)",
        padding="8px",
        width="100%"
    )
