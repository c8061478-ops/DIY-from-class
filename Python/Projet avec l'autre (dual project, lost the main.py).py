# Les imports + alphabet
alphabet = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
# Liste donnée

contacts_tries = [ ("Bernard", "0656789012"), ("Chevalier", "0645678901"), ("Diallo", "0623456789"), ("Girard", "0690123456"), ("Lefevre", "0689012345"), ("Martin", "0612345678"), ("Nguyen", "0667890123"), ("Petit", "0601234567"), ("Roux", "0634567890"), ("Simon", "0678901234"), ]

# PARTIE 1
# Carnet vide
def creer_carnet():
    carnet = []
    return carnet

# PARTIE 2
# Ajouter contact
def ajouter_contact(carnet, nom, telephone):
    base_tpl = (nom.title(), telephone) # Définition du tuple
    # Variables nulles pour caller après
    place = 0
    for contacts in carnet: # Check tout l'annuaire
        if int(alphabet[nom.upper()[0]]) > int(alphabet[contacts[0][0]]): # Si la lettre est plus grande
            while int(alphabet[nom.upper()[0]]) > int(alphabet[contacts[0][0]]):
                place += 1 # On change de place
                break # On sort de la boucle
        if int(alphabet[nom.upper()[0]]) == int(alphabet[contacts[0][0]]): # Si la lettre est la même
            for i in range(len(nom.upper())):
                if int(alphabet[nom.upper()[i]]) == int(alphabet[contacts[0][0]]):
                    while int(alphabet[nom.upper()[i]]) == int(alphabet[contacts[0][0]]):
                        if int(alphabet[nom.upper()[i]]) > int(alphabet[contacts[0][0]]): # Si la lettre est plus grande
                            place += 1 # On change de place
                            break # On sort de la boucle
                        if int(alphabet[nom.upper()[i]]) < int(alphabet[contacts[0][0]]): # Si la lettre est plus petite
                            place -= 1 # On change de place
                            break # On sort de la boucle
                        break
    carnet.insert(place, base_tpl) # Add

# PARTIE 3
# Supprimer contact
def supprimer_contact(carnet, nom):
    if nom in carnet:
        carnet.remove(nom) # Remove

"""
1. Comment passe-t-on d’une crise boursière à une crise financière ?
Le 24 octobre 1929, lors du « jeudi noir », puis surtout le 29 octobre 1929, lors du « mardi noir », les cours des actions à la Bourse de Wall Street s’effondrent. C’est le krach boursier : de nombreux investisseurs cherchent à vendre leurs actions en même temps, ce qui provoque une panique et une chute brutale des prix.
Cette crise boursière devient ensuite une crise financière car les banques sont elles aussi touchées. Certaines banques ont prêté de l’argent aux investisseurs pour acheter des actions et ont également investi en Bourse. Lorsque les emprunteurs ne peuvent plus rembourser leurs dettes et que la valeur des actions s’effondre, les banques perdent de l’argent. Les clients, inquiets, retirent alors massivement leur argent, ce qui peut provoquer des faillites bancaires.
👉 À retenir :
Krach boursier → pertes des investisseurs → difficultés des banques → retraits bancaires → faillites bancaires → crise financière.
2. Expliquer le cercle vicieux de la crise de 1929
La crise devient un cercle vicieux, car chaque difficulté en entraîne une autre et aggrave la précédente.
Les faillites bancaires entraînent une diminution des crédits et des investissements. Les entreprises ont donc moins d’argent pour produire et investir. La production baisse, ce qui entraîne des licenciements et une hausse du chômage.
Avec le chômage, les revenus des ménages diminuent. Les ménages consomment donc moins. La baisse de la consommation entraîne une diminution des ventes des entreprises. Les entreprises produisent alors encore moins et licencient davantage.
On obtient donc :
Crise bancaire → baisse des investissements → baisse de la production → chômage → baisse des revenus → baisse de la consommation → baisse des ventes → nouvelle baisse de la production.
C’est un cercle vicieux car la crise s’auto-entretient et s’aggrave.
3. Les définitions importantes
Tu dois être capable de retrouver le mot à partir de la définition et de donner la définition à partir du mot.
Notion
Définition à connaître
Krach boursier
Effondrement brutal des cours des actions en Bourse.
Protectionnisme
Politique qui consiste à protéger la production nationale de la concurrence étrangère, notamment avec des droits de douane.
Dévaluation
Diminution volontaire de la valeur d'une monnaie afin notamment de rendre les exportations plus compétitives.
Taylorisme
Organisation scientifique du travail fondée sur la division et la rationalisation des tâches.
Fordisme
Production de masse standardisée, notamment grâce à la chaîne de montage, associée à Henry Ford.
Autarcie
Recherche de l'autonomie économique d'un pays en limitant sa dépendance envers l'étranger.
Destruction créatrice
Processus par lequel les innovations créent de nouvelles activités tout en faisant disparaître certaines activités anciennes.
New Deal
Ensemble des mesures mises en place par Roosevelt à partir de 1933 pour lutter contre la crise et renforcer l'intervention de l'État.
État-providence
État qui intervient pour protéger les populations contre certains risques sociaux et améliorer leurs conditions de vie.
4. Les personnages à connaître
Franklin D. Roosevelt 🇺🇸
→ Président des États-Unis à partir de 1933.
→ Il met en place le New Deal pour lutter contre la crise.
→ Il renforce fortement l'intervention de l'État dans l'économie.
Léon Blum 🇫🇷
→ Homme politique socialiste et dirigeant de la SFIO.
→ Il devient président du Conseil en 1936 après la victoire du Front populaire.
→ Son gouvernement met en place de grandes réformes sociales : congés payés, semaine de 40 heures, hausse des salaires, droits syndicaux, etc.
Joseph Schumpeter 🇦🇹
→ Économiste.
→ Il insiste sur l'importance de l'innovation dans le fonctionnement du capitalisme.
→ Il développe l'idée de « destruction créatrice » : les innovations créent de nouvelles activités mais peuvent aussi faire disparaître les anciennes.
5. Que s'est-il passé le 6 février 1934 ?
Le 6 février 1934, plusieurs ligues d'extrême droite et autres groupes hostiles au régime parlementaire organisent une grande manifestation à Paris.
Les manifestants se dirigent notamment vers la Chambre des députés. Des affrontements violents ont lieu avec les forces de l'ordre et provoquent plusieurs morts et de nombreux blessés.
Cet événement provoque une grave crise politique et renforce la peur d'une remise en cause de la République. À gauche, il pousse notamment les socialistes et les communistes à se rapprocher pour défendre la République.
Cette dynamique contribue ensuite à la formation du Front populaire, qui rassemble notamment :
PCF → Maurice Thorez
SFIO → Léon Blum
Parti radical → Édouard Daladier
Le Front populaire remporte les élections législatives d'avril-mai 1936.
6. Quelles mesures le Front populaire prend-il en 1936 ?
Après la victoire du Front populaire, Léon Blum devient président du Conseil.
De grandes grèves ont lieu en mai-juin 1936. Elles aboutissent aux accords de Matignon,
"""
