from django import forms

class Registration_form(forms.Form):
    fname=forms.CharField(
        label='fname',
        widget = forms.TextInput(
            attrs={
                "placeholder": "enter first name",
                'class': 'form-control',
                'autocomplete': False
        }))
    ln=forms.CharField(
        label='ln',
        widget = forms.TextInput(
             attrs={
                "placeholder": "enter last name",
                'class': 'form-control',
                'autocomplete': False
             }  )  )
    un=forms.CharField(
        label='un',
        widget = forms.TextInput(
             attrs={
                 "placeholder": "enter last name",
                 'class': 'form-control',
                 'autocomplete': False
        }
    )
    )
    pswd=forms.CharField(
        label="password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
                'class':'form-control'

            }
        )
    )
    mobile=forms.IntegerField(label='mobile')
    email=forms.EmailField(label='email')


class Login_form(forms.Form):
    uname=forms.CharField(
        label="user name",
        widget=forms.TextInput(
            attrs={
                "placeholder":"enter user name",
                'class':'form-control',
                'autocomplete':False
            }
        )

    )
    passw=forms.CharField(
        label="password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':"password",
                'class':'form-control'
            }
        )
    )

class Feedback_from(forms.Form):
    # name=forms.CharField(
    #     label="enter your name",
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder':"enter name",
    #             'class':'form-control'
    #         }
    #     )
    # )
    # rating=forms.IntegerField(
    #     label="enter your rating",
    #     widget=forms.NumberInput(
    #         attrs={
    #             'placeholder':"eter your rating",
    #             "class":"form-control"
    #         }
    #     )
    # )
    #
    # desc=forms.CharField(
    #     label="Description",
    #     widget=forms.Textarea(
    #         attrs={
    #             'placeholder':'enter your description',
    #             "class":"form-conttrol"
    #         }
    #     )
    # )
    #
    name=forms.CharField(label="name")
    rating=forms.IntegerField(label="rating")
    desc=forms.CharField(label="desc")
