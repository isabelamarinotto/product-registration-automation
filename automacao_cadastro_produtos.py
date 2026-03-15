
import pyautogui
import time

# pyautogui.write -> escrever um texto    
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.5
link_sistema = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

#Passo 1: entrar no sistema da empresa
pyautogui.press('win')
pyautogui.write('chrome')    
pyautogui.press('enter')
pyautogui.click(x=772, y=604)
pyautogui.click(x=299, y=66)
pyautogui.write(link_sistema)
pyautogui.press('enter')
#fazer uma pausa
#   Mouse   a maior somente nesse ponto pra dar tempo de carregar o site (importar biblioteca time):
time.sleep(3)

#Passo 2: fazer login
pyautogui.click(x=887, y=409)
pyautogui.write('email_email@gmail.com')
pyautogui.press('tab')
pyautogui.write('senha123')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

#Passo 3: importar a base de produtos pra cadastrar
import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:

#se a base tiver mais de uma aba, usar o read_excel e especificar a aba:
#tabela = pandas.read_excel('produtos.xlsx', sheet_name='nome_da_aba') mas é so em arquivos excel

#Passo 4: cadastrar um produto
#codigo
    pyautogui.click(x=822, y=293)
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    #sempre que for localizar uma informação bota colchetes 

    #marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    #tipo
    pyautogui.press('tab')
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    #categoria
    pyautogui.press('tab')
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    #preco
    pyautogui.press('tab')
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    #custo
    pyautogui.press('tab')
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    #obs
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    #enviar
    pyautogui.press('tab')
    pyautogui.press('enter')

    #voltar para o  inicio da tela
    pyautogui.scroll(1000) 


#Passo 5: repetir o passo 4 para cadastrar os outros produtos da base

