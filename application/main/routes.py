from flask import Blueprint, render_template, flash, request, abort, redirect, url_for
from application.models import Post, SubscribedUser
from application.main.utils import send_confirmation_email, send_everyone_email, send_test_email
from flask_login import current_user, login_required
from application.database import db
from application.main.forms import SubscriptionEmailForm

main = Blueprint("main", __name__)

@main.route('/')
@main.route('/home')
def home():
	page = request.args.get("page", 1, type=int)
	posts = Post.query.filter_by(draft=0).order_by(Post.date_posted.desc()).paginate(page=page, per_page=9)

	return render_template("home.html", posts=posts)

@main.route('/about')
def about():
    return render_template("about.html", title="About")

@main.route("/email_confirm", methods=['POST'])
def email_confirm():
	email_data = request.form["email"]
	name_data = request.form["name"]

	user = SubscribedUser(name=name_data, email=email_data)
	db.session.add(user)
	db.session.commit()
	send_confirmation_email(name=name_data, email=email_data)
	return ""

@main.route("/send_subscribers_email", methods=["GET", "POST"])
@login_required
def send_subscribers_email():
	if current_user.role != "Admin":
		abort(403)

	form = SubscriptionEmailForm()
	if form.validate_on_submit():
		all_users = SubscribedUser.query.all()

		subject = form.subject.data
		content = form.content.data

		if form.test.data: #if sending test email
			send_test_email(subject=subject, content=content)
		else: #if sending real email
			recipients = [user.email for user in all_users]
			send_everyone_email(subject=subject, content=content, recipients=recipients)
		return redirect(url_for("main.home"))
	return render_template("send_subscribers_email.html", form=form)