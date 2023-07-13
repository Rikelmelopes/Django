from django import forms
from cars.models import Car


    
class CarModelForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):#Validação de campo
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor minimo do carro deve ser de R$20.000')
        return value   
    
    def clean_factore_year(self):
        factore_year = self.cleaned_data.get('factore_year')
        if factore_year < 1975:
            self.add_error('factore_year', 'Ano minimo para cadastro é 1975' ) 
        return factore_year      