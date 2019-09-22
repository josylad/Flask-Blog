from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, TextField, SelectField, widgets
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
from flask_login import current_user
from flask_ckeditor import CKEditor, CKEditorField


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=10)])
    content = TextAreaField('Content', validators=[DataRequired()])
    image = FileField('Featured Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    category = StringField('Category', validators=[DataRequired()])
    submit = SubmitField('Publish')
    
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Submit')