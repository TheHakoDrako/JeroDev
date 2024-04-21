import reflex as rx

from JeroDev import data
from JeroDev.Styles.styles import MAX_WIDTH, EmSize, Size, BASE_STYLE, STYLES_SHEET
from JeroDev.Views.header import header
from JeroDev.Views.about import about
from JeroDev.Views.tech_stack import tech_stack
from JeroDev.Views.info import info
from JeroDev.Views.extra import extra
from JeroDev.Views.footer import footer

DATA = data.data

def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            header(DATA),
            about(DATA.about),
            rx.divider(),
            tech_stack(DATA.technologies),
            info("Experiencia", DATA.experience),
            info("Proyectos", DATA.projects),
            info("Formacion", DATA.training),
            extra(DATA.extras),
            rx.divider(),
            footer(DATA.media),    
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"
        )
    )


app = rx.App(
    stylesheets=STYLES_SHEET,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        radius="large"
    )
)


title = DATA.title
description = DATA.description
image = DATA.image


app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {
            "name": "og:title",
            "content": title
        },
        {
            "name": "og:description",
            "content": description
        },
        {
            "name": "og:image",
            "content": image
        }
    ]
)
