wrk_path = "/var/www/html/wrk1.txt"         # fichier contenant le compteur de worker1
output_path = "/var/www/html/index.html"    # fichier HTML généré que Nginx 

def read_count(path):
    try:
        with open(path, "r") as f:          # ouvre le fichier en lecture
            return f.read().strip()         # lit tout le contenu du fichier et enlève les espaces ou retours à la ligne
    except:                                 # si le fichier n’existe pas ou si une erreur se produit, on retourne "N/A"
        return "N/A"

count = read_count(wrk_path)                # Lecture du compteurs du worker, et on le stocke dans la variable count

with open(output_path, "w") as f:           # Ouverture du fichier index.html en écriture ("w")
    f.write(f"""
    <html>
    <head><title>Worker 1 Status</title></head>
    <body>
        <h1>Worker 1 Count: {count}</h1>
    </body>
    </html>
    """)