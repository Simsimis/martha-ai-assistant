import json
import random
from datetime import datetime
from ..modules import empathy, clock

# Φόρτωση προσωπικότητας
with open('config/personality.json', encoding='utf-8') as f:
    PERSONALITY = json.load(f)

def handle_input(user_input: str) -> str:
    user_input = user_input.lower()
    
    # Χαιρετισμοί
    if any(word in user_input for word in ["γεια", "hello", "χαίρετε"]):
        return random.choice(PERSONALITY["responses"]["greeting"])
    
    # Ευχαριστίες
    if "ευχαριστώ" in user_input or "ευγνωμων" in user_input:
        return random.choice(PERSONALITY["responses"]["gratitude"])
    
    # Ώρα
    if "τι ωρα ειναι" in user_input or "τι ώρα είναι" in user_input:
        current_time = clock.get_time()
        return f"Η ώρα είναι {current_time} 🕒"
    
    # Προσθήκη ενσυναίσθησης σε τυχαίες απαντήσεις
    base_response = "Κατάλαβα! Θα το ψάξω γι' αυτό."
    return empathy.add_empathy(base_response)