import re 
def filter_valid_emails(emails): 
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 
    return [email for email in emails if re.match(pattern, email)] 
emails = ["user@example.com", "invalid-email", "admin@domain.org", "test@com"] 
print(filter_valid_emails(emails)) 