from django import forms
from catalog.models import Product
from django.core.exceptions import ValidationError


FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите описание'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену'})

    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        name_lower = name.lower()
        for word in FORBIDDEN_WORDS:
            if word in name_lower:
                self.add_error('name', f'В названии запрещено использовать слово «{word}».')

        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        description_lower = description.lower()
        for word in FORBIDDEN_WORDS:
            if word in description_lower:
                self.add_error('description', f'В описании запрещено использовать слово «{word}».')

        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price is not None and price <= 0:
            raise forms.ValidationError('Цена не может быть отрицательной.')

        return price
