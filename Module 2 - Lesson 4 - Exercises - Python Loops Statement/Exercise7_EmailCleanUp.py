# List representing email addresses, 'None' indicates an invalid email
emails = ["user1@example.com", None, "user2@example.com", "user3@example.com", None]

# List to hold valid emails
valid_emails = []

# Iterate over the list of emails
for email in emails:
    # Skip the iteration if the email is invalid
    if email is None:
        continue
    valid_emails.append(email)
print(f"Valid emails: {valid_emails}")