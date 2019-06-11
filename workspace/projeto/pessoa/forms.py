from django import forms
from .models import PessoaModel
from django.contrib.admin import widgets

class PessoaForm(forms.ModelForm):
    pessoa_nome = forms.CharField(required=True, label="Nome")
    pessoa_logradouro = forms.CharField(required=True, label="Logradouro")
    pessoa_numero = forms.CharField(required=True, label="Numero")
    pessoa_data_nascimento = forms.DateField(required=True, label="Data Nascimento")

    class Meta:
        model = PessoaModel
        fields = [
            'pessoa_nome',
            'pessoa_logradouro',
            'pessoa_numero',
            'pessoa_data_nascimento'
        ]
        widgets = {
            'pessoa_data_nascimento':forms.DateInput(attrs={'class':'js-date'})
        }
        
    class ContatoForm(forms.ModelForm):
        
        contato_telefone = forms.CharField(label="Telefone")
        pessoa = forms.ModelChoiceField(queryset=PessoaModel.objects.all(), label="Contato")    
    