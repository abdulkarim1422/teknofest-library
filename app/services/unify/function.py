from difflib import get_close_matches
import unicodedata

# Function to remove accents and normalize non-Latin characters
def normalize_text(text):
    text = text.lower()
    text = unicodedata.normalize("NFKD", text)  # Normalize accented characters
    return "".join(c for c in text if not unicodedata.combining(c))  # Remove diacritics

def find_original_sentence(sentence, groups, threshold=0.5):
    lookup = {}
    all_phrases = []
    
    for group in groups:
        original = group[0]  # First element is the original
        for phrase in group:
            normalized = normalize_text(phrase)
            lookup[normalized] = original
            all_phrases.append(normalized)

    normalized_input = normalize_text(sentence)
    
    # Try exact match first
    if normalized_input in lookup:
        return lookup[normalized_input]
    
    # Try fuzzy matching
    close_matches = get_close_matches(normalized_input, all_phrases, n=1, cutoff=threshold)
    
    if close_matches:
        return lookup[close_matches[0]]  # Return original key
    
    return None  # No match found