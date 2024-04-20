import reflex as rx

from JeroDev.Components.heading import heading
from JeroDev.Styles.styles import Size
from JeroDev.Components.media import media

def header() -> rx.Component:
    return rx.hstack(
        rx.avatar(size=Size.BIG.value, src="https://avatars.githubusercontent.com/u/72213815?v=4"),
        rx.vstack(
            heading("Nombre", h1=True),
            heading("Habilidad principal"),
            rx.text(
                rx.icon("map-pin"),
                "Localización",
                display="inherit"
            ),
            media(),
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value,
    )