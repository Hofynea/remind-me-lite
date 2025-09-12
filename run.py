from app import create_app
from app.utils import send_email_reminder

app = create_app()

# Testind to send an email
send_email_reminder(
    to_email="yourtestemail@gmail.com",
    subject="Reminder Test",
    body="If you're seeing this, your reminder app works!"
)

if __name__ == "__main__":
    app.run(debug=True)
