from app import create_app, db
from app.utils import send_email_reminder

app = create_app()

# Testind to send an email
send_email_reminder(
    to_email="ads959039@gmail.com",
    subject="Reminder Test",
    body="If you're seeing this, your reminder app works!"
)

with app.app_context():
    db.create_all()
    
if __name__ == "__main__":
    app.run(debug=True)
