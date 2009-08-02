from enthought.etsconfig.api import ETSConfig
from enthought.traits.api import Instance, DelegatesTo
from enthought.pyface.workbench.api import View

from hermes2d import Solution

from mpl_editor import PlotModel


class SceneView(View):
    category = 'Color'
    name = 'Scene'
    position = 'bottom'
    model = Instance(PlotModel)
    mesh = DelegatesTo("model")
    sln = DelegatesTo("model")
    mode = DelegatesTo("model")

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

        self.model = PlotModel(toolkit="wx")
        ui = self.model.edit_traits(parent=parent, kind='subpanel')
        return ui.control

    def _qt4_create_control(self, parent, color):
        """ Create a Qt4 version of the control. """

        self.model = PlotModel(toolkit="qt4")
        ui = self.model.edit_traits(parent=parent, kind='subpanel')
        return ui.control
        from PyQt4 import QtGui

        widget = QtGui.QWidget(parent)

        palette = widget.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(color))
        widget.setPalette(palette)
        widget.setAutoFillBackground(True)

        return widget
