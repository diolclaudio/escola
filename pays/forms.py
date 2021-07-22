from django import forms
from .models import Pagar, Comentario, Inscricoes

class PagarForm(forms.ModelForm):

    class Meta:
        model = Pagar
        fields = ['classe', 'nome','valor', 'mes', 'email']

class InscricoesForm(forms.ModelForm):

    class Meta:
        model= Inscricoes
        fields = ['nome', 'valor', 'curso', 'email', 'numero']

class ComentarioForm(forms.ModelForm):

    class Meta:
        model= Comentario
        fields = ['opiniao']