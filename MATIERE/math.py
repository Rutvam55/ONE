import random
def opperateur(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        c = b * a
        return c / a, c

def choisir_un_nombre(min, max):
    a = random.randint(min, max)
    b = random.randint(min, max)
    return a, b

def math_base():
    i = ["addition", "soustraction", "multiplication", "division"]
    choix = random.choice(i)
    if choix == "addition":
        op = "+"
        a, b = choisir_un_nombre(-100, 100)
        reponse_correct = opperateur(a, b, op)
        if a > 0:
            a = "+" + str(a)
        elif b > 0:
            b = "+" + str(b)
    elif choix == "soustraction":
        op = "-"
        a, b = choisir_un_nombre(-100, 100)
        reponse_correct = opperateur(a, b, op) 
        if a > 0:
            a = "+" + str(a)
        elif b > 0:
            b = "+" + str(b)
    elif choix == "multiplication":
        op = "*"
        a, b = choisir_un_nombre(-12, 12)
        reponse_correct = opperateur(a, b, op)
        if a > 0:
            a = "+" + str(a)
        elif b > 0:
            b = "+" + str(b)
    elif choix == "division":
        op = "/"
        b, c = choisir_un_nombre(-12, 12)
        reponse_correct, a = opperateur(c, b, op)
        if a > 0:
            a = "+" + str(a)
        elif b > 0:
            b = "+" + str(b)
    question = f"Calcul\n ({a}) {op} ({b}) = ?\n>"
    return question, reponse_correct
