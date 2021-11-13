def multiply(m1, m2):
    result = []
    if(len(m1[0]) != len(m2)):
        return "Ces matrices ne sont pas multipliables car les colonnes de la 1ere matrice sont différentes aux lignes de la 2eme"
    for i in range (len(m1)):
        row = []
        for j in range (len((m2)[0])):
            element = 0
            for k in range (len(m1[0])):
                element = element + m1[i][k] * m2[k][j]
            row.append(element)
        result.append(row)
    return result