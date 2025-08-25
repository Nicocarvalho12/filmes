#importações necessárias
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

# Classe principal do aplicativo
class FilmeApp(App): 
    def build(self):
        # Layout principal
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Campo para o nome
        self.nome_input = TextInput(hint_text="Digite seu nome", multiline=False)
        self.layout.add_widget(self.nome_input)

        # menu suspenso para escolher gênero
        self.spinner = Spinner(
            text="Escolha um gênero",
            values=("Ação", "Comédia", "Animação", "Terror", "Romance", "Ficção Científica", "Drama"),
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.spinner)

        # Botão de sugerir filme
        self.btn_sugerir = Button(text="Sugerir Filme", size_hint=(1, 0.2))
        self.btn_sugerir.bind(on_press=self.sugerir_filme)
        self.layout.add_widget(self.btn_sugerir)

        # Botão de limpar
        self.btn_limpar = Button(text="Limpar", size_hint=(1, 0.2))
        self.btn_limpar.bind(on_press=self.limpar)
        self.layout.add_widget(self.btn_limpar)

        # Label para exibir a sugestão
        self.resultado = Label(text="")
        self.layout.add_widget(self.resultado)

        return self.layout

    def sugerir_filme(self, instance):
        nome = self.nome_input.text.strip()
        genero = self.spinner.text

        # Listas dos filmes com ano de lançamento
        filmes_acao = [
            ("Matrix", 1999), ("John Wick", 2014), ("Gladiador", 2000),
            ("Mad Max: Estrada da Fúria", 2015), ("Duro de Matar", 1988)
        ]
        filmes_comedia = [
            ("As Branquelas", 2004), ("Se Beber, Não Case!", 2009), ("Click", 2006),
            ("O Máskara", 1994), ("Superbad", 2007)
        ]
        filmes_animacao = [
            ("Toy Story", 1995), ("Shrek", 2001), ("Procurando Nemo", 2003),
            ("Os Incríveis", 2004), ("Divertida Mente", 2015)
        ]
        filmes_terror = [
            ("Invocação do Mal", 2013), ("O Exorcista", 1973), ("It: A Coisa", 2017),
            ("Hereditário", 2018), ("Halloween", 1978)
        ]
        filmes_romance = [
            ("Titanic", 1997), ("Como Eu Era Antes de Você", 2016), ("Diário de uma Paixão", 2004),
            ("La La Land", 2016), ("Querido John", 2010)
        ]
        filmes_scifi = [
            ("Interestelar", 2014), ("Star Wars: Uma Nova Esperança", 1977), ("Blade Runner", 1982),
            ("A Origem", 2010), ("O Quinto Elemento", 1997)
        ]
        filmes_drama = [
            ("O Poderoso Chefão", 1972), ("Um Sonho de Liberdade", 1994), ("Clube da Luta", 1999),
            ("Forrest Gump", 1994), ("O Menino do Pijama Listrado", 2008)
        ]
        #se o nome estiver vazio vai pedir para digitar o nome
        if not nome:
            self.resultado.text = "Por favor, digite seu nome."
            return 
 #se o gênero estiver vazio vai pedir para escolher um gênero
        if genero == "Ação":
            filme, ano = random.choice(filmes_acao)
        elif genero == "Comédia":
            filme, ano = random.choice(filmes_comedia)
        elif genero == "Animação":
            filme, ano = random.choice(filmes_animacao)
        elif genero == "Terror":
            filme, ano = random.choice(filmes_terror)
        elif genero == "Romance":
            filme, ano = random.choice(filmes_romance)
        elif genero == "Ficção Científica":
            filme, ano = random.choice(filmes_scifi)
        elif genero == "Drama":
            filme, ano = random.choice(filmes_drama)
        else:
            self.resultado.text = "Escolha um gênero de filme."
            return

        self.resultado.text = f"Olá, {nome}! Sua sugestão de filme de {genero} é: {filme} ({ano})."
 # Função para limpar os campos
    def limpar(self, instance):
        self.nome_input.text = ""
        self.spinner.text = "Escolha um gênero"
        self.resultado.text = ""


if __name__ == "__main__":
    FilmeApp().run()
