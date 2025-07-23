from StateGraph.nodes_def import classify_ticket

def test_classification_billing():
    ticket = {
        "subject": "Refund issue",
        "description": "I didn't get my refund for a canceled subscription."
    }
    result = classify_ticket(ticket)
    print("Classification result:", result)
    assert result == "Billing"

def test_classification_technical():
    ticket = {
        "subject": "App crash",
        "description": "The app crashes every time I try to upload a file."
    }
    result = classify_ticket(ticket)
    print("Classification result:", result)
    assert result == "Technical"

def test_classification_account():
    ticket = {
        "subject": "Password reset",
        "description": "I can't reset my password using the link provided."
    }
    result = classify_ticket(ticket)
    print("Classification result:", result)
    assert result == "Account"

def test_classification_general():
    ticket = {
        "subject": "Other inquiry",
        "description": "I have a question about your company."
    }
    result = classify_ticket(ticket)
    print("Classification result:", result)
    assert result == "General"



test_classification_general()