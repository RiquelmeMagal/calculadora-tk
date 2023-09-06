# Importação dos módulos necessários
from tkinter import *
from tkinter import Menu
from tkinter.messagebox import showerror 
from webbrowser import open_new
from  tkinter.messagebox import askyesno
import math


acumulador = ''
rad = True

def callback(url):
    """
    Abre a URL fornecida no navegador padrão.
    """
    open_new(url)

def sair():
    """
    Fecha a janela da instância do Tkinter com uma confirmação.
    """
    pergunta = askyesno(title='Confirmação',
                    message='Tem certeza de que deseja sair?')
    if pergunta:
        janela.destroy()

def formatar_numero(numero, comprimento=10):
    """
    Formata um número para exibição, arredondando para até 10 casas decimais, se necessário.
    """
    return round(numero, comprimento) if len(str(numero))  > comprimento else numero
        
def obter_caractere(e):
    """
    Atualiza o acumulador e a expressão atual com um caractere fornecido.
    """
    global acumulador, expressao_atual, ultimo_caractere

    # Adiciona o caractere recebido ao acumulador
    acumulador += str(e)

    # Atualiza a expressão atual com o valor do acumulador
    expressao_atual.set(acumulador)

def limpar_display():
    """
    Limpa o display da calculadora, redefinindo o acumulador e a expressão atual.
    """
    global acumulador, expressao_atual

    # Redefine o acumulador para uma string vazia
    acumulador = ''
    # Atualiza a expressão atual para uma string vazia
    expressao_atual.set('')

def tratar_expressao(expressao):
    if 'e' in expressao:
        expressao = expressao.replace('e', 'math.e')
    if 'log' in expressao:
        expressao = expressao.replace('log', 'math.log')
    if 'sinh' in expressao:
        expressao = expressao.replace('sinh', 'math.sinh')
    if 'cosh' in expressao:
        expressao = expressao.replace('cosh', 'math.cosh')
    if 'tanh' in expressao:
        expressao = expressao.replace('tanh', 'math.tanh')
    if 'asin' in expressao:
        expressao = expressao.replace('asin', 'math.asin')
    if 'acos' in expressao:
        expressao = expressao.replace('acos', 'math.acos')
    if 'atan' in expressao:
        expressao = expressao.replace('atan', 'math.atan')
    if 'π' in expressao:
        expressao = expressao.replace('π', 'math.pi')

    return expressao

def sin():
    global acumulador
    try:
        n = float(acumulador)
        limpar_display()

        if rad:
            obter_caractere(math.sin(math.radians(n)))
        else:
            obter_caractere(math.sin(n))
    except:
        pass

def cos():
    global acumulador
    try:
        n = float(acumulador)
        limpar_display()

        if rad:
            obter_caractere(math.cos(math.radians(n)))
        else:
            obter_caractere(math.cos(n))
    except:
        pass
    
def tan():
    global acumulador
    try:
        n = float(acumulador)
        limpar_display()

        if rad:
            obter_caractere(math.tan(math.radians(n)))
        else:
            obter_caractere(math.tan(n))
    except:
        pass

def calcular_expressao():
    """
    Calcula e atualiza o resultado da expressão no display da calculadora.
    """
    global acumulador, expressao_atual

    if len(acumulador) > 0:
        try:
            # Avalia a expressão no acumulador
            resultado = eval(tratar_expressao(acumulador))

            # Verifica se o resultado é um número inteiro 
            if int(resultado) == resultado:
                expressao_atual.set(int(resultado))
            else:   
                # Formata o resultado e atualiza a expressão atual
                resultado_formatado = formatar_numero(resultado)
                expressao_atual.set(resultado_formatado)

            # Atualiza o acumulador com a expressão atual
            acumulador = expressao_atual.get()
        except:
            # Em caso de erro na expressão, mostra uma mensagem de erro
            showerror('Erro', 'Expressão mal formada')
            limpar_display()

def criar_botao(text='', command=None):
    botao = Button(frame_botao, 
                   text=text, 
                   background='#ffffff', 
                   foreground='black', 
                   font=('Arial', 20),
                   borderwidth=0,
                   cursor='hand2',
                   height=2,
                   width=5,
                   command=command) 
    return botao

