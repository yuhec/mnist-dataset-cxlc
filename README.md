# mnist-dataset-cxlc
Source for https://algorithmia.com/algorithms/laetitia/mnistDataset


 Ce que vous avez fait, où vous en êtes (code, tests, etc.)
* Problématiques et difficultés rencontrées. Lesquelles avez-vous résolues, comment? Sont-elles liées au déploiement sur plateforme cloud en général, ou spécifiquement à Algorithmia?
* Ce qu’il reste à faire: pistes à suivre pour résoudre problème en cours, idées, tâches à accomplir pour obtenir une API qu’on pourrait mettre dans les mains d’un utilisateur final, améliorations possibles
* Ce que vous avez appris via ce projet

# Progression 

Repo github associé à Algorithmia et DeepNote 
Créer un modèle avec autoKeras, l'entrainer, le sauvegarder et le charger depuis un fichier ".h5"
Faire une prédiction depuis un modèle chargé
Fonction apply qui fait une prédiction avec le modèle chargé et l'image en input
Travail en pair programming avec DeepNote et partage d'écran pour la partie Algorithmia


# Difficultés rencontrées

Problème -> Prise en main de l'interface d'Algorithmia, erreurs type "Algorithm process exited" (assez vaste à cerner le problème)
soucis pour load le model, résultat non satisfaisant (return null ou 'Object of type float32 is not JSON serializable')
Une horreur à debugger depuis Algorithmia. On est obligé de mettre à jour le git puis algorithmiadoit build et on perd 5 à 10 min à chaque fois ...


# Pour aller plus loin

Fixer l'output -> n'arrive pas à resize l'image car l'image est considérée comme vide, surement un soucis de l'input

Idée d'amélioration :
- passer un tableau d'image ou un objet au lieu d'un string (path)


# Compétences acquises

Initiation à Algorithmia, travail en groupe, création d'une API dans le cloud, notion de serverless