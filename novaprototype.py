import random


hello_responses = [
    "hello!",
    "hi!",
    "hey!",
    "hello, how can i help you?"
]


memory = {
    "name": None,
    "favourite_food": None,
    "favourite_game": None
}


def nova_brain(user):

    user = user.lower().strip()


    # GREETINGS

    if "hello" in user or user == "hi" or "hey" in user:
        return random.choice(hello_responses)


    # NAME

    elif "my name is " in user:

        memory["name"] = user.replace(
            "my name is ",
            "",
            1
        )

        return "nice to meet you " + memory["name"] + "!"


    elif "what is my name" in user:

        if memory["name"] is not None:
            return "your name is " + memory["name"] + "!"

        else:
            return "i don't know your name yet."


    # FAVOURITE GAME

    elif "my favourite game is " in user:

        memory["favourite_game"] = user.replace(
            "my favourite game is ",
            "",
            1
        )

        return "cool! i'll remember that."


    elif "what is my favourite game" in user:

        if memory["favourite_game"] is not None:
            return (
                "your favourite game is "
                + memory["favourite_game"]
                + "!"
            )

        else:
            return "i don't know your favourite game yet."


    # FAVOURITE FOOD

    elif "my favourite food is " in user:

        memory["favourite_food"] = user.replace(
            "my favourite food is ",
            "",
            1
        )

        return "cool! i'll remember that."


    elif "what is my favourite food" in user:

        if memory["favourite_food"] is not None:
            return (
                "your favourite food is "
                + memory["favourite_food"]
                + "!"
            )

        else:
            return "i don't know your favourite food yet."


    # UNKNOWN

    else:
        return "i don't understand that yet."


# CONSOLE MODE

if __name__ == "__main__":

    print("NOVA AI is online!")
    print("Type 'quit' to stop NOVA.")
    print()

    while True:

        user = input("You: ")

        if user.lower() == "quit":

            print("NOVA: goodbye!")
            break

        response = nova_brain(user)

        print("NOVA:", response)