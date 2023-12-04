import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
import streamlit as st
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# Chargez le fichier texte et prétraitez les données
with open('homme_oreille.txt', 'r', encoding='utf-8') as fichier:
    data = fichier.read().replace('\n', ' ')
# Tokeniser le texte en phrases
#sentences = sent_tokenize(data)
# Définir une fonction pour prétraiter chaque phrase
def preprocess(sentence):
    # Tokeniser la phrase en mots
    words = word_tokenize(sentence)
    # Supprimer les mots vides et la ponctuation
    words = [word.lower() for word in words if word.lower() not in stopwords.words('french') and word not in string.punctuation]
    # Lemmatiser les mots
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return words

# Prétraitez chaque phrase du texte
corpus = [preprocess(sentence) for sentence in sentences]

# Définir une fonction pour trouver la phrase la plus pertinente compte tenu d'une requête
def get_most_relevant_sentence(query):
    # Prétraiter la requête
    query = preprocess(query)
    # Calculer la similarité entre la requête et chaque phrase du texte
    max_similarity = 0
    most_relevant_sentence = ""
    for sentence in corpus:
        similarity = len(set(query).intersection(sentence)) / float(len(set(query).union(sentence)))
        if similarity > max_similarity:
            max_similarity = similarity
            most_relevant_sentence = " ".join(sentence)
    return most_relevant_sentence

def chatbot(question):
    # Trouvez la phrase la plus pertinente
    most_relevant_sentence = get_most_relevant_sentence(question)
    # Retourne la réponse
    return most_relevant_sentence

# Créer l'application Streamlit
def main():
    st.title("LE CHATBOT A VOTRE SERVICE")
    st.write("Bonjour bienvenue! pourrais-je  vous aider?")
    # Obtenez la question de l'utilisateur
    question = st.text_input("Vous:")
    # Créez un bouton pour soumettre la question
    if st.button("Submit"):
        # Appelez la fonction chatbot avec la question et affichez la réponse
        response = chatbot(question)
        st.write("retour Chatbot: " + response)
if __name__ == "__main__":
    main()
