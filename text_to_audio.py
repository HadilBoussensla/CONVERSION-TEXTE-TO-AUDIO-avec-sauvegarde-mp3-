#bibliothèque à installer 
pip install gtts

from gtts import gTTS
import os

# Fonction pour convertir texte en audio avec gTTS
def text_to_audio(text):
    # Créer un objet gTTS pour la conversion du texte en audio
    tts = gTTS(text=text, lang='fr')
    # Sauvegarder et lire le fichier audio immédiatement
    tts.save("audio_output.mp3")
    os.system("mpg321 audio_output.mp3")  # Lire l'audio avec mpg321 (ou une autre commande selon ton système)
    print("Le texte a été converti en audio et joué immédiatement.")

# Exemple d'utilisation
user_text = input("Entrez le texte que vous voulez transformer en audio : ")

# Convertir le texte en audio et le lire
text_to_audio(user_text)
  
