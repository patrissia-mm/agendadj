from django.shortcuts import render
from django.views.generic import ListView, TemplateView
#
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
) 
#
from .models import Person
from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    PersonaSerializer2
)


class PersonListView(ListView):
    template_name = "persona/personas.html"
    context_object_name = 'personas'
    def get_queryset(self):
        return Person.objects.all()

class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()


class PersonasListView(TemplateView):
    """ Ejemplo de uso del servicio API """
    template_name = "persona/lista.html"

class PersonSearchApiView(ListAPIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )

class PersonCreateView(CreateAPIView):
    serializer_class = PersonSerializer

class PersonDetailView(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonUpdateView(UpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonApiLista(ListAPIView):
    #serializer_class = PersonaSerializer
    serializer_class = PersonaSerializer2
    def get_queryset(self):
        return Person.objects.all()

