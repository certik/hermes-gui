from enthought.etsconfig.api import ETSConfig
from enthought.traits.api import Instance, Tuple
from enthought.pyface.workbench.api import View

from mpl_editor import PlotModel

class SceneView(View):
    category = 'Color'
    name = 'Scene'
    position = 'bottom'
    model = Instance(PlotModel)
    mesh = Tuple

    def _id_default(self):
        return self.name

    def _mesh_changed(self):
        self.model.mesh = self.mesh

    def create_control(self, parent):
        method = getattr(self, '_%s_create_control' % ETSConfig.toolkit, None)
        if method is None:
            raise SystemError('Unknown toolkit %s', ETSConfig.toolkit)

        color = "green"

        return method(parent, color)

    def _wx_create_control(self, parent, color):
        """ Create a wx version of the control. """

        self.model = PlotModel()
        ui = self.model.edit_traits(parent=parent, kind='subpanel')
        return ui.control

    def _qt4_create_control(self, parent, color):
        """ Create a Qt4 version of the control. """

        from PyQt4 import QtGui

        widget = QtGui.QWidget(parent)

        palette = widget.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(color))
        widget.setPalette(palette)
        widget.setAutoFillBackground(True)

        return widget
