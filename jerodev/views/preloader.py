import reflex as rx
import asyncio

class AppState(rx.State):
     loading: bool = True  # El estado de carga comienza como True.

     @rx.background  # Uso del decorador para tareas de fondo.
     async def on_page_load(self):
         async with self:  # Usar un administrador de contexto async with self
             await asyncio.sleep(3)  # Espera de manera asíncrona.
             self.loading = False  # Cambia el estado a False una vez completado.