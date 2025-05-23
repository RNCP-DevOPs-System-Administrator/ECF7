### Construire une architecture de type micro-service
1 - Créer une structure de fichier de type micro-service :
myapp/
├── serveurweb/
│   └── Dockerfile
├── worker1/
│   ├── affichage.py
│   ├── Dockerfile
│   └── increment.sh
└── worker2/
    ├── affichage.py
    ├── Dockerfile
    └── increment.sh
	
2 – Définissez dans le service serveurweb, un Dockerfile créant un conteneur Nginx avec un volume de montage persistant, le dockerfile devrait ressembler à :
FROM 	 nginx base latest / 
MAINTAINER you /
RUN aptget update && aptget install -y nginx /
VOLUME /var/www/html /
ENTRYPOINT [ "nginx", "-g", "daemon o_;"]

3 - Implémenter un fichier shell qui incrémente une variable de 1 chaque seconde et qui sauvegarde cette variable dans les fichiers /var/www/html/wrk1.txt et /var/www/html/wrk2.txt puis lance le fichier python affichage.py. 
Ce mini script que vous implémenterez lira ce fichier au format text pour modifier le fichier html du serveur web.

4 - Définissez dans les services worker1 et worker2, un Dockerfile créant un conteneur Ubuntu avec une gestion des fichiers de code dans le cadre d'un binding avec le volume de montage persistant du serveur web, le dockerfile devrait ressembler à :
FROM ubuntu latest / 
MAINTAINER you / 
COPY increment.sh / 
&& affichage.py /
RUN chmod 755 /increment.sh / 
ENTRYPOINT ["/ increment.sh"]

5 - Lancer les services un par un :
docker run -tid -name toto serveurweb
docker run -tid -name worker1 -volumes-from toto worker1 
docker run -tid -name worker2 -volumes-from toto worker2
