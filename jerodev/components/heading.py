import reflex as rx

from jerodev.styles.styles import Size


def heading(text: str, h1=False, center=False) -> rx.Component:
    align = "center" if center else "left"  
    return rx.flex(
        rx.heading(
            text,
            as_="h1" if h1 else "h2",
            size=Size.BIG.value if h1 else Size.MEDIUM.value,
            align=align
        ),
        direction="column",
        width="100%"
    )

