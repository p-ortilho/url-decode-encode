import reflex as rx
import urllib.parse
from rxconfig import config

class State(rx.State):
    code: str = ""

    def encode(self):
        self.code = urllib.parse.quote(self.code)

    def decode(self):
        self.code = urllib.parse.unquote(self.code)


def index() -> rx.Component:
    return rx.flex(
        rx.color_mode.button(position="top-right"),
        rx.container(
            rx.vstack(
                rx.heading(
                    "URL DECODE|ENCODE",
                    font_family="Mochiy Pop One"
                ),
                rx.list.unordered(
                    rx.list.item("Para utilizar basta colocar um sequência de texto, depois codifique ou decodifique-a."),
                    rx.list.item("Útil para transformar URLs JavaScript codificadas em um texto legível.")
                ),
                rx.text_area(
                    placeholder="Digite o código",
                    value=State.code,
                    on_change=State.set_code,
                    width="100%",  
                    height="200px",  
                    style={"font_size": "20px"},  
                ),
                rx.grid(
                    rx.button(
                        "Decode",
                        variant="soft",
                        on_click=State.decode,
                        width="150px",  
                        height="50px",  
                        style={"font_size": "18px"},  
                    ),
                    rx.button(
                        "Encode",
                        on_click=State.encode,
                        width="150px",  
                        height="50px",  
                        style={"font_size": "18px"},  
                    ),
                    columns="2",
                    spacing="8",
                    spacing_y="4"
                ),
                spacing="8",
                width="100%",
                align="center",
                justify="center",
            ),
            height="50vh",
            width="80%",  
        ),
        width="100%",
        height="100vh",
        justify="center",
        align="center",
)
    
app = rx.App(
    theme=rx.theme(
        appearance='dark', has_background=True, radius="large", accent_color="purple"
    ),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Mochiy+Pop+One&display=swap"
    ]
)

app.add_page(index)