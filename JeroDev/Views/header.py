import reflex as rx

from JeroDev.Components.heading import heading
from JeroDev.Styles.styles import Size
from JeroDev.Components.media import media
from JeroDev.data import Data

def header(data: Data) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src=data.avatar,
            size=Size.BIG.value
        ),
        rx.vstack(
            heading(data.name, True),
            heading(data.title),
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display="inherit"
            ),
            media(data.media),
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value,
    )