from RecursoDigital import RecursoDigital

class Podcast(RecursoDigital):
    def __init__(self, titulo, autor, anio, num_episodios, tema):
        super().__init__(titulo, autor, anio)
        self.num_episodios = num_episodios
        self.tema = tema

    def abrir(self):
        return f"Abriendo {self.get_titulo()} de {self.get_autor()}"