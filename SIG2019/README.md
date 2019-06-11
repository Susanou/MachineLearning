# SIG2019 
Projet d'un chat bot pouvant à partir des paroles d'un utilisateur, donner un texte psychologique pouvant l'aider.

- [SIG2019](#sig2019)
  - [Introduction](#introduction)
    - [Overview](#overview)
    - [Utilisation](#utilisation)
      - [Environement](#environement)
      - [Instalation](#instalation)
  - [DB visualisation statistique](#db-visualisation-statistique)

---

## Introduction
### Overview
**SIG** est un projet d'intelligence artificelle (aka IA) psychologique permetant de simuler une conversation avec un psychologue. 

### Utilisation
#### Environement
**SIG** est un bot qui marche grace a de nombreux paquets; tous sont repertories dans `requirements.txt`. Cette application a ete developpee pour `python3.6` ou plus

Avant de lancer les differents scripts d'entrainemnt, il vous faut une base de donnee ainsi que creer un fichier `config.ini` avec les information suivantes:
```ini
[mysqlDB]
host = [host]
db = [DB_name]
user = [username]
pass = [password]
```

#### Instalation


## DB visualisation statistique
Sur PHPMyAdmin pour voir les mots qui sont les plus courants, aller dans la vue `plain` et chercher en fonction du theme et regler selon freq decroissante.
