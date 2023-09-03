import copy

from google_trans_new import google_translator

Translator = google_translator()

def TraduireMot(mot):
    motTraduit = Translator.translate(mot, lang_src = 'fr', lang_tgt = 'en')
    while " " == motTraduit[-1]:
        motTraduit = motTraduit[:-1]
    while " " == motTraduit[0]:
        motTraduit = motTraduit[1:]
    return motTraduit



L = open("Fichier utiles/liste_francais.txt","r",encoding="utf-8").read().split("\n")

import Dictionnaire
ListeMot = copy.deepcopy(Dictionnaire.ListeMot)

for i in range(18572,len(L)):
    ListeMot.append({"mot":L[i],"motTraduit":TraduireMot(L[i])})
    open("Dictionnaire.py", "w", encoding="utf-8").write("ListeMot = " + str(ListeMot).replace("},","},\n"))
    print(i,"/",len(L))

