import reflex as rx

from jerodev.components.heading import heading
from jerodev.data import Technology
from jerodev.styles.styles import EmSize, Size


def tech_stack(technologies: list[Technology]) -> rx.Component:
    return rx.section(
        rx.vstack(
            heading("Tecnologías"),
            rx.flex(
                *[
                    rx.badge(
                        rx.box(
                            class_name=technology.icon,
                            font_size="24px"
                        ),
                        rx.text(technology.name),
                        size="2"
                    )
                    for technology in technologies
                ],
                wrap="wrap",
                spacing=Size.SMALL.value
            ),
            spacing=Size.MEDIUM.value
        ),
        paddingTop="12px",
        paddingBottom="32px"
    )
        
