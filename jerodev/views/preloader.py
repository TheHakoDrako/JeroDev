import reflex as rx
import asyncio
# from jerodev.styles.styles import circular_progress_style

def preloader() -> rx.Component:
    class AppState(rx.State):
        loading: bool = True  # El estado de carga comienza como True.
        
        @rx.background  # Uso del decorador para tareas de fondo.
        async def on_page_load(self):
            async with self:  # Usar un administrador de contexto async with self
                await asyncio.sleep(3)  # Espera de manera asíncrona.
                self.loading = False  # Cambia el estado a False una vez completado.

    return AppState

# rx.cond(
#     AppState.loading,
#     rx.center(
#         rx.chakra.circular_progress(**circular_progress_style, is_indeterminate=True),
#         width="100%",
#         height="100vh"
#     ),