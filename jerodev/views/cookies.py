import reflex as rx

class CookieState(rx.State):
    show_dialog: str = rx.Cookie("true")
    accept_cookies: str = rx.Cookie("false")
    dialog_closed: bool = False

    @rx.var
    def cookies_accepted(self) -> bool:
        return self.accept_cookies == "true"

    @rx.var
    def should_show_dialog(self) -> bool:
        return self.show_dialog == "true" and not self.dialog_closed

    def toggle_cookies(self, value: bool):
        self.accept_cookies = "true" if value else "false"

    def close_dialog(self):
        self.dialog_closed = True

    def save_and_close(self):
        if self.cookies_accepted:
            self.show_dialog = "false"
        self.dialog_closed = True

    def handle_dialog_change(self, open: bool):
        if not open:
            self.dialog_closed = True

def cookie_dialog():
    return rx.dialog.root(
        rx.dialog.content(
            rx.flex(
                rx.center(
                    rx.dialog.title("Configuración de Cookies"),
                    justify="center",
                    align="center",
                    width="100%",
                ),
                width="100%"
            ),
            rx.dialog.description("¿Acepta el uso de cookies de terceros para Google Analytics?", style={"width": "100%", "textAlign": "center"}),
            rx.flex(
                rx.switch(
                    checked=CookieState.cookies_accepted,
                    on_change=CookieState.toggle_cookies,
                    ariaLabel="Aceptar cookies de Google Analytics",
                    style={"margin": "12px"},
                ),
                width="100%",
                justify="center",
                align="center",
            ),
            rx.button("Guardar", on_click=CookieState.save_and_close, ariaLabel="Guardar configuración de cookies", style={"width": "100%"}),
        ),
        open=CookieState.should_show_dialog,
        on_open_change=CookieState.handle_dialog_change,
    )