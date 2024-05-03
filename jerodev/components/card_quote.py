import reflex as rx
import random
from jerodev.data import data, Quote

class QuoteState(rx.State):
    current_quote: str = "Presiona el botón para obtener una cita"
    current_author: str = "de Autor"
    quote = Quote
    quotes = [(quote.description, quote.author) for quote in data.quotes]

    def change_quote(self):
        description, author = random.choice(self.quotes)
        self.current_author = {author}
        self.current_quote = {description}
