import reflex as rx

from JeroDev.data import Info
from JeroDev.Components.heading import heading
from JeroDev.Components.info_detail import info_detail
from JeroDev.Styles.styles import Size

def info(tittle: str, info: list[Info]) -> rx.Component:
    return rx.section(
        rx.vstack(
            heading(tittle),
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
        padding_top="35px",
        padding_bottom="40px"
    )