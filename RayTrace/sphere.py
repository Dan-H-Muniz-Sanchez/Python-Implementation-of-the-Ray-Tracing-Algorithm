from math import sqrt


''' un rayo se puede expresar mediante la siguiente función:
    O+Dt=y y Una esfera de forma X^2+Y^2+Z^2=R^2
    Tenemos que considerar uno de los 3 siguientes casos
    
    - EL RAYO INTERSECTO 2 VECES CON LA ESFERA
    - EL RAYO INTERSECTA DE FORMA TANGENCIAL CON LA ESFERA
    - NO HUBO NIGUNA INTERSECCION
    
    PARA ELLO DEBEMOS ESTUDIAR EL DISCRIMINANTE
               DISCRIMINANTE = B^2 -4*A*C
    EL SIGNO DE ESTO NOS REVELARA CUANTAS VECES SE
    INTERSECTO EL RAYO CON LA ESFERA '''

class Sphere:
    

    def __init__(self, center, radius, material): #CONSTRUCTOR DEL OBJETO ESFERA
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray):
        #AQUI REVISAMOS EL DISCRIMINANTE Y LA INTERSECCION CON LOS RAYOS 
        sphere_to_ray = ray.origin - self.center
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius
        discriminant = b * b - 4 * c

        if discriminant >= 0:
            dist = (-b - sqrt(discriminant)) / 2
            if dist > 0:
                return dist
        return None

    def normal(self, surface_point):
        """Funcion que regresa el vector normal sobre cualquier punto de la esfera"""
        return (surface_point - self.center).normalize()