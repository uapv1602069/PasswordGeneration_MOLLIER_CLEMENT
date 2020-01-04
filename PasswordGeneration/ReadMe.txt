##########
# README #
##########

--- Architecture du projet ---

corpus: Contient les différents corpus utilisés et générés
figures: Contient les différentes figures générées. Le nom du sous dossier correspond au nom du fichier à partir duquel les graphes ont été générés
generated_passwords: Contient les mots de passe générés
improvements: Contient le modèle entraîné
logs: Contient les logs Tensorflow. Voir suite pour les consulter.

--- Utilisation des scripts ---

Analyzer.py :
Nécessite un argument correspondant au nom du corpus sans l'extension (ex: python Analyzer.py corpus2)
Cela va générer les différents graphes dans le dossier figures pour le corpus donné en paramètre

Evaluator.py :
Evalue la couverture du "corpus2test.txt" par les mots de passe générés "passwords.txt".
Il est nécessaire d'éditer le script pour évaluer sur des corpus différents (simplement changer open("corpus/corpus2test.txt")
Afin d'afficher les mots de passe trouver, il faut enlever les commentaires aux lignes 10 et 11.

EvaluatorLevenshtein.py :
Même fonctionnement que Evaluator.py

GeneratorLSTN.py
Nécessite qu'un apprentissage ait été fait avec LSTN.py. En effet, il va charger le modèle du dossier improvements.
Les mots de passe générés se trouveront dans le dossier generated_passwords ("passwords.txt"). La génération peut être très longue

GeneratorRAND.py
Génère des mots de passe aléatoires dans le fichier "passwordsRand.txt"

LSTN.py
Lance l'apprentissage à partir du "corpus2train.txt". Pour changer de corpus, il est nécessaire d'éditer la ligne 11.

shuffler.py
Ouvre le fichier "corpus2.txt" et crée le fichier "corpus2shuffled.txt" qui correspond au même corpus mais mélangé.

--- Affichage des logs TensorBoard ---

Depuis la racine du projet, executer la commande:
tensorboard --logdir logs
Puis aller à l'addresse indiquée dans la console.