import reflex as rx

from JeroDev.Styles.styles import Size

def icon_button(icon: str, url: str, text="", solid=False) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon),
            text,
            variant="solid" if solid else "surface",
        ),
        href=url,
        is_external=True
    )