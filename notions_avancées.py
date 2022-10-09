# def a(n, limit):
#     if n > limit:
#         return
#     print("n:", n)
#     a(n*n, limit)

# a(2, 100000)

"""""     LA RECURSIVITE     """
# def demander_choix_user(min, max):
#     reponse_str = input(f"Quel est votre choix entre {min} et {max}: ")
#     try:
#         reponse_int = int(reponse_str)
#         if not min <= reponse_int <= max:
#             print(f"ERREUR: vous devez rentrer un nombre entre {min} et {max}")
#             return demander_choix_user(min, max)
#         return reponse_int
#     except:
#         print("ERREUR: vous devez rentrer un nombre")
#         return demander_choix_user(min, max)


# choix = demander_choix_user(1, 4)
# print(f"choix de l'utilisateur: {choix}")

# def ma_function():
#     print("toto")
#     return 1

# #CALL BACK--------------------------
# """a = 5

# b = ma_function

# print("a", a, "b", ma_function())"""

# def table_multiplication(n):
#     for i in range(1, 10):
#         print(f" {i} x {n} = {i*n}")


# def table_addition(n):
#     for i in range(1, 10):
#         print(f" {i} + {n} = {i+n}")

"""
def mult_cbk(a, b):
    return a*b


def add_cbk(a, b):
    return a+b
"""


def affichez_table(n, operateur_str, operation_cbk):
    for i in range(1, 10):
        print(f" {i} {operateur_str} {n} = {operation_cbk(i, n)}")


# LAMBDA
affichez_table(2, "x", lambda a, b: a * b)  # mult_cbk
print()
affichez_table(2, "+", lambda a, b: a+b)  # add_cbk
