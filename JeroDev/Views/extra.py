import reflex as rx

from JeroDev.Components.heading import heading
from JeroDev.Components.card_detail import card_detail
from JeroDev.Styles.styles import Size

def extra() -> rx.Component:
    return rx.vstack(
        heading("Extra"),
        rx.hstack(
            *[
                card_detail()
                for _ in range(0, 3)
            ],
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )