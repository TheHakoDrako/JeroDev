import reflex as rx

from jerodev.components.heading import heading
from jerodev.components.media import media
from jerodev.data import Data
from jerodev.styles.styles import Size


def header(data: Data) -> rx.Component:
    return  rx.section(
        rx.center(
            rx.vstack(
                heading(data.name, True, center=True),
                rx.avatar(
                    src=data.avatar,
                    size=Size.BIG.value
                ),
                heading(data.skill, center=True),
                rx.text(
                    rx.icon("map-pin"),
                    data.location,
                    display="inherit"
                ),
                media(data.media),
                spacing=Size.SMALL.value,
                align="center",
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            direction="column",
            align="center",
            width="100%"
        ),
        padding_top="15px",
        padding_bottom="20px",
        width="100%"
    )

