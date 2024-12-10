import os
import config
from mistralai import Mistral

client = Mistral(api_key=config.MISTRAL_KEY)
dossier = "../7_test_unitaires/test"



def lire_fichiers_dossier(dossier):
    try:
        if not os.path.exists(dossier):
            print(f"Le dossier {dossier} n'existe pas.")
            return
        
        for fichier in os.listdir(dossier):
            chemin_fichier = os.path.join(dossier, fichier)
            
            if os.path.isfile(chemin_fichier):
                print(f"\nLecture du fichier: {fichier}")
                try:
                    contenu_final = ""
                    with open(chemin_fichier, 'r', encoding='utf-8') as f:
                        contenu = f.read()
                        contenu_final+=contenu
                        return contenu
                except Exception as e:
                    print(f"Erreur lors de la lecture du fichier {fichier}: {e}")
    except Exception as e:
        print(f"Erreur générale: {e}")
    
def ecrire_dans_fichier(nom_fichier, contenu):
    try:
        with open(nom_fichier, 'w', encoding='utf-8') as f:
            f.write(contenu)
        print(f"Contenu écrit dans le fichier {nom_fichier}")
    except Exception as e:
        print(f"Erreur lors de l'écriture dans le fichier {nom_fichier}: {e}")


content = lire_fichiers_dossier(dossier)
chat_response = client.agents.complete(
    agent_id="ag:7775c2d3:20241126:untitled-agent:bd8bf971",
    messages=[
        {
            "role": "user",
            "content": content,
        },
    ],
)
reponse_agent = chat_response.choices[0].message.content
fichier_reponse = "./reponse_agent.txt"
ecrire_dans_fichier(fichier_reponse, reponse_agent)
