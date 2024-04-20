import reflex as rx

from JeroDev.Views.header import header
from JeroDev.Views.about import about
from JeroDev.Views.tech_stack import tech_stack
from JeroDev.Views.info import info
from JeroDev.Views.extra import extra
from JeroDev.Views.footer import footer
from JeroDev.Styles.styles import MAX_WIDTH, EmSize, Size

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            header(),
            about(),
            rx.divider(),
            tech_stack(),
            info("Experiencia"),
            info("Proyectos"),
            info("Formacion"),
            extra(),
            rx.divider(),
            footer(),    
            spacing=Size.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"
        )
    )

app = rx.App()
app.add_page(index)
