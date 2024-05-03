import reflex as rx
import random
import json

with open("assets/data/data.json", encoding="utf-8") as file:
    json_data = json.load(file)
    
class Quote:
    def __init__(self, description, author):
        self.description = description
        self.author = author

class Data:
    def __init__(self,quotes):
        self.quotes = [Quote(**quote) for quote in quotes]

class QuoteState(rx.State):
    current_quote: str = "Presiona el botón para obtener una cita"
    current_author: str = "de Autor"

    quotes = [(Quote(**quote).description, Quote(**quote).author) for quote in json_data["quotes"]]
    
    def change_quote(self):
        description, author = random.choice(self.quotes)
        self.current_author = author
        self.current_quote = description
