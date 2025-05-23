#!/bin/bash

# fichier : increment.sh
COUNT=0				# Cette variable va servir de compteur incrémenté à chaque seconde
FILE="/var/www/html/wrk1.txt" 	# Destination où on écrit la valeur du compteur

while true; do 			# Boucle infinie qui va tourner sans arrêt (jusqu’à interruption)
  echo $COUNT > $FILE 		# Écrit la valeur actuelle du compteur dans le fichier cible
  COUNT=$((COUNT + 1))		# Incrémente la variable COUNT de 1
  sleep 1			# Pause de 1 seconde avant de répéter la boucle
  python3 /affichage.py		# Mise à jour du fichier HTML Nginx (index.html) avec les valeurs de wrk1.txt
done
