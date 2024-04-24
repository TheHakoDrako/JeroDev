import reflex as rx

from JeroDev.Components.media import media
from JeroDev.Styles.styles import Size
from JeroDev.data import Media

def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.text("© 2021 JeroDev"),
        media(data),
        spacing=Size.SMALL.value,
        align="center",
        width="100%"
    )