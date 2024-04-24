import reflex as rx

from JeroDev.Components.heading import heading
from JeroDev.Styles.styles import Size, EmSize
from JeroDev.data import Technology

def tech_stack(technologies: list[Technology]) -> rx.Component:
    return rx.vstack(
        rx.section(
            heading("Tecnologias"),
            rx.flex(
                padding_top="15px",
                *[
                    rx.badge(
                        rx.center(
                            rx.box(
                                class_name=technology.icon,
                                font_size="22px",
                                margin="1px",
                                padding="1px"
                                ),
                            ),
                        rx.text(technology.name),
                        size="1",
                        box_shadow="shadow"
                    )
                    for technology in technologies
                ],
                wrap="wrap",
                spacing=Size.SMALL.value
            ),
            spacing=Size.DEFAULT.value,
            padding_top="10px",
            padding_bottom="15px"
        )
    )