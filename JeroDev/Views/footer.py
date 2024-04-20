import reflex as rx

from JeroDev.Components.media import media
from JeroDev.Styles.styles import Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.text("© 2021 JeroDev"),
        media(),
        spacing=Size.SMALL.value
    )