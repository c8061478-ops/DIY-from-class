#1
'''
t = [[3, 8, 1],
     [7, 2, 9],
     [4, 6, 5]]

a = t[1][2]
b = t[2][0]
c = t[1][1]
d = t[-1][-1]
nb_lignes = len(t)
nb_colonnes = len(t[0])
ligne = t[1]
#print(t[3][0]) #Flemme de exe l'erreur mais c'est prcq y'a pas de 3e indice
assert a == 9 and b == 4 and c == 2 and d == 5
assert nb_lignes == 3 and nb_colonnes == 3
assert ligne == [7, 2, 9]
'''
#2
'''
plan = [["Inès", "Malo", "Léa"],
        ["Yanis", "Zoé", "Enzo"],
        ["Lina", "Noah", "Jade"]]
print(plan[0][1])
print(plan[2][1])
plan[1][1], plan[2][1] = plan[2][1], plan[1][1]
plan[0][2] = ""
plan.append(["Tom", "Sam", ""])
assert plan == [["Inès", "Malo", ""],
["Yanis", "Noah", "Enzo"],
["Lina", "Zoé", "Jade"],
["Tom", "Sam", ""]]
'''
#3
'''
g = [[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]]
g[0][3] = 7
g[-1][0] = 3
for i in range(len(g)):
    g[i][i] = 1
for j in range(len(g)):
    g[2][j] = 5
for ligne in g:
    print(ligne)
assert g == [[1, 0, 0, 7],
[0, 1, 0, 0],
[5, 5, 5, 5],
[3, 0, 0, 1]]
'''
#4
'''
eleves = [["Inès", 14, 12],
["Malo", 9, 15],
["Léa", 17, 19],
["Yanis", 11, 8]]
for i in range(len(eleves)):
    print(f"{eleves[i][0]} a eu {eleves[i][2]} en NSI")
def moyenne_nsi(t):
     somme = 0
     for i in range(len(t)):
          somme += t[i][2]
     return somme / len(t)
def meilleur_maths(t):
     max = t[0]
     max_note = t[0][1]
     for i in range(len(t)):
          if t[i][1] > max_note:
               max = t[i]
               max_note = t[i][1]
     return max[0]
def bonus_maths(t, points):
     for i in range(len(t)):
          t[i][1] += points
          if t[i][1] > 20:
               t[i][1] = 20
assert moyenne_nsi(eleves) == 13.5
assert meilleur_maths(eleves) == "Léa"
bonus_maths(eleves, 4)
assert eleves[0][1] == 18 and eleves[1][1] == 13
assert eleves[2][1] == 20 and eleves[3][1] == 15
'''
#5
'''
releve = [[12, 7, 3, 18],
[5, 21, 9, 4],
[16, 2, 11, 8]]
def somme(m):
    s = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            s += m[i][j]
    return s
def nb_pairs(m):
    c = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] % 2 == 0:
                c += 1
    return c
def position_max(m):
     a = 0
     b= 0
     c= 0
     for i in range(len(m)):
          for j in range(len(m[i])):
            if m[i][j] > a:
               a = m[i][j]
               b = j
               c = i
     tpl_final = (b, c)
     return tpl_final
def remplacer(m, ancien, nouveau):
     count = 0
     for i in range(len(m)):
          for j in range(len(m[i])):
               if m[i][j] == ancien:
                    m[i][j] = nouveau
                    count += 1
     return count
assert somme(releve) == 116
assert nb_pairs(releve) == 6
assert position_max(releve) == (1, 1)
essai = [[1, 2, 1],
[2, 1, 1]]
print(remplacer(essai, 1, 0))
assert remplacer(essai, 1, 0) == 4
assert essai == [[0, 2, 0], [2, 0, 0]]
'''
#6
'''
carre = [[2, 7, 6],
[9, 5, 1],
[4, 3, 8]]
def somme_lignes(m, i):
    s = 0
    for j in range(len(m[i])):
        s += m[i][j]
    return s
def somme_colonnes(m, j):
    s = 0
    for i in range(len(m)):
        s += m[i][j]
    return s
def somme_diagonale(m):
    s = 0
    for i in range(len(m)):
        s += m[i][i]
    return s
def somme_antidiagonale(m):
    s= 0
    for i in range(len(m)):
        s += m[i][len(m)-1-i]
    return s
def est_magique(m):
    a = None
    a = somme_lignes(m, 0) or somme_colonnes(m, 0) or somme_diagonale(m) or somme_antidiagonale(m)
    if a is None or m == [] or len(m[0]) == 2 :
        return False
    else:
        return True
print(est_magique(carre))
assert somme_lignes(carre, 0) == 15
assert somme_colonnes(carre, 2) == 15
assert somme_diagonale(carre) == 15
assert somme_antidiagonale(carre) == 15
assert est_magique(carre) == True
assert est_magique([[1, 2], [3, 4]]) == False
'''
#7
mer = [[".", "B", "B", ".", "."],
[".", ".", ".", ".", "B"],
["B", ".", ".", ".", "B"],
["B", ".", ".", ".", "B"],
[".", ".", ".", ".", "."]]