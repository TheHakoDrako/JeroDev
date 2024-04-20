import reflex as rx

from JeroDev.Components.heading import heading
from JeroDev.Styles.styles import Size, EmSize
from JeroDev.data import Technology

def tech_stack(technologies: list[Technology]) -> rx.Component:
    return rx.vstack(
        heading("Tecnologias"),
        rx.flex(
            *[
                rx.badge(
                rx.box(
                    class_name=technology.icon,
                    font_size="24px"
                    ),
                rx.text(technology.name),
                size="1"
                )
                for technology in technologies
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )