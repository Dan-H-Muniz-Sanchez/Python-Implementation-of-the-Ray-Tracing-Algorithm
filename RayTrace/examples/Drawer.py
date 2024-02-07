

from color import Color
from light import Light
from material import ChequeredMaterial, Material
from point import Point
from sphere import Sphere
from vector import Vector
from cube import Cube

WIDTH = 960
HEIGHT = 540
RENDERED_IMG = "Draw.ppm"
CAMERA = Vector(0, -0.35, -1)
OBJECTS = [
    # Ground Plane
    Sphere(
        Point(0, 10000.5, 1),
        10000.0,
        ChequeredMaterial(
            color1=Color.from_hex("#000000 "),
            color2=Color.from_hex("#FFFFFF "),
            ambient=0.5,
            reflection=0.1,
        ),
    ),
    # Blue ball
    Cube(Point(0.75, -0.1, 1), 0.6,0.6,0.6, Material(Color.from_hex("#0000FF"))),
    # Pink ball
    Cube(Point(-0.75, -0.1, 2.25), 0.6,0.6,0.6, Material(Color.from_hex("#803980"))),
    # Yellow Ball
    #Sphere(Point(-0.75, -0.1, 1), 0.3, Material(Color.from_hex("#F9FC30"))),
    #Purple Ball
    Cube(Point(0.0, -0.1, 6.50), 2.0,2.0,2.0, Material(Color.from_hex("#08D40A"))),

    Sphere(Point(-0.85, -0.07, 1), 0.3 ,Material(Color.from_hex("#F9FC30")) ),
    Sphere(Point(0.30, -0.2, 1), 0.5, Material(Color.from_hex("#F10A0A "))), ##36ABF6
    Sphere(Point(0.60, -0.2, -1 ), 0.5, Material(Color.from_hex("#F10A0A "))),
    Sphere(Point(0.80, -0.1, -1.2 ), 0.5, Material(Color.from_hex("#36ABF6 "))),

]
LIGHTS = [
    Light(Point(1.5, -0.5, -10), Color.from_hex("#FFFFFF")),
]


"""
from color import Color
from light import Light
from material import ChequeredMaterial, Material
from point import Point
from sphere import Sphere
from vector import Vector
from cube import Cube

WIDTH = 960
HEIGHT = 540
RENDERED_IMG = "2balls.ppm"
CAMERA = Vector(0, -0.35, -1)
OBJECTS = [
    # Ground Plane
    Sphere(
        Point(0, 10000.5, 1),
        10000.0,
        ChequeredMaterial(
            color1=Color.from_hex("#1914C4  "),
            color2=Color.from_hex("#1914C4 "),
            ambient=0.5,
            reflection=0.1,
        ),
    ),
    # Blue ball
    Cube(Point(0.75, -0.1, 0.2), 0.6,0.6,0.6, Material(Color.from_hex("#0000FF"))),
    # Pink ball
    Sphere(Point(-0.75, -0.1, 0.3), 0.6, Material(Color.from_hex("#803980"))),

]
LIGHTS = [
    Light(Point(1.5, -0.5, -10), Color.from_hex("#FFFFFF")),
]


"""