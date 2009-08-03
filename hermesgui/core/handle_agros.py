from enthought.traits.api import (HasTraits, Str, List, Int, Instance, BaseInt,
        BaseFloat)
from enthought.traits.ui.api import View, Item
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

class MyFloat(BaseFloat):

    def validate(self, object, name, value):
        if isinstance(value, str):
            try:
                value = float(value)
            except ValueError:
                self.error(object, name, value)
        return super(MyFloat, self).validate(object, name, value)


class ProblemEdge(HasTraits):
    pass

class ProblemLabel(HasTraits):
    pass

class Problem(HasTraits):
    name = Str
    type = Str
    adaptivitysteps = MyInt
    adaptivitytype = Str
    adaptivitytolerance = MyFloat
    frequency = MyInt
    id = MyInt
    polynomialorder = MyInt
    problemtype = Str
    numberofrefinements = MyInt
    edges = List(ProblemEdge)
    labels = List(ProblemLabel)

    view = View(
            Item("name"),
            Item("type"),
            Item("problemtype"),
            Item("edges"),
            Item("labels"),
            resizable=True)

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

    view = View(
            Item("nodes"),
            Item("edges"),
            Item("labels"),
            resizable=True)


def read_a2d(filename):
    root = etree.fromstring(open(filename).read())

    problem = root.xpath("/document/problems/problem")[0]
    p = Problem(**problem.attrib)
    #p.name = problem.get("name")
    #p.type = problem.get("problemtype")
    #p.number_of_refinements = int(problem.get("numberofrefinements"))

    #p.script_startup = problem.xpath("scriptstartup")[0]
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

    p.configure_traits()
    g.configure_traits()



if __name__ == "__main__":
    import glob
    for file in glob.glob(get_data_dir()+"/agros2d/*.a2d"):
        print file
        read_a2d(file)
