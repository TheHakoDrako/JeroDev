import reflex as rx
import asyncio

from jerodev import data
from jerodev.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size, circular_progress_style
from jerodev.views.about import about
from jerodev.views.extra import extra
from jerodev.views.footer import footer
from jerodev.views.header import header
from jerodev.views.info import info
from jerodev.views.tech_stack import tech_stack
# from jerodev.views.preloader import AppState


DATA = data.data


# @rx.page(on_load=AppState.on_page_load)
def index() -> rx.Component:
    return rx.center(
        # rx.cond(
        #     AppState.loading,
        #     rx.center(
        #         rx.chakra.circular_progress(**circular_progress_style, is_indeterminate=True),
        #         width="100%",
        #         height="100vh"
        #     ),
            # rx.theme_panel(),
            rx.vstack(
                header(DATA),
                rx.divider(),
                about(DATA.about),
                rx.divider(),
                tech_stack(DATA.technologies),
                info("Experiencia", DATA.experience),
                info("Proyectos", DATA.projects),
                info("Formación", DATA.training),
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
    # )


app = rx.App(
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
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image}
    ]
)
