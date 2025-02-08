import reflex as rx
from jerodev.styles.styles import NAVBAR, NAVBAR_LINK

# Datos de navegación de la página
nav_data = [
    {"title": "Inicio", "label": "sobre-mi", "url": "/#sobre-mi"},
    {"title": "Experiencia", "label": "experiencia", "url": "/#experiencia"},
    {"title": "Proyectos", "label": "proyectos", "url": "/#proyectos"},
    {"title": "Formación", "label": "formación", "url": "/#formación"},
    {"title": "Extra", "label": "extra", "url": "/#extra"},
]

# Barra de navegación de la página
def nav_bar() -> rx.Component:
    links = [
        rx.link(
            item["title"], 
            href=item["url"],
            style=NAVBAR_LINK,
            color_scheme="sky",      
            high_contrast=True,
            underline="none"
        ) for item in nav_data
    ]
    
    return rx.center(
        rx.section(
            rx.hstack(
                *links
            ),
            id="nav_bar",
            style=NAVBAR
        )
    )