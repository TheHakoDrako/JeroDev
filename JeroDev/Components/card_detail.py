import reflex as rx

from JeroDev.Styles.styles import IMAGE_HEIGHT, Size
from JeroDev.data import Extra

def card_detail(extra: Extra) -> rx.Component:
    return rx.card(
        rx.inset(
            rx.image(
                src=extra.image,
                height=IMAGE_HEIGHT,
                width="100%",
                object_fit="cover"
            ),
            pb=Size.DEFAULT.value
        ),
        rx.text.strong(extra.title),
        rx.text(
            extra.description,
            size=Size.SMALL.value,
            color_scheme="gray"
        ),
        width="100%",
        on_click=rx.redirect(extra.url, True)
    )