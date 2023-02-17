import subprocess
import json

def get_sirene_data(siret):
    # Construire la commande CURL à exécuter
    curl_command = f"curl -X GET --header 'Accept: application/json' --header 'Authorization: Bearer d903a44d-974c-3867-b4d5-f6749631fd63' 'https://api.insee.fr/entreprises/sirene/V3/siret/{siret}'"
    
    # Exécuter la commande CURL et récupérer la sortie JSON
    result = subprocess.check_output(curl_command, shell=True)
    
    # Charger les données JSON dans un objet Python
    data = json.loads(result.decode("utf-8"))
    
    return data
