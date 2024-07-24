import reflex as rx

from jerodev.components.heading import heading
from jerodev.styles.styles import Size

def about(description: str) -> rx.Component:
    return rx.section(
        rx.vstack(
            heading("Sobre mí"),
            rx.text(
                description,
                white_space="pre-wrap",
                paddingTop="16px",
            ),
            backgroundColor="var(--background-secondary)",
            textAlign= "justify"
        ),
        spacing=Size.MEDIUM.value,
        paddingTop="32px",
        paddingBottom="38px",
        id="sobre-mi"
    )
