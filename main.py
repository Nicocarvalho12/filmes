#importações necessárias
import random 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen

# primeira tela de Boas-vindas
class TelaBoasVindas(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        self.input_nome = TextInput(hint_text="Digite seu nome", multiline=False)
        self.btn_continuar = Button(text="Continuar", size_hint=(1, 0.2))
        self.label_erro = Label(text="", color=(1,0,0,1))
        self.btn_continuar.bind(on_press=self.ir_para_filmes)
        layout.add_widget(Label(text="Bem-vindo ao App de Filmes!", font_size=28, size_hint=(1,0.3)))
        layout.add_widget(self.input_nome)
        layout.add_widget(self.btn_continuar)
        layout.add_widget(self.label_erro)
        self.add_widget(layout)


# essa função verifica se o nome foi digitado e navega para a tela de filmes
    def ir_para_filmes(self, instance):
        nome = self.input_nome.text.strip()
        if not nome:
            self.label_erro.text = "Por favor, digite seu nome."
            return
        self.manager.get_screen('tela_filmes').set_nome(nome)
        self.manager.current = 'tela_filmes'

# segunda tela de Sugestão de Filmes
class TelaFilmes(Screen):
    def __init__(self, **kwargs): # essa linha inicializa a tela de filmes
        super().__init__(**kwargs)
        self.nome_usuario = ""
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        self.label_boasvindas = Label(text="", font_size=22, size_hint=(1, 0.2))
        self.spinner = Spinner(
            text="Escolha um gênero",
            values=("Ação", "Comédia", "Animação", "Terror", "Romance", "Ficção Científica", "Drama"),
            size_hint=(1, 0.15)
        )
        #essa parte cria o botão de sugerir filme e o label para mostrar o resultado
        self.btn_sugerir = Button(text="Sugerir Filme", size_hint=(1, 0.15))
        self.btn_sugerir.bind(on_press=self.sugerir_filme)
        self.label_resultado = Label(text="", font_size=18, size_hint=(1, 0.2))
        self.btn_voltar = Button(text="Voltar", size_hint=(1, 0.12))
        self.btn_voltar.bind(on_press=self.voltar)


          #essa parte adiciona todos os widgets ao layout
        self.layout.add_widget(self.label_boasvindas)
        self.layout.add_widget(self.spinner)
        self.layout.add_widget(self.btn_sugerir)
        self.layout.add_widget(self.label_resultado)
        self.layout.add_widget(self.btn_voltar)
        self.add_widget(self.layout)

# essa função define o nome do usuário e atualiza a mensagem de boas-vindas
    def set_nome(self, nome):
        self.nome_usuario = nome
        self.label_boasvindas.text = f"Ola, {nome}! Escolha um gênero de filme:"
# essa função sugere um filme baseado no gênero selecionado
    def sugerir_filme(self, instance):
        genero = self.spinner.text
# listas de filmes por gênero
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
# lógica para escolher um filme aleatório baseado no gênero selecionado

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
            self.label_resultado.text = "Escolha um gênero de filme."#se nenhum gênero for selecionado, pede para escolher um
            return

        self.label_resultado.text = f"Sua sugestão de filme de {genero}: {filme} ({ano})." #mostra a sugestão de filme

    def voltar(self, instance):
        self.manager.current = 'tela_boasvindas'

class FilmeApp(App):# essa parte inicializa o app e o gerenciador de telas
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaBoasVindas(name='tela_boasvindas'))
        sm.add_widget(TelaFilmes(name='tela_filmes'))
        return sm

if __name__ == "__main__":
    FilmeApp().run()