from enthought.traits.api import HasTraits, Str, List, Int, Instance, BaseInt
from utils import get_data_dir
from lxml import etree

class MyInt(BaseInt):

    def validate(self, object, name, value):
        if isinstance(value, str):
            try:
                value = int(value)
            except ValueError:
                self.error(object, name, value)
        return super(MyInt, self).validate(object, name, value)


class ProblemEdge(HasTraits):
    pass

class ProblemLabel(HasTraits):
    pass

class Problem(HasTraits):
    name = Str
    type = Str
    numberofrefinements = MyInt
    edges = List(ProblemEdge)
    labels = List(ProblemLabel)

    def _numberofrefinements_validate():
        pass


class Node(HasTraits):
    pass

class Edge(HasTraits):
    pass

class Label(HasTraits):
    pass

class Geometry(HasTraits):
    nodes = List(Node)
    edges = List(Edge)
    labels = List(Label)



def read_a2d(filename):
    root = etree.fromstring(open(filename).read())

    problem = root.xpath("/document/problems/problem")[0]
    p = Problem(**problem.attrib)
    #p.name = problem.get("name")
    #p.type = problem.get("problemtype")
    #p.number_of_refinements = int(problem.get("numberofrefinements"))

    p.script_startup = problem.xpath("scriptstartup")[0]
    p.edges = [ProblemEdge(**edge.attrib) for edge in \
            problem.xpath("edges/edge")]
    p.labels = [ProblemLabel(**label.attrib) for label in \
            problem.xpath("labels/label")]

    geometry = root.xpath("/document/geometry")[0]
    g = Geometry()
    g.nodes = [Node(**node.attrib) for node in geometry.xpath("nodes/node")]
    g.edges = [Edge(**edge.attrib) for edge in geometry.xpath("edges/edge")]
    g.labels = [Label(**label.attrib) for label in \
            geometry.xpath("labels/label")]

    p.print_traits()



read_a2d(get_data_dir()+"/agros2d/electrostatic_planar_capacitor.a2d")
