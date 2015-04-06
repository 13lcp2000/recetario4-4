from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

# Here we are specifying urls for the
# different ways to navigate through
# the website
urlpatterns = patterns('',
	url(r'^$','principal.views.inicio'),

    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^contacto/$','principal.views.contacto'),
    url(r'^comenta/$','principal.views.nuevo_comentario'),
    url(r'^ingresar/$','principal.views.ingresar'),
    url(r'^privado/$','principal.views.privado'),
    url(r'^cerrar/$', 'principal.views.cerrar'),
    

    url(r'^usuarios/$','principal.views.usuarios'),
    url(r'^usuario/nuevo/$','principal.views.nuevo_usuario'),


    url(r'^bebida/(?P<id_bebida>\d+)$','principal.views.detalle_bebida', name="bebida_name"),
    url(r'^bebidas/$','principal.views.lista_bebidas', name="listar_bebidas_name"),
    url(r'^bebida/nueva/$','principal.views.nueva_bebida', name="new_B"),
    url(r'^bebida/borrar/$','principal.views.borrar_bebida', name="borrar_B"),

    
    url(r'^receta/(?P<id_receta>\d+)/$','principal.views.detalle_receta', name="receta_name"),
    url(r'^recetas/$','principal.views.lista_recetas', name="listar_recetas_name"),
    url(r'^receta/nueva/$','principal.views.nueva_receta', name="new_R"),
    url(r'^receta/borrar/(?P<id_receta>\d+)/$','principal.views.borrar_receta', name="borrar_R"),

    
    url(r'^postre/(?P<id_postre>\d+)$','principal.views.detalle_postre', name="postre_name"),
    url(r'^postres/$','principal.views.lista_postres', name="listar_postres_name"),
    url(r'^postre/nuevo/$','principal.views.nuevo_postre', name="new_P"),
    url(r'^postre/borrar/$','principal.views.borrar_postre', name="borrar_P"),
)
