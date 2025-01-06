import re

text = "The quick brown fox jumps over the lazy dog"

pattern = r"quick"
match = re.search(pattern, text)
if match:
    print(f"Found: {match.group()}")

email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails = "Contact us at john@example.com or support@company.org"
found_emails = re.findall(email_pattern, emails)
print(found_emails)

phone_pattern = r"\d{3}-\d{3}-\d{4}"
text_with_phones = "Call me at 123-456-7890 or 987-654-3210"
phones = re.findall(phone_pattern, text_with_phones)
print(phones)

text_to_clean = "Hello123World456"
cleaned = re.sub(r'\d+', '', text_to_clean)
print(cleaned)

words = re.findall(r'\w+', text)
print(words)

sentence = "apple,banana;orange:grape"
fruits = re.split(r'[,;:]', sentence)
print(fruits)
