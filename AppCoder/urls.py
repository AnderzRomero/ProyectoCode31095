from django.urls import path

from AppCoder.views import entregable, inicio, curso_formulario, busqueda_camada, busqueda_camada_post, \
    eliminar_curso, editar_curso, curso

urlpatterns = [
    path('', inicio, name='AppCoderInicio'),
    path('curso/', curso, name='AppCoderCurso'),
    path('entregable/', entregable, name='AppCoderEntregable'),
    path('curso_formulario/', curso_formulario, name='AppCoderCursoFormulario'),
    path('busqueda_camada/', busqueda_camada, name='AppCoderBusquedaCamada'),
    path('busqueda_camada_post/', busqueda_camada_post, name='AppCoderBusquedaCamadaPost'),
    path('eliminar_curso/<int:camada>', eliminar_curso, name='AppCoderEliminarCurso'),
    path('editar_curso/<int:camada>', editar_curso, name='AppCoderEditarCurso'),
]

