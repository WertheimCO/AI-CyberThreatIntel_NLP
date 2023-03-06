import requests
import spacy
from spacy.lang.en import English

# Initialize NLP model
nlp = spacy.load('en_core_web_sm')
parser = English()

# Retrieve text data from a web page
def get_text(url):
    r = requests.get(url)
    return r.text

# Extract entities from text using NLP
def extract_entities(text):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append({'text': ent.text, 'label': ent.label_})
    return entities

# Main function to process threat intelligence
def process_threat_intelligence(url):
    text = get_text(url)
    entities = extract_entities(text)
    print('Entities found in threat intelligence:')
    print(entities)

# Example usage
process_threat_intelligence('https://www.example.com/threat-intelligence')
