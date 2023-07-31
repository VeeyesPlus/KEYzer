import spacy

def load_spacy_model():
    model_path = "path to spacy_models/en_core_web_sm"
    nlp = spacy.load(model_path)
    return nlp
