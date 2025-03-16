from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class ServiceAddress(FlaskForm):
    url = StringField('Введите ссылку на API', validators=[InputRequired('Обязательное поле')])
    submit = SubmitField('Отправить')
