from hermes2d import Mesh, H1Shapeset, PrecalcShapeset, H1Space, \
                WeakForm, Solution, ScalarView, LinSystem, DummySolver, \
                MeshView
from hermes2d.forms import set_forms
from hermes2d.mesh import read_hermes_format
from hermes2d.plot import plot_mesh_mpl2

def read_mesh(filename):
    nodes, elements, boundary, nurbs = read_hermes_format(filename)
    return nodes, elements, boundary, nurbs

def plot_mesh(mesh, axes=None):
    nodes, elements, boundary, nurbs = mesh
    return plot_mesh_mpl2(nodes, elements, axes=axes)
