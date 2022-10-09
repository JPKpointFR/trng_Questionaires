question1 = ["la France", "Marseille", "Nice", "Paris", "Nantes"]
question2 = ["l'Italie", "Milan", "Naple", "Vatican", "Rome"]
question3 = ["l'Alemagne", "Berlin", "Dortmund", "Munich", "Leverkussen"]
question4 = ["l'Angleterre", "Manchester", "Londre", "Liverpool", "Brighton"]


def question(pays, ville1, ville2, ville3, ville4, breponse):
    global score
    print(f"Question: Quelle est la capitale de {pays} ?")
    print(f"a - {ville1}")
    print(f"b - {ville2}")
    print(f"c - {ville3}")
    print(f"d - {ville4}")
    print()
    reponse = input("Votre réponse: ")
    if reponse == breponse:
        print(f"Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")

    print()


score = 0
question(question1[0], question1[1], question1[2],
         question1[3], question1[4], "c")

question(question2[0], question2[1], question2[2],
         question2[3], question2[4], "d")

question(question3[0], question3[1], question3[2],
         question3[3], question3[4], "a")

question(question4[0], question4[1], question4[2],
         question4[3], question4[4], "b")

print(f"score final: {score}")
