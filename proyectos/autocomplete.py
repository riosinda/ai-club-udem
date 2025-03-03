# proyectos/autocomplete.py
from dal import autocomplete
from .models import Autor

class AutorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Asegúrate de que el usuario esté autenticado si es necesario:
        if not self.request.user.is_authenticated:
            return Autor.objects.none()

        qs = Autor.objects.all()

        if self.q:  # 'q' es el texto que el usuario escribe
            qs = qs.filter(nombre__icontains=self.q)

        return qs
