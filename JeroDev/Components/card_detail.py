import reflex as rx

from JeroDev.Styles.styles import EmSize, Size
from JeroDev.Styles.styles import IMAGE_HEIGHT

def card_detail() -> rx.Component:
    return rx.card(
        rx.inset(
            rx.image(
                src="favicon.ico",
                height=IMAGE_HEIGHT,
                width="100%",
                border_radius=EmSize.DEFAULT.value
            ),
            pb=Size.DEFAULT.value
        ),
        rx.text(
            "Description of the project.",
            Size=Size.SMALL.value,
            color_scheme="gray"
        ),
        width="100%"
    )