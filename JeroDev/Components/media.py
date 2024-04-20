import reflex as rx

from JeroDev.Components.icon_button import icon_button
from JeroDev.Styles.styles import Size

def media() -> rx.Component:
    return rx.hstack(
        icon_button(
            "mail",
            "url",
            "Email@gmail.com",
            True
        ),
        icon_button(
            "github",
            "url",
            "Github",
        ),
        icon_button(
            "linkedin",
            "url",
            "LinkedIn",
        ),
        icon_button(
            "file-text",
            "url",
            "Cv",
        ),
        spacing=Size.SMALL.value
    )