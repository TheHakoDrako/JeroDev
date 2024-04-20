import reflex as rx

from JeroDev.Components.heading import heading

def about() -> rx.Component:
    return rx.vstack(
        heading("About JeroDev", h1=True),
        rx.text(
            "JeroDev is a software developer who loves to create and share projects. "
        )
    )