import reflex as rx

from jerodev.components.icon_button import icon_button
from jerodev.data import Media
from jerodev.styles.styles import Size


def media(data: Media) -> rx.Component:
    return rx.flex(
        icon_button(
            "mail",
            f"mailto:{data.email}",
            data.email,
            True
        ),
        rx.hstack(
            icon_button(
                "file-text",
                data.cv
            ),
            icon_button(
                "github",
                data.github
            ),
            icon_button(
                "linkedin",
                data.likedin
            ),
            spacing=Size.SMALL.value
        ),
        spacing=Size.SMALL.value,
        flex_direction=["column", "column", "row"]
    )