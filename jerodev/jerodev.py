import reflex as rx
import jerodev.constans as const

from jerodev import data
from jerodev.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size, BACKGROUND_IMAGE
from jerodev.views.about import about
from jerodev.views.extra import extra
from jerodev.views.footer import footer
from jerodev.views.header import header
from jerodev.views.info import info
from jerodev.views.tech_stack import tech_stack
from jerodev.views.nav_bar import nav_bar
#from jerodev.views.quotes import quote

DATA = data.data

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            # rx.theme_panel(),
            # Components of my website
            nav_bar(),
            header(DATA),
            about(DATA.about),
            tech_stack(DATA.technologies),
            info("Experiencia", DATA.experience),
            info("Proyectos", DATA.projects),
            info("Formación", DATA.training),
            extra(DATA.extras),
            #quote(),
            rx.divider(),
            footer(DATA.media),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"
        ),
        style=BACKGROUND_IMAGE,
    )

app = rx.App(
    head_components=[
        # Google Analytics script
        rx.script(src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}", async_=True),
        rx.script(f"""
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{const.G_TAG}');
        """),
    ],
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        accent_color="indigo",
        radius="full"
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
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@JeroRmSoyYo"},
        {"char_set": "UTF-8"}
    ]
)
