# Maria Isabel Ortiz Naranjo
# Graficas por computadora
# 18176
from Tracing import Raytracer, BLACK
from Tracing import Material
from Tracing import Sphere
from Tracing import color
from Tracing import V3

nieve = Material(diffuse=color(255, 250, 250))
puntos = Material(diffuse=BLACK)
ojo = Material(diffuse=BLACK)
zanahoria = Material(diffuse=color(255, 108, 25))

render = Raytracer(800, 800)
render.models = [
    # Cabeza
    Sphere(V3(0.24, -2.08, -6), 0.06, puntos),
    Sphere(V3(-0.24, -2.08, -6), 0.06, puntos),
    Sphere(V3(0.24, -2.08, -6), 0.14, ojo),
    Sphere(V3(-0.24, -2.08, -6), 0.14, ojo), 
    Sphere(V3(0, -1.82, -6), 0.16, zanahoria),
    Sphere(V3(-0.3, -1.62, -6), 0.06, puntos),
    Sphere(V3(-0.14, -1.48, -6), 0.06, puntos),
    Sphere(V3(0.14, -1.48, -6), 0.06, puntos),
    Sphere(V3(0.3, -1.62, -6), 0.06, puntos),
    # Complementos de Cuerpo
    Sphere(V3(0, -0.6, -6), 0.16, puntos),
    Sphere(V3(0, 0.2, -6), 0.24, puntos),
    Sphere(V3(0, 1.42, -6), 0.32, puntos),
    # Cuerpo
    Sphere(V3(0, -1.8, -6), 0.76, nieve),
    Sphere(V3(0, -0.4, -6), 0.94, nieve),
    Sphere(V3(0, 1.74, -8), 1.8, nieve),
]

render.finish()