import spacy
from collections import defaultdict

# Load small English model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = defaultdict(list)
    for ent in doc.ents:
        entities[ent.label_].append(ent.text)

    # Optional: Only keep relevant entity types
    desired = ["PERSON", "ORG", "DATE", "MONEY", "GPE", "LOC", "TIME", "PERCENT"]
    return {k: v for k, v in entities.items() if k in desired}
