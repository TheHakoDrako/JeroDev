import reflex as rx

from jerodev.components.heading import heading
from jerodev.data import Technology
from jerodev.styles.styles import EmSize, Size

def tech_stack(technologies: list[Technology]) -> rx.Component:
    return rx.section(
        rx.grid(
            heading("Tecnologías"),
            rx.badge(
                rx.flex(
                    *[
                        rx.badge(
                            rx.box(
                                class_name=technology.icon,
                                font_size="24px"
                            ),
                            rx.text(technology.name),
                            size="3",
                            margin="4px",
                            variant="soft",
                            high_contrast=True
                        )
                        for technology in technologies
                    ],
                    wrap="wrap",
                    justify="center",
                    align="center",
                    width="100%"
                ),
                size="2",
                variant="soft",
                borderRadius="14px"
            ),
            spacing="3"
        ),
        paddingTop="12px",
        paddingBottom="32px"
    )   
