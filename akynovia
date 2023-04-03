import os
import time
import configparser

# Configurações do assistente virtual
config = configparser.ConfigParser()
config.read('config.ini')

# Nome do usuário
name = config['User']['name']

# Bem-vindo
print(f'Bem-vindo, {name}!')

# Função para exibir a hora atual
def show_time():
    current_time = time.strftime("%H:%M:%S")
    print(f"A hora atual é {current_time}.")

# Função para abrir o navegador w3m
def open_browser(url):
    os.system(f"w3m {url}")

# Loop principal do assistente virtual
while True:
    # Aguarda a entrada do usuário
    command = input("> ")

    # Processa o comando do usuário
    if command == "hora":
        show_time()
    elif command.startswith("navegar "):
        url = command.split(" ")[1]
        open_browser(url)
    elif command == "sair":
        break
    else:
        print("Desculpe, não entendi o que você quer.")

print("Até mais!")
