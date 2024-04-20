import reflex as rx

from JeroDev.Components.heading import heading
from JeroDev.Styles.styles import Size

def tech_stack() -> rx.Component:
    return rx.vstack(
        heading("Tecnologias"),
        rx.flex(
            *[
                rx.badge(
                rx.icon("code"),
                rx.text(f"Stack {index}"),
                size="1"
                )
                for index in range(0, 6)
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )