from langchain.prompts import PromptTemplate  

classify_prompt = PromptTemplate(
    input_variables=["subject", "description"],
    template="""You are a customer support classifier. Classify the following support ticket into **one** of the following categories:

- **Billing**: Issues related to payments, refunds, charges, invoices, or subscriptions.
- **Technical**: Bugs, crashes, login errors, performance issues, or software malfunctions.
- **Security**: Account breaches, password reset requests, suspicious activity, or data protection concerns.
- **General**: Questions, feedback, feature inquiries, or anything not fitting the other categories.

Return the classification as a valid JSON object **only**, in this format:
{{"category": "<Billing|Technical|Security|General>"}}

Ticket Subject: {subject}
Ticket Description: {description}

Example:
{{"category": "Technical"}}

Only respond with the JSON object. No explanation."""
)

draft_prompt = PromptTemplate(
    input_variables=["subject", "description", "context"],
    template="""Generate a professional and polite response for the following support ticket using the provided context. Ensure the response is clear, addresses the issue, and is suitable for customer communication. Mention JSON in the context of structured data to ensure compatibility. Return the response as a plain text string.

Ticket Subject: {subject}
Ticket Description: {description}
Context: {context}

Example response: Dear Customer,\nThank you for reaching out. [Address issue based on context]. Please let us know if you need further assistance.\nBest regards,\nSupport Team"""
)

review_prompt = PromptTemplate(
    input_variables=["draft", "subject", "description"],
    template="""Review the following draft reply to a support ticket. Check for clarity, professionalism, and relevance. Return a JSON object like:

{{"pass": true, "feedback": "The draft is clear and professional."}}

Ticket Subject: {subject}
Ticket Description: {description}
Draft: {draft}

Only return the JSON. Do not include code formatting or explanation."""
)