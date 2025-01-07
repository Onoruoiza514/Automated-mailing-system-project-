import time
import requests

# Constants
API_BASE_URL = "https://api.gohighlevel.com/v1"
API_KEY = "*******************"  #Emcrypted for security purposes 
BATCH_SIZE = 100
BATCH_DELAY = 5  # Delay in seconds between batches

# Fetch all active contacts from GoHighLevel
def fetch_contacts():
    url = f"{API_BASE_URL}/contacts"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {"status": "active"}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    contacts = response.json().get("contacts", [])
    return [contact for contact in contacts if contact.get("email")]

# Send bulk emails in batches
def send_bulk_emails(contacts, email_template):
    for i in range(0, len(contacts), BATCH_SIZE):
        batch = contacts[i:i + BATCH_SIZE]
        
        for contact in batch:
            send_email(contact, email_template) #We'll create a helper send email function below

        print(f"Batch {i // BATCH_SIZE + 1} sent. Waiting {BATCH_DELAY} seconds before next batch...")
        time.sleep(BATCH_DELAY)

# Send a single email
def send_email(contact, email_template):
    url = f"{API_BASE_URL}/emails/send"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    # Replace template variables with contact data
    email_body = email_template.format(
        first_name=contact.get("firstName", ""),
        last_name=contact.get("lastName", ""),
        email=contact.get("email", "")
    )

    payload = {
        "to": contact["email"],
        "subject": "Your Subject Here",
        "body": email_body
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"Email sent to {contact['email']}")
    else:
        print(f"Failed to send email to {contact['email']}: {response.text}")

# Main execution block
def main():
    email_template = """
    Hi {first_name},

    This is a bulk email sent using the GoHighLevel Api,we hope this message finds you we'll 
    we'll contact you shortly..............

    Best regards,
    abdulfaatih
    """

    print("Fetching contacts...")
    contacts = fetch_contacts()
    print(f"Total active contacts: {len(contacts)}")

    print("Starting bulk email campaign...")
    send_bulk_emails(contacts, email_template)

    print("Bulk email campaign completed.")

if __name__ == "__main__":
    main()
  
