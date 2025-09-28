import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    pattern = r'^\+?1?[-.\s]?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})$'
    return re.match(pattern, phone) is not None

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit"
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character"
    return True, "Password is valid"

def extract_urls(text):
    pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.findall(pattern, text)

def clean_html_tags(html):
    pattern = r'<[^>]+>'
    return re.sub(pattern, '', html)

test_emails = ["user@example.com", "invalid-email", "test@domain.co.uk"]
for email in test_emails:
    print(f"{email}: {validate_email(email)}")

test_phones = ["123-456-7890", "(555) 123-4567", "invalid-phone"]
for phone in test_phones:
    print(f"{phone}: {validate_phone(phone)}")

test_password = "MyPass123!"
valid, message = validate_password(test_password)
print(f"Password '{test_password}': {message}")

text_with_urls = "Visit https://www.example.com or http://test.org for more info"
urls = extract_urls(text_with_urls)
print(f"URLs found: {urls}")

html_content = "<p>This is <b>bold</b> and <i>italic</i> text.</p>"
clean_text = clean_html_tags(html_content)
print(f"Clean text: {clean_text}")
