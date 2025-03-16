from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, DataRequired, ValidationError, Length, Regexp


class FormUrl(FlaskForm):
    url = StringField('Введите ссылку на API', validators=[DataRequired('Обязательное поле')])

    submit = SubmitField('Отправить')
