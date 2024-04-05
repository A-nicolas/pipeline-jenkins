# Test unitaire pour l'application simple : test_hello.py
from hello import dire_bonjour

def test_dire_bonjour():
    resultat = dire_bonjour("Alice")
    assert resultat == "Bonjour, Alice !"
