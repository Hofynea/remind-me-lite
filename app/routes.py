from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Reminder
from datetime import datetime

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

    if not all([recipient, message, send_time_str, method]):
        flash("All fields are required.", "error")
        return redirect(url_for('main.index'))

    try:
        send_time = datetime.fromisoformat(send_time_str)
    except ValueError:
        flash("Invalid date/time format.", "error")
        return redirect(url_for('main.index'))

    reminder = Reminder(
        recipient=recipient,
        message=message,
        send_time=send_time,
        method=method,
        sent=False
    )
    db.session.add(reminder)
    db.session.commit()

    flash("Reminder added successfully!", "success")
    return redirect(url_for('main.index'))
