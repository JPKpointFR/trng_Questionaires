"""question1 = ["la France", "Marseille", "Nice", "Paris", "Nantes"]
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
question(*question1, "c")

question(*question2, "d")

question(*question3, "a")

question(*question4, "b")

print(f"score final: {score}")"""
"""
titre = question[0]
choix = question[1]
bonne_reponse = question[2]
"""


def demander_reponse_numerique_user(min, max):
    reponse_str = input(f"Votre réponse (entre {min} et {max}): ")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int

        print(f"ERREUR: vous devez rentrez un chiffre entre {min} et {max}")
    except:
        print("ERREUR: veullez rentrez uniquement des chiffres")
    return demander_reponse_numerique_user(min, max)


def poser_question(question):
    choix = question[1]
    breponse = question[-1]
    print("QUESTION")
    titre = question[0]
    print("  ", question[0])
    for i in range(len(choix)):
        print(f"  {i+1} - ", choix[i])
    print()
    resultat_reponse_correcte = False
    reponse_int = demander_reponse_numerique_user(1, len(choix))
    if choix[reponse_int - 1].lower() == breponse.lower():
        print(f"Bonne réponse")
        resultat_reponse_correcte = True  # return True
    else:
        print("Mauvaise réponse")

    print()
    return resultat_reponse_correcte
    # return False


question1 = ("Quelle est la capitale de la France ?",
             ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")

question2 = ("Quelle est la capitale de l'Italie ?",
             ("Milan", "Naple", "Vatican", "Rome"), "Rome")

# poser_question(question1)

# poser_question(question2)


def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        poser_question(question)
        score += 1
    print(f"score final: {score}/{len(questionnaire)}")


"""
    questionnaire[]
        question 
        titre = "Quelle est la capitale de la France"
        reponse = ("Marseille", "Nice", "Paris", "Nantes")
"""

questionnaire = (question1, question2)

lancer_questionnaire(questionnaire)
