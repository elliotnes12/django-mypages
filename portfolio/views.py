from django.shortcuts import render
from .models import Project,Employee,ProjectCategory,Sections,Post,Category
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
      template_name = "portfolio/home.html"
      #Contiene la respuesta completa de la peticion
      def get(self,request,*args,**kwargs):
          post = Post.objects.all()
          categoria_proyectos = ProjectCategory.objects.all()
          section_somos = Sections.objects.get(name = "QuienesSomos")
          section_header = Sections.objects.get(name = "cabecera")
          return render(request,self.template_name,{'projects':Project.objects.all(),'posts':post,'catProyecto':categoria_proyectos,'sectionSomos':section_somos,'sectionHeader':section_header})
