from enthought.traits.api import HasTraits, Instance, Range,\
                           Array, on_trait_change, Property,\
                           cached_property, Bool
from enthought.traits.ui.api import View, Item
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from enthought.traits.ui.api import CustomEditor
import wx
import numpy

def make_plot(parent, editor):
    """
    Builds the Canvas window for displaying the mpl-figure
    """
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

    figure = Instance(Figure, ())
    axes = Instance(Axes)
    line = Instance(Line2D)
    _draw_pending = Bool(False) #a flag to throttle the redraw rate

    #a variable paremeter
    scale = Range(0.1,10.0)
    #an independent variable
    x = Array(value=numpy.linspace(-5,5,512))
    #a dependent variable
    y = Property(Array, depends_on=['scale','x'])

    traits_view = View(
            Item('figure', editor=CustomEditor(make_plot), resizable=True),
            Item('scale'),
            resizable=True
        )

    def _axes_default(self):
        return self.figure.add_subplot(111)

    def _line_default(self):
        return self.axes.plot(self.x, self.y)[0]

    @cached_property
    def _get_y(self):
        return numpy.sin(self.scale * self.x)

    @on_trait_change("x, y")
    def update_line(self, obj, name, val):
        attr = {'x': "set_xdata", 'y': "set_ydata"}[name]
        getattr(self.line, attr)(val)
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

if __name__=="__main__":
    model = PlotModel(scale=2.0)
    model.configure_traits()
