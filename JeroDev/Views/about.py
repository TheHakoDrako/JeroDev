import reflex as rx

from JeroDev.Components.heading import heading

def about(description: str) -> rx.Component:
    return rx.vstack(
        heading("Sobre mi:", h1=True),
        rx.text(description, as_="div")
    )