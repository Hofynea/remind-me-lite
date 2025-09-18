import time
from datetime import datetime
from app.models import db, Reminder
from app.utils import send_email_reminder
from app import create_app

app = create_app()
app.app_context().push()

def process_reminders():
    while True:
        print("Checking for due reminders...")
        now = datetime.now()
        due_reminders = Reminder.query.filter_by(sent=False).filter(Reminder.send_time <= now).all()

        for reminder in due_reminders:
            if reminder.method == 'email':
                send_email_reminder(
                    to_email=reminder.recipient,
                    subject="Reminder: Your Task is Due",
                    body=reminder.message
                )
                reminder.sent = True
                db.session.commit()
                print(f"Sent reminder to {reminder.recipient}")

        time.sleep(60)  # check every 60 seconds

if __name__ == "__main__":
    process_reminders()