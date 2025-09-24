from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Reminder
from datetime import datetime, timedelta
from .utils import send_email_reminder
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    reminders = Reminder.query.order_by(Reminder.send_time).all()
    return render_template('index.html', reminders=reminders)

@main.route('/add', methods=['POST'])
def add_reminder():
    recipient = request.form.get('recipient')
    message = request.form.get('message')
    send_time_str = request.form.get('send_time')
    method = request.form.get('method')
    offset_str = request.form.get('timezone_offset_minutes', '0')

    if not all([recipient, message, send_time_str, method]):
        flash("All fields are required.", "error")
        return redirect(url_for('main.index'))

    try:
        offset_minutes = int(offset_str)
        local_time = datetime.fromisoformat(send_time_str)
        send_time_utc = local_time + timedelta(minutes=offset_minutes)
    except ValueError:
        flash("Invalid date/time format.", "error")
        return redirect(url_for('main.index'))

    reminder = Reminder(
        recipient=recipient,
        message=message,
        send_time=send_time_utc,
        method=method,
        sent=False
    )
    db.session.add(reminder)
    db.session.commit()

    flash("Reminder added successfully!", "success")
    return redirect(url_for('main.index'))

# TEMPORARY: Test route to verify SMTP setup
@main.route('/test-email')
def test_email():
    to_email = os.getenv("TEST_EMAIL")
    if not to_email:
        return "No TEST_EMAIL found in environment variables."

    send_email_reminder(
        to_email=to_email,
        subject="Reminder Test Email",
        body="If you're reading this, your Gmail SMTP setup works perfectly!"
    )
    return "Test email sent!"