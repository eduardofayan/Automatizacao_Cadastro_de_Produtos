# 1º Passo - No CMD (Prompt de comando) use: "pip install pyautogui pillow mouseinfo"
# 2º Passo - Importar a biblioteca Pyautogui no projeto use: import pyautogui
# 3º Passo - Importar o Sleep para poder pausar a execução por alguns segundos

import pyautogui
from time import sleep

# 1 - Executar Arquivo
# 2 - Clicar e digitar meu usuário
pyautogui.click(991,541,duration=0.5)
pyautogui.write('rpa_eduardo_login')

# 3 - Clicar e digitar minha senha
pyautogui.click(1008,576,duration=0.5)
pyautogui.write('123456') 

# 4 - Clicar em "entrar"
pyautogui.click(846,604,duration=0.5)


# 5 - extrair cada produto
with open('produtos.txt', 'r') as file:
    for linha in file:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        # 	1 - Clicar e digitar produto
        pyautogui.click(651,524,duration=0.5)
        pyautogui.write(produto)
        # 	2 - Clicar e digitar quantidade
        pyautogui.click(649,558,duration=0.5)
        pyautogui.write(quantidade)
        # 	3 - Clicar e digitar preço
        pyautogui.click(651,593,duration=0.5)
        pyautogui.write(preco)
        # 	4 - Clicar em registrar
        pyautogui.click(504,781,duration=0.5)
        sleep(1)