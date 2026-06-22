from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completada', 'categoria', 'prioridad']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})