from enthought.etsconfig.api import ETSConfig
from enthought.traits.api import Instance, Undefined, Str
from enthought.traits.ui.api import View, Item
from enthought.pyface.workbench.api import View as PyfaceView

from ..handle_agros import Problem, Geometry


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


class ProblemView(PyfaceView):
    name = 'Problem'
    position = 'bottom'
    problem = Instance(Problem)
    geometry = Instance(Geometry)

    view = View(
            Item("problem"),
            Item("geometry"),
            )

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
