import reflex as rx

from jerodev.components.heading import heading
from jerodev.components.info_detail import info_detail
from jerodev.data import Info
from jerodev.styles.styles import Size


def info(title: str, info: list[Info]) -> rx.Component:
    return rx.section(
        rx.vstack(
            heading(title),
            rx.vstack(
                *[
                    info_detail(item)
                    for item in info
                ],
                spacing=Size.DEFAULT.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        padding_top="15px",
        padding_bottom="30px"
    )
        
