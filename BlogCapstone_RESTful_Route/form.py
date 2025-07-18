from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class PostForm(FlaskForm):
    post_title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Name', validators=[DataRequired()])
    image_url = StringField('Image', validators=[URL()])
    body = CKEditorField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')

