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
    # remove the element markers
    elements = [x[:-1] for x in elements]
    return plot_mesh_mpl2(nodes, elements, axes=axes)

def poisson_solver(mesh_tuple):
    """
    Poisson solver.

    mesh_tuple ... a tuple of (nodes, elements, boundary, nurbs)
    """
    mesh = Mesh()
    mesh.create(*mesh_tuple)
    mesh.refine_element(0)
    shapeset = H1Shapeset()
    pss = PrecalcShapeset(shapeset)

    # create an H1 space
    space = H1Space(mesh, shapeset)
    space.set_uniform_order(5)
    space.assign_dofs()

    # initialize the discrete problem
    wf = WeakForm(1)
    set_forms(wf)

    solver = DummySolver()
    sys = LinSystem(wf, solver)
    sys.set_spaces(space)
    sys.set_pss(pss)

    # assemble the stiffness matrix and solve the system
    sys.assemble()
    A = sys.get_matrix()
    b = sys.get_rhs()
    from scipy.sparse.linalg import cg
    x, res = cg(A, b)
    sln = Solution()
    sln.set_fe_solution(space, pss, x)
