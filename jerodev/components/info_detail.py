import reflex as rx

from jerodev.components.icon_badge import icon_badge
from jerodev.components.icon_button import icon_button
from jerodev.data import Info
from jerodev.styles.styles import IMAGE_HEIGHT, EmSize, Size


def info_detail(info: Info) -> rx.Component:
    return rx.flex(
        rx.hstack(
            icon_badge(info.icon),
            rx.vstack(
                rx.text.strong(info.title),
                rx.text.kbd(info.subtitle, size="3"),
                rx.text(
                    info.description,
                    size=Size.SMALL.value,
                    color_scheme="gray",
                    textAlign= "justify"
                ),
                rx.cond(
                    info.technologies,
                    rx.flex(
                        *[
                            rx.badge(
                                rx.box(class_name=technology.icon),
                                technology.name,
                                color_scheme="gray"
                            )
                            for technology in info.technologies
                        ],
                        wrap="wrap",
                        spacing=Size.SMALL.value
                    )
                ),
                rx.hstack(
                    rx.cond(
                        info.url != "",
                        icon_button(
                            "link",
                            info.url,
                            "Web"
                        )
                    ),
                    rx.cond(
                        info.github != "",
                        icon_button(
                            "github",
                            info.github,
                            "Github"
                        )
                    )
                ),
                spacing=Size.SMALL.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        rx.cond(
            info.image != "",
            rx.card(
                rx.image(
                    src=info.image,
                    height="auto",
                    width="auto",
                    margin="auto",
                    padding="2px",
                    borderRadius="18px",
                    opacity="0.4",
                    _hover={
                        "opacity": 1,  # Cambia la opacidad cuando el mouse esté por encima
                    },
                ),
                style={"--card-padding": "var(--space-1)"},
                background="radial-gradient(black, transparent)",
                width="100%"
            )
        ),
        rx.vstack(
            rx.cond(
                info.date != "",
                rx.badge(info.date)
            ),
            rx.cond(
                info.certificate != "",
                icon_button(
                    "shield-check",
                    info.certificate,
                    "Certificado",
                    solid=True
                )
            ),
            spacing=Size.SMALL.value,
            align="end"
        ),
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        width="100%"
    )
