from vector import Vector 
from point import Point

class Cube:

     def __init__(self, center, length, width, height, material):
        self.center = center
        self.length = length
        self.width = width
        self.height = height
        self.material = material

        self.lb = self.center - Point(width/2, height/2, length/2)
        self.rt = self.center + Point(width/2, height/2, length/2)

     def intersects(self, ray):
        #Detecta interseccion con la esfera o no (NONE)
  
        t1 = (self.lb.x-ray.origin.x)/ray.direction.x
        t2 = (self.rt.x-ray.origin.x)/ray.direction.x
        t3 = (self.lb.y-ray.origin.y)/ray.direction.y
        t4 = (self.rt.y-ray.origin.y)/ray.direction.y
        t5 = (self.lb.z-ray.origin.z)/ray.direction.z
        t6 = (self.rt.z-ray.origin.z)/ray.direction.z

        tmin= max(max(min(t1,t2), min(t3,t4)),min(t5,t6))
        tmax= min(min(max(t1,t2), max(t3,t4)),max(t5,t6))

        mask1= (tmax <0) | (tmin > tmax)

        if mask1==1:
            return None

        mask2= tmin<0

        if mask2:
            return tmax
        else:
            return tmin
        

     def normal(self, surface_point):
        #Funcion para regresar el vector normal del punto en el cubo
        P=(surface_point-self.center).normalize()

        tol=0.0001

        xn=self.center.x-self.width/2
        yn=self.center.y-self.height/2
        zn=self.center.z-self.length/2

        xp=self.center.x+self.width/2
        yp=self.center.y+self.height/2
        zp=self.center.z+self.length/2

        mindiff = min(min(min(abs(surface_point.z-zn),abs(surface_point.z-zp)), min(abs(surface_point.x-xn),abs(surface_point.x-xp))), min(abs(surface_point.y-yn),abs(surface_point.y-yp)))

        #Cara frontal
        if abs(surface_point.z-zn)==mindiff:
            return Vector(0,0,-1)

        #Cara trasera
        if abs(surface_point.z-zp)==mindiff:
            return Vector(0,0,1)

        #Cara lateral izquierda
        if abs(surface_point.x-xn)==mindiff:
            return Vector(-1,0,0)

        #Cara lateral derecha
        if abs(surface_point.x-xp)==mindiff:
            #print("Entro al if")
            #print(P)
            return Vector(1,0,0)

        #Cara superior
        if abs(surface_point.y-yn)==mindiff:
            return Vector(0,-1,0)

        #Cara inferior
        if abs(surface_point.y-yp)==mindiff:
            return Vector(0,1,0)

        
        return P