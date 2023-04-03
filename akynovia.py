import time
import configparser
from open_browser import open_browser
from show_time import show_time
from talk import talk

# Abre o arquivo config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Verifica se o nome do usuário já está configurado
if 'User' in config and 'name' in config['User']:
    name = config['User']['name']
else:
    name = "Usuário"

# Bem-vindo
print(f'Bem-vindo, {name}!')

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
    elif command == "conversar":
        talk()
    elif command == "sair":
        break
    else:
        print("Desculpe, não entendi o que você quer.")

print("Até mais!")