def trocar_modo_rad_deg():
    global rad, texto_botao_rad_deg

    if rad:
        texto_botao_rad_deg.set('DEG')
        rad = False
    else:
        texto_botao_rad_deg.set('RAD')
        rad = True

def janela_modo_cientifico():
    global texto_botao_rad_deg

    janela.geometry('647x574')

    botoes_cientificos = {
        '%': (0, 5), 'asin': (1, 5), 'acos': (2, 5), 'atan': (3, 5), 'π': (4, 6),
        'sinh': (1, 7), 'cosh': (2, 7), 'tanh': (3, 7), 'e' : (4,5),'log': (4, 7),
    }

    botao_sin = criar_botao('sin', lambda:sin()).grid(row=1, column=6, sticky=NSEW)
    botao_cos = criar_botao('cos', lambda:cos()).grid(row=2, column=6, sticky=NSEW)
    botao_tan = criar_botao('tan', lambda:tan()).grid(row=3, column=6, sticky=NSEW)

    for caractere, posicao in botoes_cientificos.items():
        botao = criar_botao(caractere, lambda x=caractere: obter_caractere(x))
        botao.grid(row=posicao[0], column=posicao[1], sticky=NSEW)

    botao_rad_deg = criar_botao()
    botao_rad_deg.configure(textvariable=texto_botao_rad_deg, 
                            background='#daffcc', 
                            foreground='green', 
                            activebackground='#daffcc', 
                            activeforeground='green')
    botao_rad_deg.bind("<Button-1>", lambda e: trocar_modo_rad_deg())
    botao_rad_deg.grid(row=0, column=6, sticky=NSEW, columnspan=2)

def janela_modo_default():
    janela.geometry('388x574')

def centralizar_janela(root_, width_, height_):
        screen_width = root_.winfo_screenwidth()
        screen_height = root_.winfo_screenheight()
        pos_x = screen_width // 2 - width_ // 2
        pos_y = screen_height // 2 - height_ // 2

        root_.geometry(f'{width_}x{height_}+{pos_x}+{pos_y}')

def janela_sobre():
    janela_sobre = Toplevel(janela)

    centralizar_janela(janela_sobre, 385, 202)

    janela_sobre.title('Sobre a Calculadora TK')
    janela_sobre.resizable(0, 0)
    janela_sobre.attributes('-topmost', True)
    janela_sobre.attributes('-alpha', 0.9)

    label_program_name = Label(janela_sobre, 
                                text='Calculadora TK', 
                                font=('Arial', 10, 'bold')).place(x=0, y=0)

    label_license = Label(janela_sobre, 
                            text=f'Este projeto está licenciado sob a licença CC BY 4.0', 
                            font=('Arial', 10, 'bold')).place(x=0, y=25)

    label_ufal = Label(janela_sobre, 
                            text='Universidade Federal de Alagoas - UFAL', 
                            font=('Arial', 10)).place(x=0, y=45)

    label_course_name = Label(janela_sobre, 
                            text='Curso de Ciência da Computação', 
                            font=('Arial', 10)).place(x=0, y=65) 

    label_project = Label(janela_sobre, 
                            text='Projeto de monitoria da disciplina APC', 
                            font=('Arial', 10)).place(x=0, y=105) 
    
    label_teaching_assistants = Label(janela_sobre, 
                            text='Monitores: João V. V. Santos, Riquelme Magalhães de Souza', 
                            font=('Arial', 10)).place(x=0, y=125) 
    
    label_teacher = Label(janela_sobre, 
                            text='Docentes: Alexandre de Andrade Barbosa, Rodolfo C. Cavalcante', 
                            font=('Arial', 10)).place(x=0, y=145)

    label_repository = Label(janela_sobre, 
                    text='Código fonte', 
                    font=('Arial', 10, 'bold'), foreground='blue', cursor='hand2') 
    label_repository.bind("<Button-1>", lambda e: callback('https://github.com/oaojcc/calculadora-tk'))
    label_repository.place(x=0, y=175)

