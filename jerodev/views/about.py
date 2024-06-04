import reflex as rx

from jerodev.components.heading import heading


def about(description: str) -> rx.Component:
    return rx.section(
        rx.vstack(
            heading("Sobre mí"),
            rx.box(
                rx.text(
                    description,
                    white_space="pre-wrap"
                ),
                padding="20px",
                borderRadius="10px",
                backgroundColor="var(--background-secondary)",
                textAlign= "justify"
            )
        ),
        paddingTop="28px",
        paddingBottom="32px",
        id="sobre-mi"
    )
