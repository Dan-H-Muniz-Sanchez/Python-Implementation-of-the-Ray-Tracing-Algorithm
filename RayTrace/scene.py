class Scene:
    """CREACION DE LA ESCENA ESTA LIBRERIA NOS SIRVE PARA CONSTRUIR EL OBJETO
    ESCENA Y DECIR SUS ATRIBUTOS , ESTO AYUDARA PARA QUE LA RENDERIZACION SE MAS ORDENADA
    Y CLARA"""

    def __init__(self, camera, objects, lights, width, height):
        self.camera = camera
        self.objects = objects
        self.lights = lights
        self.width = width
        self.height = height
