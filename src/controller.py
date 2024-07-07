from models import *
from views import load_data

def clean_data(data):
    """
    Cette fonction nettoie les données en supprimant les données manquantes et les doublons.
    
    Parameters:
    donnees (list of dict): Liste de dictionnaires représentant les données.
    
    Returns:
    list of dict: Liste de dictionnaires nettoyée.
    
    """
    
    # Afficher le nombre de lignes avant le nettoyage
    print(f"Nombre de lignes avant nettoyage: {len(data)}")
    
    # Supprimer les données manquantes
    cleaned_data = [
        ligne for ligne in data 
        if all(valeur != '' and valeur is not None for valeur in ligne.values())
    ]
    
    # Afficher le nombre de lignes après suppression des données manquantes
    print(f"Nombre de lignes après suppression des données manquantes: {len(cleaned_data)}")
    
    # Supprimer les doublons
    cleaned_data = list({tuple(ligne.items()): ligne for ligne in cleaned_data}.values())
    
    # Afficher le nombre de lignes après suppression des doublons
    print(f"Nombre de lignes après suppression des doublons: {len(cleaned_data)}, {len(cleaned_data[0].keys())}")
    
    return cleaned_data

def verify():
    Commercial_Aviation = load_data('./src/dataset/Commercial_Aviation.csv')
    transport = load_data('./src/dataset/transport.csv')
    Covid_19 = load_data('./src/dataset/COVID-19_Outcomes_by_Vaccination.csv')

    print("Jeu de données Commercial_Aviation")
    if missing_data(Commercial_Aviation):
        print(f"Il y a des données manquantes dans le fichier sur le Commercial_Aviation.csv \n")
        data1 = clean_data(Commercial_Aviation)
    else:
        print(f"Il n'y a pas de données manquantes dans le fichier sur le Commercial_Aviation.csv.\n")
        data1 = Commercial_Aviation

    print("Jeu de données transport")
    if missing_data(transport):
        print(f"Il y a des données manquantes dans le fichier transport.csv\n")
        data2 = clean_data(transport)
    else:
        print(f"Il n'y a pas de données manquantes dans le fichier sur transport.csv\n")
        data2 = transport

    print("Jeu de données Covid_19")
    if missing_data(Covid_19):
        print(f"Il y a des données manquantes dans le fichier sur Covid_19.csv\n")
        data3 = clean_data(Covid_19)
    else:
        print(f"Il n'y a pas de données manquantes dans le fichier sur Covid_19.csv\n")
        data3 = Covid_19

    return [data1, data2, data3]
    
