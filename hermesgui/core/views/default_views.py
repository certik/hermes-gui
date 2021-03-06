from enthought.etsconfig.api import ETSConfig
from enthought.traits.api import Instance, Undefined, Str
from enthought.traits.ui.api import (View, Item, TreeNode, TreeEditor, Action,
        Handler, Group)
from enthought.pyface.workbench.api import View as PyfaceView

from ..handle_agros import Problem, Geometry, Node, Edge, Label
from ..utils import search_path


class ColorView(PyfaceView):
    category = 'Color'

    def _id_default(self):
        return self.name

    def create_control(self, parent):
        method = getattr(self, '_%s_create_control' % ETSConfig.toolkit, None)
        if method is None:
            raise SystemError('Unknown toolkit %s', ETSConfig.toolkit)

        color = self.name.lower()

        return method(parent, color)

    def _wx_create_control(self, parent, color):
        """ Create a wx version of the control. """

        import wx

        panel = wx.Panel(parent, -1)
        panel.SetBackgroundColour(color)

        return panel

    def _qt4_create_control(self, parent, color):
        """ Create a Qt4 version of the control. """

        color="white"
        from PyQt4 import QtGui
        widget = QtGui.QWidget(parent)
        palette = widget.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(color))
        widget.setPalette(palette)
        widget.setAutoFillBackground(True)

        return widget

def format_node(node, _):
    return "[%g; %g]" % (node.x, node.y)

def format_edge(edge, _):
    return "[%d] - [%d]" % (edge.start, edge.end)

def format_label(label, _):
    return "[%g; %g]" % (label.x, label.y)

def configure(node):
    node.configure_traits()

no_view = View()
tree_editor = TreeEditor(nodes=[
    TreeNode(
        node_for=[Geometry],
        children="",
        label="=Geometry",
        view=no_view,
        icon_item="",
        ),
    TreeNode(
        node_for=[Geometry],
        children="nodes",
        label="=Nodes",
        view=no_view,
        icon_group="",
        icon_open="",
        add=[Node],
        ),
    TreeNode(
        node_for=[Geometry],
        children="edges",
        label="=Edges",
        view=no_view,
        icon_group="",
        icon_open="",
        add=[Edge],
        ),
    TreeNode(
        node_for=[Geometry],
        children="labels",
        label="=Labels",
        view=no_view,
        icon_group="",
        icon_open="",
        add=[Label],
        ),
    TreeNode(
        node_for=[Node],
        formatter=format_node,
        icon_item="scene-node.png",
        icon_path=search_path,
        view=no_view,
        on_dclick=configure,
        ),
    TreeNode(
        node_for=[Edge],
        formatter=format_edge,
        icon_item="scene-edge.png",
        icon_path=search_path,
        view=no_view,
        on_dclick=configure,
        ),
    TreeNode(
        node_for=[Label],
        formatter=format_label,
        icon_item="scene-label.png",
        icon_path=search_path,
        view=no_view,
        on_dclick=configure,
        ),
            ])

class ProblemView(PyfaceView):
    name = 'Problem'
    position = 'bottom'
    problem = Instance(Problem)
    geometry = Instance(Geometry)

    view = View(
        Group(
            Item("geometry", editor=tree_editor),
            show_labels=False
            ),
        )


    def _geometry_default(self):
        return Geometry()

    def _id_default(self):
        return self.name

    def create_control(self, parent):
        ui = self.edit_traits(parent=parent, kind='subpanel')
        return ui.control

class LocalValuesView(ColorView):
    name = 'Local Values'
    position = 'bottom'

class VolumeIntegralView(ColorView):
    name = 'Volume Integral'
    position = 'bottom'

class SurfaceIntegralView(ColorView):
    name = 'Surface Integral'
    position = 'bottom'

class RedView(ColorView):
    name = 'Red'
    position = 'bottom'

class YellowView(ColorView):
    name = 'Yellow'
    position = 'bottom'
