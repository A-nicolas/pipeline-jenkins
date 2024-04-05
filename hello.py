# Application Python simple : hello.py

def dire_bonjour(nom):
    return "Bonjour, " + nom + " !"

if __name__ == "__main__":
    nom = input("Entrez votre nom : ")
    message = dire_bonjour(nom)
    print(message)
