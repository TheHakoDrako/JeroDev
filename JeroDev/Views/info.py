import reflex as rx

from JeroDev.Components.heading import heading
from JeroDev.Components.info_detail import info_detail
from JeroDev.Styles.styles import Size

def info(tittle: str) -> rx.Component:
    return rx.vstack(
        heading(tittle),
        info_detail(),
        spacing=Size.DEFAULT.value,
        width="100%"
    )