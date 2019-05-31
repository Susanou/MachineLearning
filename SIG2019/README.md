# SIG2019 
Projet d'un chat bot pouvant à partir des paroles d'un utilisateur, donner un texte psychologiaque pouvant l'aider.

## Requirements
No pip requirements.

Create a `config.ini` file in the same repository with the following information:
```ini
[mysqlDB]
host = [host]
db = [DB_name]
user = [username]
pass = [password]
```

## How to run?
First add execution permissions to the file

```bash
chmod +x reader.py
```

Then use it as follows
```bash
./reader.py <inputTextFile> <ThemeName>
```

## [fonctions.py](fonctions.py)
Fichier contenant toutes les fonctions utilisées pour ce projet.

## [reader.py](reader.py)
Script python à exécuter.

## DB visualisation statistique
Sur PHPMyAdmin pour voir les mots qui sont les plus courants, aller dans la vue `plain` et chercher en fonction du theme et regler selon freq decroissante.
