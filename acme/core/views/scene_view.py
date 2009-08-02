from enthought.etsconfig.api import ETSConfig
from enthought.pyface.workbench.api import View

from mpl_editor import PlotModel

class SceneView(View):
    category = 'Color'
    name = 'Scene'
    position = 'bottom'
    model = PlotModel

    def _id_default(self):
        return self.name

    def create_control(self, parent):
        method = getattr(self, '_%s_create_control' % ETSConfig.toolkit, None)
        if method is None:
            raise SystemError('Unknown toolkit %s', ETSConfig.toolkit)

        color = "green"

        return method(parent, color)

    def _wx_create_control(self, parent, color):
        """ Create a wx version of the control. """

        import wx

        panel = wx.Panel(parent, -1)
        panel.SetBackgroundColour(color)

        return panel

    def _qt4_create_control(self, parent, color):
        """ Create a Qt4 version of the control. """

        from PyQt4 import QtGui

        widget = QtGui.QWidget(parent)

        palette = widget.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(color))
        widget.setPalette(palette)
        widget.setAutoFillBackground(True)

        return widget
