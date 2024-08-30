from django.db import models


# Create your models here.
class Classes(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    
    class Meta:
        db_table = 'classes'
        ordering = ('id', )
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'
    
    def __str__(self):
        return self.nome
    
class Componentes(models.Model):
    nome = models.CharField(max_length=10, blank=False, null=False)

    class Meta:
        db_table = 'componentes'
        ordering = ('id', )
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'
        
    def __str__(self):
        return self.nome
    
class Escolas(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    cor = models.CharField(max_length=7, blank=True, null=True, help_text='Insira uma cor em formato hexadecimal, ex: #FF5733')

    
    class Meta:
        db_table = 'escolas'
        ordering = ('id', )
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'

    def __str__(self):
        return self.nome

class Fonte(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    
    class Meta:
        db_table = 'fontes'
        ordering = ('id', )
        verbose_name = 'Fonte'
        verbose_name_plural = 'Fontes'

    def __str__(self):
        return self.nome

class Magias(models.Model):
    nome = models.TextField()
    nivel = models.IntegerField(blank=False, null=False)
    tempo_conjuracao = models.CharField(max_length=50, blank=False, null=False)
    duracao = models.CharField(max_length=50, blank=False, null=False)
    alcance = models.CharField(max_length=50, blank=False, null=False)
    descricao = models.TextField(blank=False, null=False)
    em_nivel_mais_alto = models.TextField(blank=False, null=True)
    ritual = models.BooleanField(blank=False, null=False, default=False)
    concentracao = models.BooleanField(blank=False, null=False, default=False)
    ataque_magico = models.BooleanField(blank=False, null=False, default=False)
    tipo_dado = models.CharField(max_length=20, blank=False, null=False)
    savaguarda = models.CharField(max_length=50, blank=False, null=False)
    truque = models.BooleanField(blank=False, null=False, default=False)
    alvo = models.CharField(max_length=100, blank=False, null=True)
    escola = models.ForeignKey(Escolas, verbose_name=("escola_magia"), on_delete=models.CASCADE, blank=False, null=False)
    fonte = models.ForeignKey(Fonte, verbose_name=("magia_fonte"), on_delete=models.CASCADE, blank=False, null=True)
    componentes = models.ManyToManyField(Componentes, verbose_name=("componentes_magias"))
    material_descricao = models.TextField(blank=True, null=True)
    classes = models.ManyToManyField(Classes, verbose_name=("classes_magias"))
    imagem = models.ImageField(upload_to='magias/', blank=True, null=True, verbose_name="Imagem da Magia")
    
    class Meta:
        db_table = 'magias'
        ordering = ('id', )
        verbose_name = 'Magia'
        verbose_name_plural = 'Magias'
        
    def __str__(self):
        return self.nome