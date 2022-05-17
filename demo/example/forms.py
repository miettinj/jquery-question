from django import forms
from django.forms import fields, models, formsets, widgets
from django.contrib.admin.widgets import AdminDateWidget
from django.conf import settings



class SingleClsVariable(forms.Form):
    technical_name = forms.CharField(widget=forms.TextInput(
                                        attrs={
                                            'class':'readonly_able tn'
                                            }
                                        ))
    
    var_name_fi =  forms.CharField(     
                        widget=forms.HiddenInput())
    var_name_sv =  forms.CharField(     
                        widget=forms.HiddenInput())
    var_name_en =  forms.CharField(     
                        widget=forms.HiddenInput())
    
    var_desc_fi =  forms.CharField(     
                        widget=forms.HiddenInput())
    var_desc_sv =  forms.CharField(     
                        widget=forms.HiddenInput())
    var_desc_en =  forms.CharField(     
                        widget=forms.HiddenInput())
    var_class_id =  forms.CharField(     
                        widget=forms.HiddenInput())
                                     
    
    
    
class SingleNumVariable(forms.Form):
    technical_name = forms.CharField(widget=forms.TextInput(
                                        attrs={
                                            'class':'readonly_able tn'
                                            }
                                        ))

    var_name_fi =  forms.CharField(     
                        widget=forms.HiddenInput())
    var_name_sv =  forms.CharField(     
                        widget=forms.HiddenInput())
    var_name_en =  forms.CharField(     
                        widget=forms.HiddenInput())
    
    var_desc_fi =  forms.CharField(     
                        widget=forms.HiddenInput())
    var_desc_sv =  forms.CharField(     
                        widget=forms.HiddenInput())
    var_desc_en =  forms.CharField(     
                        widget=forms.HiddenInput())
    

class LuokittelevatmuuttujatForm(forms.Form):
    technical_name = forms.CharField(widget=forms.TextInput(
                                        attrs={
                                            'class':'readonly_able tn'
                                            }
                                        ))

    

