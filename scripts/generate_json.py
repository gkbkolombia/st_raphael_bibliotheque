import os, json

# Dossiers à ignorer
IGNORES = {"json", "scripts", ".github"}

# Fichier de sortie
OUTPUT_DIR = "json"

# Icônes par défaut (FontAwesome)
ICONES = {
    "mathematiques": "fas fa-square-root-alt",
    "svt": "fas fa-leaf",
    "francais": "fas fa-book",
    "histoire": "fas fa-landmark",
    "geographie": "fas fa-globe",
}

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    matieres = []

    # Parcourt les dossiers dans la racine
    for dossier in os.listdir("."):
        if os.path.isdir(dossier) and dossier not in IGNORES:
            fichiers_pdf = [
                f"{dossier}/{f}" for f in os.listdir(dossier) if f.endswith(".pdf")
            ]

            if fichiers_pdf:
                titre = dossier.capitalize()
                icone = ICONES.get(dossier.lower(), "fas fa-folder")

                # Ajoute la matière
                matieres.append({
                    "id": dossier,
                    "titre": titre,
                    "icone": icone
                })

                # Sauvegarde la liste des pdfs de cette matière
                with open(f"{OUTPUT_DIR}/{dossier}.json", "w", encoding="utf-8") as f:
                    json.dump({"titre": titre, "pdfs": fichiers_pdf}, f, indent=2, ensure_ascii=False)

    # Sauvegarde la liste des matières
    with open(f"{OUTPUT_DIR}/matieres.json", "w", encoding="utf-8") as f:
        json.dump(matieres, f, indent=2, ensure_ascii=False)

    print("✅ JSON générés dans /json/")

if __name__ == "__main__":
    main()