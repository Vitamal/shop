from django import forms
from django.core.exceptions import ValidationError


def validate_file_format(data):
    if data.name.split('.')[-1] != 'csv':
        raise ValidationError("The format of the file is invalid, must be a valid 'csv' file")


class UploadFileForm(forms.Form):
    file = forms.FileField(validators=[validate_file_format])
