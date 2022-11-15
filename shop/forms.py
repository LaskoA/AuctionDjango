from .models import Lot, Category
from django import forms


class LotForm(forms.ModelForm):
    class Meta:
        model = Lot
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class LotSearchForm(forms.Form):
    category = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by category"}),
    )
