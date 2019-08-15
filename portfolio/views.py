from django.shortcuts import render
from .models import Project,Employee,ProjectCategory,Sections,Post,Category
from django.views.generic.base import TemplateView
from django.conf import settings

class HomePageView(TemplateView):
      template_name = "portfolio/home.html"
      #Contiene la respuesta completa de la peticion
      def get(self,request,*args,**kwargs):
          post = Post.objects.all()
          base = settings.BASE_URL
          hometitle =  'Consultoria Web SEO BukaSystem  '
          categoria_proyectos = ProjectCategory.objects.all()
          section_somos = Sections.objects.get(name = "QuienesSomos")
          section_header = Sections.objects.get(name = "cabecera")
          return render(
               request,self.template_name,
                {'projects':Project.objects.all(),
                 'posts':post,
                 'projectsCAT':categoria_proyectos,
                 'about':section_somos,
                 'header':section_header,
                 'baseURL':base,
                 'Hometitle':hometitle
                 }
                )
