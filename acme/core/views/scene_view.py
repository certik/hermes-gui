from enthought.traits.api import Instance, DelegatesTo
from enthought.pyface.workbench.api import View

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
        self.model = PlotModel()
        ui = self.model.edit_traits(parent=parent, kind='subpanel')
        return ui.control
