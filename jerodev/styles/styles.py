from enum import Enum
import reflex as rx

# Estilos de la página
MAX_WIDTH = "900px"
IMAGE_HEIGHT = "180px"
BACKGROUND_COLOR = "#00000052"
BACKGROUND_IMAGE = {
    "background": "url(background.jpg) center fixed no-repeat",
    "backgroundSize": "cover"
    }

# Estilos de la barra de navegación
NAVBAR = {
    "position": "fixed",
    "top": "18px",
    "left": "50%",
    "transform": "translateX(-50%)",
    "z-index": "10",
    "display": "flex",
    "justifyContent": "center",
    "alignItems": "center",
    "padding": "4px 16px",
    "paddingLeft": "8px",
    "paddingRight": "8px",
    "margin": "4px",
    "borderBottom": "1px solid rgba(0, 0, 0, 0.1)",
    "backgroundColor": "rgb(255 255 255 / 22%)",
    "borderRadius": "15px",  # Bordes redondeados en las esquinas
    "boxShadow": "0px 2px 4px rgba(0, 0, 0, 0.1)",  # Sombra
    "ring": "1",  # Anillo
    "backdropFilter": "blur(10px)",  # Efecto de desenfoque
    "transition": "backgroundColor 0.3s ease-in-out, borderBottom 0.3s ease-in-out",
    "@media (max-width: 768px)": {  # Estilos para dispositivos móviles
        "width": "90%",
        "fontSize": "smaller"
    }
}

# Estilos para los enlaces de navegación
NAVBAR_LINK = {
    "textSizeAdjust": "100%",
    "WebkitTextSizeAdjust": "100%",
    "margin": "3px",
    "color": "rgb(255 255 255)",
    "transition": "color 0.3s ease-in-out"
}

NAVBAR_LINK

# Colores 
class Color(Enum):
    PRIMARY = "#14A1F0"
    SECONDARY = "#087ec4"
    BACKGROUND = "#0C151D"
    CONTENT = "#171F26",
    PURPLE = "#9146ff"

# Colores de texto
class TextColor(Enum):
    HEADER = "#F1F2F4"
    BODY = "#C3C7CB"
    FOOTER = "#A3ABB2"

# Tamaños de fuente
class EmSize(Enum):
    DEFAULT = "1em"  # 16px
    DEFAULT_BIG = "1.5em"  # 24px
    MEDIUM = "2em" # 32px
    BIG = "4em" # 64px

# Espaciado
class Size(Enum):
    ZERO = "0"
    SMALL = "2"  # 8px
    DEFAULT = "4"  # 16px/1em
    MEDIUM = "6"  # 32px
    BIG = "8"  # 48px

# Estilos
STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
]

# Estilos base
BASE_STYLE = {
    "textSizeAdjust": "100%",
    rx.button: {
        "textSizeAdjust": "100%",
        "fontWeight": "var(--font-weight-regular)",
        "--cursor-button": "pointer",
        "boxShadow": "inset rgb(43 84 205) 0px 1px 2px 1px",
        "_hover":{
            "boxShadow": "0px 0px 6px 0px #7c8ae185, 0px 27px 44px -13px color(prophoto-rgb 0.21 0.13 0.49 / 0.23) inset"
        }
    }
}
