import random

EMPATHIC_PHRASES = [
    " Ελπίζω να βοηθάει αυτό! 🌟",
    " Πες μου αν χρειαστείς κάτι άλλο! 😊",
    " Έχεις κάνει πολύ καλή δουλειά μέχρι τώρα! 💪",
    " Στο μεταξύ, θυμήθηκες να πιεις νερό σήμερα; 💧"
]

def add_empathy(text: str) -> str:
    return text + random.choice(EMPATHIC_PHRASES)