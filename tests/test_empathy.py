from src.modules.empathy import add_empathy

def test_empathy():
    base_text = "Ολοκληρώθηκε η εργασία."
    result = add_empathy(base_text)
    assert len(result) > len(base_text)
    assert any(emoji in result for emoji in ["🌟", "😊", "💪", "💧"])
    print("✅ test_empathy passed!")

test_empathy()