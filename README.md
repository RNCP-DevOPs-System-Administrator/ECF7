# RNCP DevOps System Administrator
<ins>**Evaluation en cours de Formation ECF7**</ins>

#  🐳 GESTION DE CONTENEURS

## ✅ Prise en main de DOCKER
1. Installer Docker et tester l'installation avec un docker -version
2. Lister les conteneurs actifs de votre machine.
3. Lancer un conteneur test avec l'image nginx:latest avec le paramètre -p 8080:80.
- Lancer l'url 127.0.0.1/80 dans votre navigateur
- Lister les conteneurs actifs et inactifs de votre machine.
4. Supprimez l'image test et relancez-la avec les paramètre -tid -p 8080:80 .
5. Modifier le fichier html lancé par le serveur web(/usr/share/nginx/html/index.html)
Vérifier si la modification sur l'url 127.0.0.1 a bien eu lieu.
6. Entrer dans l'image avec la commande docker exec -it test increment.sh
7. Supprimer l'image.

## ✅ Construire une architecture de type micro-service
1. ⚙️ Créer une structure de fichier de type micro-service :
```
📁 myapp/
├── 📁 serveurweb/
│   └── 🐳 Dockerfile
├── 📁 worker1/
│   ├── ⚙ affichage.py
│   ├── 🐳 Dockerfile
│   └── ⚙ increment.sh
└── 📁 worker2/
    ├── ⚙ affichage.py
    ├── 🐳 Dockerfile
    └── ⚙ increment.sh
```
	
2. 🌍 Définir dans le service serveurweb
- un Dockerfile créant un conteneur Nginx avec un volume de montage persistant
- le Dockerfile devrait ressembler à :
```bash
FROM 	 nginx base latest / 
MAINTAINER you /
RUN aptget update && aptget install -y nginx /
VOLUME /var/www/html /
ENTRYPOINT [ "nginx", "-g", "daemon o_;"]
```

3. ⚙️ Implémenter un fichier shell qui incrémente une variable de 1 chaque seconde
- qui sauvegarde cette variable dans les fichiers /var/www/html/wrk1.txt et /var/www/html/wrk2.txt
- puis lance le fichier python affichage.py. 
Ce mini script que vous implémenterez lira ce fichier au format text pour modifier le fichier html du serveur web.

4. 🐳 Définissez dans les services worker1 et worker2:
- un Dockerfile créant un conteneur Ubuntu avec une gestion des fichiers de code dans le cadre d'un binding avec le volume de montage persistant du serveur web
- le Dockerfile devrait ressembler à :
```bash
FROM ubuntu latest / 
MAINTAINER you / 
COPY increment.sh / 
&& affichage.py /
RUN chmod 755 /increment.sh / 
ENTRYPOINT ["/ increment.sh"]
```

5. 🚀 Lancer les services un par un :
```bash
docker run -tid -name test serveurweb
docker run -tid -name worker1 -volumes-from test worker1 
docker run -tid -name worker2 -volumes-from test worker2
```
