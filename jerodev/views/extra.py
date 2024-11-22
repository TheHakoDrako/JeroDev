import reflex as rx

from jerodev.components.card_detail import card_detail
from jerodev.components.heading import heading
from jerodev.data import Extra
from jerodev.styles.styles import Size

def extra(extras: list[Extra]) -> rx.Component:
    return rx.section(
        rx.vstack(
            heading("Extra"),
            rx.text("Aquí puedes encontrar algunos de los proyectos y actividades que realizo en mi tiempo libre. Al darle click te llevará a una página relacionada con el tema, en el cual aporte código o texto."),
            rx.mobile_only(
                rx.vstack(
                    *[
                        card_detail(extra)
                        for extra in extras
                    ],
                    spacing=Size.DEFAULT.value
                ),
                width="100%"
            ),
            rx.tablet_and_desktop(
                rx.grid(
                    *[
                        card_detail(extra)
                        for extra in extras
                    ],
                    spacing=Size.DEFAULT.value,
                    columns="3"
                ),
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        id="extra"
    )