# Cria um dicionário que mapeia os dígitos para suas posições na grade.
caracteres = {
        '(': (0, 2), ')': (0, 3), '/': (0, 4),
        7: (1, 1), 8: (1, 2), 9: (1, 3), '*': (1, 4),
        4: (2, 1), 5: (2, 2), 6: (2, 3), '-' : (2, 4), 
        1: (3, 1), 2: (3, 2), 3: (3, 3), '+': (3, 4),
        0: (4, 2), '.': (4, 1),
}

# Cria uma janela do Tkinter.
janela = Tk()

# Define o título da janela como "Calculadora TK".
janela.title('Calculadora TK')

# Define o tamanho da janela para 388 pixels de largura e 574 pixels de altura.
centralizar_janela(janela, 388, 574)

# Define que a janela não poderá ser redimensionada pelo usuário
janela.resizable(0, 0)

# sobreposição de app
janela.wm_attributes('-topmost', True)

# StringVar
expressao_atual = StringVar()
texto_botao_rad_deg = StringVar(value='RAD')

# Menu
# Criação do objeto Menu e associação à janela
menubar = Menu(janela)

# Criação de um submenu com a opção de não destacar o primeiro item
menu_opt = Menu(menubar, tearoff=FALSE)

# Criação de um submenu aninhado
sub_menu = Menu(menu_opt, tearoff=0)
sub_menu.add_command(label='Padrão', command=lambda:janela_modo_default())  # Adiciona a opção 'Padrão' ao submenu
sub_menu.add_command(label='Científica', command=lambda:janela_modo_cientifico())  # Adiciona a opção 'Científica' ao submenu

# Associa o submenu aninhado ao item 'Calculadora' do menu principal
menu_opt.add_cascade(
    label='Calculadora',
    menu=sub_menu
)

# Adiciona uma separação visual no menu principal
menu_opt.add_separator()

# Adiciona a opção 'Sair' ao menu principal, com a ação de fechar a janela quando selecionada
menu_opt.add_command(label='Sair', command=lambda:sair())

# Adiciona o menu principal ('Calculadora' e 'Sair') ao menu principal da janela
menubar.add_cascade(label='Opções', menu=menu_opt)

# Criação de um submenu separado ('Ajuda')
menu_sobre = Menu(menubar, tearoff=FALSE)

# Adiciona a opção 'Sobre' ao submenu 'Ajuda', com ação para exibir informações sobre a aplicação
menu_sobre.add_command(label='Sobre a Calculadora TK', command=lambda:janela_sobre())

# Adiciona o submenu 'Ajuda' ao menu principal da janela
menubar.add_cascade(label='Ajuda', menu=menu_sobre)

# Configura o menu criado como o menu da janela
janela.config(menu=menubar)

# Cria um contêiner para o display.
frame_display = Frame(janela, height=15, background='#f5f5f5')

# Adiciona o contêiner para o display à janela.
frame_display.pack(fill=BOTH)

texto_display = Entry(frame_display, textvariable=expressao_atual, background='#f5f5f5', font=('Arial', 50, 'bold'), state=DISABLED, borderwidth=9, justify=RIGHT)
texto_display.pack(side=RIGHT)

# Cria um contêiner para os botões.
frame_botao = Frame(janela, background='black')

# Adiciona o contêiner para os botões à janela.
frame_botao.pack(fill=BOTH)

# Cria um botão para cada dígito e o adiciona ao contêiner para os botões.
for caractere, posicao in caracteres.items():
    botao = criar_botao(str(caractere), lambda x=str(caractere): obter_caractere(x))
    if caractere in [0,1,2,3,4,5,6,7,8,9,'.']:
            botao.configure(font=('Arial', 24, 'bold'))
    botao.grid(row=posicao[0], column=posicao[1], sticky=NSEW)

# boão apagar
botao_apagar = criar_botao('C', command=lambda:limpar_display()).grid(row=0, column=1, sticky=NSEW)

# boão igual
botao_igual = criar_botao('=', command=lambda:calcular_expressao())
botao_igual.configure(background='#daffcc', 
                      foreground='green', 
                      activebackground='#daffcc', 
                      activeforeground='green')
botao_igual.grid(row=4, column=3, sticky=NSEW, columnspan=2)

# Inicia o loop principal do Tkinter, que faz com que a janela seja exibida e o programa permaneça em execução até que o usuário feche a janela.
janela.mainloop()
