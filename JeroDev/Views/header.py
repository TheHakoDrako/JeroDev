import reflex as rx

from JeroDev.Components.heading import heading
from JeroDev.Styles.styles import Size
from JeroDev.Components.media import media
from JeroDev.data import Data

def header(data: Data) -> rx.Component:
    return rx.section(
        rx.hstack(
            rx.avatar(
                src=data.avatar,
                size=Size.BIG.value,
                border_radius="full",
            ),
            rx.vstack(
                heading(data.name, True),
                heading(data.skill),
                rx.text(
                    rx.icon("map-pin"),
                    data.location,
                    display="inherit"
                ),
                media(data.media),
                spacing=Size.SMALL.value
            ),
            spacing=Size.DEFAULT.value,
        ),
        padding_top="10px",
        padding_bottom="30px"
    )
    