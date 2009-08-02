from hermes2d import Mesh, H1Shapeset, PrecalcShapeset, H1Space, \
                WeakForm, Solution, ScalarView, LinSystem, DummySolver
from hermes2d.forms import set_forms
from hermes2d.mesh import read_hermes_format

def read_mesh(filename):
    nodes, elements, boundary, nurbs = read_hermes_format(filename)
    return nodes, elements, boundary, nurbs
