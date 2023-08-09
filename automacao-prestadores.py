import webbrowser
import pyautogui
import pyperclip
import time
import os
import datetime

# Outras informações do email
destinatario = "email-do-destinatario1@dominio.com; email-do-destinatario2@dominio.com"
copia = "email-do-destinatario3@dominio.com"
assunto = "Assunto do E-mail"
# Obter a data e hora atual
data_hora_atual = datetime.datetime.now()

# Formatar a data e hora como desejado
data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M")

# Atualizar a mensagem com a data e hora formatada
mensagem = f"""
Segue e-mail atualizado em: {data_hora_formatada}

Att;
Robô
"""

# Abrir o Gmail no navegador padrão
webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")

# Esperar um pouco para o Gmail carregar
time.sleep(10)

# Preencher campos do email
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

pyperclip.copy(copia)
pyautogui.hotkey("ctrl", "shift", "b")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
time.sleep(2)

pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
time.sleep(2)

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# Pressionar TAB para focar no botão "Anexar arquivo" e depois pressionar Enter
pyautogui.press("tab")
pyautogui.press("enter")

# Esperar um pouco para a janela de seleção de arquivo abrir
time.sleep(2)

# Caminho completo do arquivo mais recente
# Pasta onde estão os arquivos
pasta_anexos = "C:\\AUTOMACAO\AUTOMAÇÃO-PYTHON"

# Selecionar o arquivo mais recente
arquivos = sorted(os.listdir(pasta_anexos), key=lambda f: os.path.getmtime(os.path.join(pasta_anexos, f)), reverse=True)
anexo = os.path.join(pasta_anexos, arquivos[0])

# Copiar o caminho do arquivo para a área de transferência
pyperclip.copy(anexo)

# Esperar um pouco para o arquivo ser copiado
time.sleep(2)

# Pressionar TAB para focar no botão "Abrir ANexo" e depois pressionar Enter
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)
# Simular o pressionamento das teclas de atalho para colar o conteúdo no campo Nome
pyautogui.hotkey("ctrl", "v")

# Pressionar Enter para confirmar o anexo
pyautogui.press("enter")

# Esperar um pouco para garantir que o anexo tenha sido adicionado
time.sleep(2)

# Pressionar TAB para focar no botão "Enviar" e depois pressionar Enter
pyautogui.press("tab")
pyautogui.press("enter")

# Imprimir mensagem de enviado com sucesso
print('E-mail com anexo enviado com sucesso!')
