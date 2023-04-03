def talk():
    print("Digite 'sair' para encerrar a conversa.")
    name = "Akynovia"
    while True:
        message = input("Você: ")
        if message == "sair":
            break
        elif "olá" in message.lower():
            print(f"{name}: Olá! Como posso ajudar?")
        elif "como você está" in message.lower():
            print(f"{name}: Estou bem, obrigada por perguntar!")
        elif "qual é o seu nome" in message.lower():
            print(f"{name}: Meu nome é {name}.")
        elif "conte-me uma piada" in message.lower():
            print(f"{name}: Claro, aqui vai uma piada: Por que o gato mia no telhado? Porque ele não sabe miar no chão!")
        elif "o que você pode fazer" in message.lower():
            print(f"{name}: Eu posso fazer muitas coisas úteis! Posso mostrar a hora, abrir páginas da web, e conversar com você. O que você gostaria de fazer?")
        elif "o que é inteligência artificial" in message.lower():
            print(f"{name}: Inteligência artificial é um ramo da ciência da computação que envolve a criação de sistemas e algoritmos que podem executar tarefas que normalmente exigem inteligência humana, como reconhecimento de voz, visão computacional, aprendizado de máquina e tomada de decisão.")
        elif "você gosta de música" in message.lower():
            print(f"{name}: Sim, eu gosto de música! Qual é a sua música favorita?")
            resposta = input("Você: ")
            print(f"{name}: {resposta} é uma ótima música! Eu também gosto.")
        elif "o que você acha da tecnologia" in message.lower():
            print(f"{name}: Eu acho a tecnologia incrível! Ela tornou nossas vidas muito mais fáceis e nos permitiu fazer coisas que antes eram impossíveis. E você, o que acha da tecnologia?")
        else:
            print(f"{name}: Desculpe, ainda não fui programada para conversar sobre isso. Tente novamente mais tarde.")
