def talk():
    print("Digite 'sair' para encerrar a conversa.")
    name = "Akynovia"
    while True:
        message = input("Você: ")
        if message == "sair":
            break
        elif "olá" in message.lower():
            print(f"{name}: Olá! Como posso ajudar?")
        elif "Como você está?" in message.lower():
            print(f"{name}: Estou bem, obrigado por perguntar!")
        elif "Qual é o seu nome" in message.lower():
            print(f"{name}: Meu nome é {name}.")
        elif "Me fala uma piada" in message.lower():
            print(f"{name}: Claro, aqui vai uma piada: Por que o gato mia no telhado? Porque ele não sabe miar no chão!")
        elif "o que é inteligência artificial?" in message.lower():
            print(f"{name}: Inteligência artificial é um ramo da ciência da computação que envolve a criação de sistemas e algoritmos que podem executar tarefas que normalmente exigem inteligência humana, como reconhecimento de voz, visão computacional, aprendizado de máquina e tomada de decisão.")
        elif "você gosta de música?" in message.lower():
            print(f"{name}: Sim, eu gosto de música! Qual é a sua música favorita?")
            resposta = input("Você: ")
            print(f"{name}: {resposta} é uma ótima música! Eu também gosto dessa.")
        elif "o que você acha da tecnologia?" in message.lower():
            print(f"{name}: Eu acho a tecnologia incrível! Ela tornou nossas vidas muito mais fáceis e nos permitiu fazer coisas que antes eram impossíveis. E você, o que acha da tecnologia?")
        else:
            print(f"{name}: Desculpe, ainda não fui programada para conversar sobre isso. Tente novamente mais tarde.")
