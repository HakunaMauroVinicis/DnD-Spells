from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from django import forms
from .models import Magias, Classes, Componentes, Escolas, Fonte

class EscolasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cor', 'color_display')
    search_fields = ('nome',)
    list_editable = ('cor',)

    def color_display(self, obj):
        """
        Exibe um quadrado colorido correspondente ao valor cadastrado na cor.
        """
        if obj.cor:
            return format_html(
                '<div style="width: 20px; height: 20px; background-color: {}; border: 1px solid #000;"></div>',
                obj.cor
            )
        return '-'
    color_display.short_description = 'Cor' 


class MagiasAdminForm(forms.ModelForm):
    class Meta:
        model = Magias
        fields = '__all__'

    # Método para inicializar o formulário com um campo adicional
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Campo adicional para a descrição do material, invisível por padrão
        self.fields['material_descricao'].widget = forms.Textarea(attrs={'rows': 2, 'cols': 40, 'style': 'display: none;'})

    def clean(self):
        cleaned_data = super().clean()
        componentes = cleaned_data.get('componentes')
        
        # Verifica se o componente 'M' foi selecionado
        if componentes and any(componente.nome == 'M' for componente in componentes):
            self.fields['material_descricao'].widget = forms.Textarea(attrs={'rows': 2, 'cols': 40, 'style': 'display: block;'})

        return cleaned_data

class MagiasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'nivel', 'escola', 'duracao', 'imagem_mini')
    search_fields = ('nome', 'descricao')

    # Adiciona um campo de visualização de texto completo na página de detalhes
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 4, 'cols': 40})},
    }
    
    def imagem_mini(self, obj):
        """Exibe uma miniatura da imagem na área administrativa."""
        if obj.imagem:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.imagem.url)
        return "-"
    imagem_mini.short_description = 'Imagem'
        
    

admin.site.register(Magias, MagiasAdmin)
admin.site.register(Classes)
admin.site.register(Componentes)
admin.site.register(Escolas, EscolasAdmin)
admin.site.register(Fonte)