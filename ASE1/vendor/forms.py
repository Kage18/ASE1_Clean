from django import forms
from vendor.models import Product, Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductsAdd(forms.ModelForm):
    quantity = forms.IntegerField()

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['qty']

    # def clean(self):
    #     cleaned_data = super().clean()
    #
    #     count = Product.objects.filter(prod_name=product['prod_name'])
    #     if count > 0:
    #         raise forms.ValidationError('The product already exists')


def email_check(user):
    return user.is_vendor


class VendorCreationForm(UserCreationForm):
    contact_number = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'contact_number']


class writereview(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Write about product', 'rows': '4', 'cols': '50'}))

    class Meta:
        model = Review
        fields = ['content']
