class Ray:
    """DEFINIMOS EL OBJETO RAYO, QUE LO TRATAMOS COMO UNA RECTA PARAMETRICA 
    VECTORIAS  DE LA FORMA O+Dt, donde O es el origen, y D es la direccion
    que suele ser un vector normalizado (como nosotros lo estaremos trabajando)"""

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()
