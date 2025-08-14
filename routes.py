from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from extensions import db
from models import Attendee
from forms import AttendeeForm

main = Blueprint("main", __name__)

# Home page - list attendees
@main.route("/")
def index():
    attendees = Attendee.query.all()
    return render_template("index.html", attendees=attendees)

# Add attendee
@main.route("/add", methods=["GET", "POST"])
def add_attendee():
    form = AttendeeForm()
    if form.validate_on_submit():
        attendee = Attendee(
            name=form.name.data,
            email=form.email.data,
            event_name=form.event_name.data
        )
        db.session.add(attendee)
        db.session.commit()
        flash("Attendee registered successfully!", "success")
        return redirect(url_for("main.index"))
    return render_template("attendee_form.html", form=form, title="Register Attendee")

# Edit attendee
@main.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_attendee(id):
    attendee = Attendee.query.get_or_404(id)
    form = AttendeeForm(obj=attendee)
    if form.validate_on_submit():
        form.populate_obj(attendee)
        db.session.commit()
        flash("Attendee updated successfully!", "success")
        return redirect(url_for("main.index"))
    return render_template("attendee_form.html", form=form, title="Edit Attendee")

# Delete attendee
@main.route("/delete/<int:id>")
def delete_attendee(id):
    attendee = Attendee.query.get_or_404(id)
    db.session.delete(attendee)
    db.session.commit()
    flash("Attendee deleted successfully!", "success")
    return redirect(url_for("main.index"))

# Optional API for Postman testing
@main.route("/api/attendees", methods=["GET"])
def api_attendees():
    attendees = Attendee.query.all()
    return jsonify([{"id": a.id, "name": a.name, "email": a.email, "event_name": a.event_name} for a in attendees])
