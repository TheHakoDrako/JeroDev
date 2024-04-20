import reflex as rx

from JeroDev.Components.icon_button import icon_button
from JeroDev.Styles.styles import Size
from JeroDev.data import Media

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
                "github",
                data.github
            ),
            icon_button(
                "linkedin",
                data.linkedin
            ),
            icon_button(
                "file-text",
                data.cv
            ),
            spacing=Size.SMALL.value
        ),
        spacing=Size.SMALL.value,
        flex_direction=["column", "column", "row"]
    )