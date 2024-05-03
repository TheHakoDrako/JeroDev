import reflex as rx
from jerodev.components.card_quote import QuoteState
from jerodev.styles.styles import Size

def quote():
    return rx.section(
        rx.center(
            rx.vstack(
                rx.blockquote(
                    rx.vstack(
                        rx.text(f"“{QuoteState.current_quote}”"),
                        rx.badge(f"Author: {QuoteState.current_author}", margin="10px"),
                        align="end",
                        justify="center",
                        width="100%"
                    ),
                    high_contrast=True,
                    padding="5px 5px 5px 10px"
                ),
                rx.vstack(
                    rx.button(
                        "Citas aleatorias",
                        rx.icon("mouse-pointer-click"),
                        on_click=QuoteState.change_quote,
                        margin="0px 10px 30px 10px",
                        color_scheme="gray"
                    ),
                    align="center",
                    width="100%"
                ),
                align="center",
                justify="center"
            ),
            spacing=Size.DEFAULT.value,
            direction="column",
            align="center",
            justify="center",
            margin="10px"
        ),
        padding_top="60px",
        padding_bottom="42px",
        margin= "8px",
        width="100%"
    )