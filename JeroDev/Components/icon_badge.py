import reflex as rx

from JeroDev.Styles.styles import Size

def icon_badge(icon: str) -> rx.Component:
    return rx.badge(
        rx.icon(
            icon,
            size=32
        ),
        aspect_ratio = "1",
        variant="soft"
    )