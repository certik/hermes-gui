from enthought.traits.api import (HasTraits, Instance, Range, Array,
        on_trait_change, Property, cached_property, Bool, Tuple, Enum)
from enthought.traits.ui.api import View, Item, Group
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from enthought.traits.ui.api import CustomEditor
import wx
import numpy

from hermes2d import Solution
from hermes2d.plot import plot_sln_mpl

from ..handle_hermes import plot_mesh

def make_plot(parent, editor):
    """
    Builds the Canvas window for displaying the mpl-figure
    """
    from PyQt4 import QtGui
    #l = QtGui.QLabel("sldkfja;slfdj")
    #parent.addWidget(l)

    widget = QtGui.QWidget()
    color="green"
    palette = widget.palette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(color))
    widget.setPalette(palette)
    widget.setAutoFillBackground(True)
    widget.setMinimumWidth(100)
    widget.setMinimumHeight(100)
    parent.addWidget(widget)
    return widget

    fig = editor.object.figure
    panel = wx.Panel(parent, -1)
    canvas = FigureCanvasWxAgg(panel, -1, fig)
    toolbar = NavigationToolbar2Wx(canvas)
    toolbar.Realize()
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(canvas,1,wx.EXPAND|wx.ALL,1)
    sizer.Add(toolbar,0,wx.EXPAND|wx.ALL,1)
    panel.SetSizer(sizer)
    return panel

class PlotModel(HasTraits):
    """A Model for displaying a matplotlib figure"""

    figure = Instance(Figure)
    axes = Instance(Axes)
    _draw_pending = Bool(False) #a flag to throttle the redraw rate

    mode = Enum("mesh", "solution", label="Mode")
    mesh_nodes = Bool(True, label="Show nodes")
    mesh = Tuple
    sln = Instance(Solution)

    traits_view = View(
            Group(
                Item('figure', editor=CustomEditor(make_plot),
                    show_label=False, resizable=True)
                ),
            Item('mode',
                enabled_when="sln is not None"),
            Item('mesh_nodes',
                enabled_when="(mesh is not ()) and (mode == 'mesh')"),
            resizable=True
        )

    def _figure_default(self):
        return Figure(figsize=(1, 1))

    def _axes_default(self):
        return self.figure.add_subplot(111)

    def _mesh_changed(self):
        self.replot()

    def _sln_changed(self):
        self.replot()

    def _mode_changed(self):
        self.replot()

    def _mesh_nodes_changed(self):
        self.replot()

    def replot(self):
        self.figure.delaxes(self.axes)
        self.axes = self.figure.add_subplot(111)
        if self.mode == "mesh":
            if self.mesh:
                plot_mesh(self.mesh, axes=self.axes, plot_nodes=self.mesh_nodes)
        elif self.mode == "solution":
            if self.sln:
                plot_sln_mpl(self.sln, axes=self.axes)
        self.redraw()


    def redraw(self):
        if self._draw_pending:
            return
        canvas = self.figure.canvas
        if canvas is None:
            return
        def _draw():
            canvas.draw()
            self._draw_pending = False
        wx.CallLater(50, _draw).Start()
        self._draw_pending = True
