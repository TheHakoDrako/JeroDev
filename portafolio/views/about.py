import reflex as rx

from jerodev.components.heading import heading


def about(description: str) -> rx.Component:
    return rx.vstack(
        heading("Sobre mí"),
        rx.text(description)
    )
