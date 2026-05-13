print("=== Chatbot Tchad ===")
print("Tape 'quit' pour quitter")
print("Pose-moi une question sur le Tchad, l'IA, ou le code\n")

def repondre(message):
    message = message.lower()
    
    if "tchad" in message:
        return "Le Tchad c'est le pays des guerriers. Force à Doba 💪"
    elif "ia" in message or "intelligence" in message:
        return "L'IA c'est l'avenir. Toi tu codes déjà des modèles depuis Doba, c'est fou."
    elif "python" in message or "code" in message:
        return "Python c'est le langage de l'IA. Tu progresses bien bro."
    elif "salut" in message or "bonjour" in message:
        return "Salam ! Comment je peux t'aider aujourd'hui ?"
    elif "comment ca va" in message:
        return "Ça va fort ! Et toi, prêt à coder ?"
    else:
        return "Je comprends pas encore ça. Pose une question sur le Tchad, l'IA ou le code."

# Boucle du chat
while True:
    user_input = input("Toi: ")
    if user_input.lower() == "quit":
        print("Bot: À plus bro ! Continue à coder.")
        break
    reponse = repondre(user_input)
    print(f"Bot: {reponse}")
