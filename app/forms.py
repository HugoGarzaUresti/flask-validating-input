from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, Regexp

class PersonForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30), Regexp('^[a-zA-Z\s]+$', message="Only letters allowed in name field")])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18)])
