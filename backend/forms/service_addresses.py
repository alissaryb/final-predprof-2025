from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class FormAddGroups(FlaskForm):
    url = StringField('URL', validators=[InputRequired('Обязательное поле')])
    submit = SubmitField('Отправить')
