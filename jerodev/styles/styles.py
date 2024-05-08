from enum import Enum
import reflex as rx


MAX_WIDTH = "900px"
IMAGE_HEIGHT = "200px"
BACKGROUND_COLOR = "#00000052"
BACKGROUND_IMAGE = {
    "background": "url(background.jpg) center fixed no-repeat",
    "backgroundSize": "cover"
    }


class EmSize(Enum):
    DEFAULT = "1em"  # 16px
    MEDIUM = "2em"
    BIG = "4em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"  # 8px
    DEFAULT = "4"  # 16px/1em
    MEDIUM = "6"  # 32px
    BIG = "8"  # 48px


STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
]


BASE_STYLE = {
    rx.button: {
        "--cursor-button": "pointer",
        "boxShadow": "inset rgb(79 103 193 / 80%) 0px 1px 2px 1px",
        "_hover":{
            "boxShadow": "0px 0px 6px 0px #ffffff, 0px 27px 44px -13px color(prophoto-rgb 0.36 0.15 0.97 / 0.1) inset"
        }
    }
}
