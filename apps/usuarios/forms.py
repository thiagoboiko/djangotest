from django import forms

class LoginForms(forms.Form):
    nome=forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Evento de integração de calouros."
            }
        )
    )
    descricao=forms.CharField(
        label="Descrição",
        required=True,
        max_length=250,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Descreva o evento."
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Thiago Boiko"
            }
        )
    )
    email=forms.CharField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: thiago.boiko@boiko.com"
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua senha"
            }
        )
    )
    senha2=forms.CharField(
        label="Senha2",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirme a sua senha"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome
    
    def clean_senha2(self):
        senha = self.cleaned_data.get('senha')
        senha2 = self.cleaned_data.get('senha2')
        
        if senha and senha2:
            if senha == senha2:
                return senha
            else:
                raise forms.ValidationError('As senhas precisam ser iguais.')