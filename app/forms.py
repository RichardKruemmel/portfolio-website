from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me', default=False)
    submit = SubmitField("Sign In")

class AddingSkillForm(FlaskForm):
    skill = TextAreaField('Skill', validators=[DataRequired(), Length(min=1, max=10)])
    level = TextAreaField('Level', validators=[DataRequired(), Length(min=1, max=4)])
    submit = SubmitField('Submit')

class ContactForm(FlaskForm):
  name = StringField("Name", validators=[DataRequired()])
  email = StringField("Email", validators=[DataRequired(), Email()])
  subject = StringField("Subject",  validators=[DataRequired()])
  message = TextAreaField("Message",  validators=[DataRequired()])
  submit = SubmitField("Send")