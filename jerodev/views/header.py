import reflex as rx
from reflex_type_animation import type_animation

from jerodev.components.heading import heading
from jerodev.components.media import media
from jerodev.data import Data
from jerodev.styles.styles import Size


def header(data: Data) -> rx.Component:
    return  rx.section(
        rx.center(
            rx.vstack(
                heading(data.name, True, center=True),
                rx.image(
                    src=data.avatar,
                    height="264px",
                    borderRadius="100px",
                    margin="12px",
                    title="Jero Rm"
                ),
                type_animation(
                    sequence=[data.skill,1000],
                    speed=1,
                    font_size=["24px"],
                    text_align="center",
                    align="center",
                    color="#9ab2ff",
                    high_contrast=True,
                    font_weight= "var(--font-weight-regular)",
                    line_height="1",
                ),
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
        padding_top="22px",
        padding_bottom="32px",
        width="100%"
    )

