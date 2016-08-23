# -*- coding: utf-8 -*-

from django import forms


class DocumentForm(forms.Form):
    # docfile = forms.FileField(
    #     label='Select Due Diligence Files to upload'
    # )

	docfile = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))