testFile = open("corpus/corpus2test.txt", "r")
passwordFile = open("generated_passwords/passwords.txt", "r")

testPasswords = testFile.read().split("\n")
generatedPasswords = passwordFile.read().split("\n")

#On calcule l'intersection entre les mots de passe générés et ceux du corpus de test
inter = set(generatedPasswords).intersection(testPasswords)
print("Mots de passe trouves : ")
#for i in inter:
#	print(i)

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
