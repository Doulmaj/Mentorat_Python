import json


def dump_database() -> None:
    content:list|dict = None    #type:ignore

    print("1. Extraction des données de la base")
    try:
        with open("ressources.json", "r", encoding="utf-8") as document:
            print("---> Fichier trouvé")
            print("---> Extraction des données")
            content = json.load(document)
        print("---> Extraction des données terminée")
    except FileNotFoundError as e:
        print("\t<-- Fichier non trouvé -->")
        return
    except Exception as e:
        print("\t<-- Erreur survenue lors de la lecture des données -->")
        print(repr(e))
        return

    print("\n2. Ecriture des données dans la base")
    try:
        with open("ressources.json", "w") as document:
            print("---> Fichier trouvé ou créé")
            print("---> Ecriture des données")
            json.dump(content, document, indent = 4)
        print("---> Ecriture des données terminée")
    except Exception as e:
        print("\t<-- Erreur lors de l'écriture des données -->")
        print(repr(e))
        return

    print("\n<---> Opération effectuée avec succès ! <--->\n")


if __name__ == "__main__":
    dump_database()