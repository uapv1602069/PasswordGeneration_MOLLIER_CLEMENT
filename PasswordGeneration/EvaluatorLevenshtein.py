from array import array

#source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
def ld(a, b, mx=-1):	
    def result(d): return d if mx < 0 else False if d > mx else True
 
    if a == b: return result(0)
    la, lb = len(a), len(b)
    if mx >= 0 and abs(la - lb) > mx: return result(mx+1)
    if la == 0: return result(lb)
    if lb == 0: return result(la)
    if lb > la: a, b, la, lb = b, a, lb, la
 
    cost = array('i', range(lb + 1))
    for i in range(1, la + 1):
        cost[0] = i; ls = i-1; mn = ls
        for j in range(1, lb + 1):
            ls, act = cost[j], ls + int(a[i-1] != b[j-1])
            cost[j] = min(ls+1, cost[j-1]+1, act)
            if (ls < mn): mn = ls
        if mx >= 0 and mn > mx: return result(mx+1)
    if mx >= 0 and cost[lb] > mx: return result(mx+1)
    return result(cost[lb])

testFile = open("corpus/corpus4.txt", "r")
passwordFile = open("generated_passwords/passwords.txt", "r")

testPasswords = testFile.read().split("\n")
testPasswords = testPasswords[0:100]
generatedPasswords = passwordFile.read().split("\n")
inter = []

#Si la distance de levenshtein est inférieure à 2, on ajout le mot de passe à l'intersection
for test in testPasswords:
	print("testing : " + test)
	for gen in generatedPasswords:
		if ld(test, gen, mx=2) == True:
			print(gen)
			inter.append(test)
			break
			
print("Nombre de mots de passe generes : ")
print(len(generatedPasswords))
print("Nombre de mots de passe testes : ")
print(len(testPasswords))
print("Nombre de mots de passe trouves : ")
print(len(inter))
print("Pourcentage de couverture : ")
coverage = len(inter)/len(testPasswords)
print(coverage)

testFile.close()
passwordFile.close()
		