from django.forms import ModelForm
from BudgetAPP.models import *
from django import forms
from django.utils.dateparse import parse_date


class DateInput(forms.DateInput):
    input_type = "date"


class UserCreationForm(ModelForm):
    class Meta:
        model = AccountInfo
        fields = ['name', 'address', 'mobilenum', 'emailid', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }


class AddExpenseForm(ModelForm):
    # date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = ExpenseInfo
        fields = ['category', 'expense_name', 'amount', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].widget = DateInput()

    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get("amount")

        if amount < 10:
            msg = "please provide correct value for price"
            self.add_error("price", msg)


class UserLoginForm(ModelForm):
    class Meta:
        model = AccountInfo
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        if (AccountInfo.objects.filter(username=username)):
            pass
        else:
            msg = "Uh-oh! There's no such user existing in this name......"
            self.add_error('username', msg)


class ExpenseCategory(ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']


class dateInsertForm(forms.Form):
    from_date = forms.DateField(widget=forms.SelectDateWidget)
    to_date = forms.DateField(widget=forms.SelectDateWidget)


class CategoryInsertForm(ModelForm):
    from_date = forms.DateField(widget=forms.SelectDateWidget)
    to_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = ExpenseInfo
        fields = ['category']
