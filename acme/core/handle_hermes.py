from hermes2d import Mesh, H1Shapeset, PrecalcShapeset, H1Space, \
                WeakForm, Solution, ScalarView, LinSystem, DummySolver, \
                MeshView
from hermes2d.forms import set_forms
from hermes2d.mesh import read_hermes_format
from hermes2d.plot import plot_mesh_mpl

def read_mesh(filename):
    nodes, elements, boundary, nurbs = read_hermes_format(filename)
    return nodes, elements, boundary, nurbs

def plot_mesh(mesh):
    nodes, elements, boundary, nurbs = mesh
    p = plot_mesh_mpl(nodes, elements)
    p.show()
