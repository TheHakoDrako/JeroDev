import reflex as rx

from JeroDev.Components.icon_badge import icon_badge
from JeroDev.Styles.styles import EmSize, Size, IMAGE_HEIGHT
from JeroDev.Components.icon_button import icon_button

def info_detail() -> rx.Component:
    return rx.hstack(
        icon_badge("box-select"),
        rx.vstack(
            rx.text.strong("Tittle:"),
            rx.text("Subtittle:"),
            rx.text(
                "Description:",
                size=Size.SMALL.value,
                color_scheme="gray"
                ),
            rx.flex(
                    *[
                        rx.badge(
                            f"Badge {index}",
                            color_scheme="gray"
                        )
                        for index in range(0, 6)
                    ],
                    wrap="wrap",
                    spacing=Size.SMALL.value,
                ),
            rx.hstack(
                icon_button(
                    "link",
                    "url"
                ),
                icon_button(
                    "github",
                    "url"
                )
            ),
            spacing=Size.SMALL.value,
            width="100%"
        ),
        rx.hstack(
            rx.image(
                src="/favicon.ico",
                height=IMAGE_HEIGHT,
                width="auto",
                border_radius=EmSize.DEFAULT.value
            ),
            rx.vstack(
                rx.badge("Años"),
                icon_button(
                    "shield-check",
                    "url",
                    solid=True
                ),
                spacing=Size.SMALL.value,
                align="end"
            ),
            spacing=Size.DEFAULT.value
        ),
        width="100%"
    )