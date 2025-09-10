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
    send_time = request.form.get('send_time')
    method = request.form.get('method')

    if not recipient or not message or not send_time or not method:
        flash("All fields are required!", "error")
        return redirect(url_for('main.index'))

    try:
        send_time = datetime.strptime(send_time, "%Y-%m-%dT%H:%M")
    except ValueError:
        flash("Invalid date/time format", "error")
        return redirect(url_for('main.index'))

    reminder = Reminder(
        recipient=recipient,
        message=message,
        send_time=send_time,
        method=method
    )
    db.session.add(reminder)
    db.session.commit()

    flash("Reminder added!", "success")
    return redirect(url_for('main.index'))
