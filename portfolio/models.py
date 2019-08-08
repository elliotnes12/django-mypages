from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.timezone import now

class Category(models.Model):
      name = models.CharField(max_length = 50,verbose_name = "Nombre")
      created = models.DateTimeField(auto_now_add=True,verbose_name = "Creado")
      updated = models.DateTimeField(auto_now=True,verbose_name = "Actualizado")
    
      class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["-created"]

      def __str__(self):
            return self.name

class Post(models.Model):
      title = models.CharField(max_length = 200,verbose_name = "Titulo")
      content = RichTextField(verbose_name = "Contenido")
      published = models.DateTimeField(verbose_name = "Fecha publicacion",default = now)
      image = models.ImageField(verbose_name = "Imagen",upload_to = "post",null = True,blank = True)
      author = models.ForeignKey(User,verbose_name = "autor",on_delete = models.CASCADE)
      categories = models.ManyToManyField(Category,verbose_name = "categoria")
      created = models.DateTimeField(auto_now_add=True,verbose_name = "Creado")
      updated = models.DateTimeField(auto_now=True,verbose_name = "Actualizado")
    
      class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"
        ordering = ["-created"]

      def __str__(self):
            return self.title

class Skills(models.Model):
      name = models.CharField(max_length = 50,verbose_name = "Nombre")
      created = models.DateTimeField(auto_now_add=True,verbose_name = "Creado")
      updated = models.DateTimeField(auto_now=True,verbose_name = "Actualizado")
    
      class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        ordering = ["-created"]
   
      def __str__(self):
        return self.name

class Sections(models.Model):
      name = models.CharField(max_length = 50,verbose_name = "Nombre")
      title = models.CharField(max_length = 50,verbose_name = "Titulo")
      description = RichTextField(verbose_name = "Descripcion")
      image = models.ImageField(verbose_name = "Imagen",upload_to = "sections",null = True,blank = True)
      created = models.DateTimeField(auto_now_add=True,verbose_name = "Creado")
      updated = models.DateTimeField(auto_now=True,verbose_name = "Actualizado")
    
      class Meta:
        verbose_name = "Seccion"
        verbose_name_plural = "Secciones"
        ordering = ["-created"]
   
      def __str__(self):
        return self.name

class Position(models.Model):
      name = models.CharField(max_length = 50,verbose_name = "Nombre")
      created = models.DateTimeField(auto_now_add=True,verbose_name = "Creado")
      updated = models.DateTimeField(auto_now=True,verbose_name = "Actualizado")
    
      class Meta:
        verbose_name = "Posicion"
        verbose_name_plural = "Posiciones"
        ordering = ["-created"]
   
      def __str__(self):
        return self.name

class Deparment(models.Model):
     name = models.CharField(max_length = 50,verbose_name = "Nombre")
     created = models.DateTimeField(auto_now_add=True,verbose_name = "Creado")
     updated = models.DateTimeField(auto_now=True,verbose_name = "Actualizado")
    
     class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ["-created"]
   
     def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50,verbose_name="Nombre")
    deparment = models.ForeignKey(Deparment,verbose_name = "Departamento",on_delete = models.CASCADE)
    position = models.ForeignKey(Position,verbose_name="Posicion",on_delete = models.CASCADE)
    createdby = models.ForeignKey(User,verbose_name = "Creado por",on_delete = models.CASCADE)  
    description = RichTextField(verbose_name = "Descripcion")
    skills = models.ManyToManyField(Skills,verbose_name = "Habilidades")
    image = models.ImageField(verbose_name = "Imagen",upload_to = "team")
    created = models.DateTimeField(auto_now_add=True,verbose_name = "Creado")
    updated = models.DateTimeField(auto_now=True,verbose_name = "Actualizado")
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["-created"]
   
    def __str__(self):
        return self.name


class ProjectCategory(models.Model):
      name = models.CharField(max_length=50,verbose_name = "Nombre")
      metadata = models.CharField(max_length=20,verbose_name = "TagName",null = True,blank = True) 
      created = models.DateTimeField(auto_now_add=True,verbose_name = "Creado")
      updated = models.DateTimeField(auto_now=True,verbose_name = "Actualizado")
     

      class Meta:
        verbose_name = "ProyectoCategoria"
        verbose_name_plural = "ProyectoCategorias"
        ordering = ["-created"]

      def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=50,verbose_name= "Titulo")
    description = RichTextField(verbose_name = "Descripcion")
    image = models.ImageField(verbose_name = "Imagen",upload_to = "projects")
    link = models.URLField(null = True,blank = True,verbose_name ="url")
    created = models.DateTimeField(auto_now_add=True,verbose_name = "Creado")
    updated = models.DateTimeField(auto_now=True,verbose_name = "Actualizado")
    categoria = models.ManyToManyField(ProjectCategory,verbose_name = "Categoria")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title