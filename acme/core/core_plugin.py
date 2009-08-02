from enthought.envisage.api import Plugin
from enthought.traits.api import List


class HermesPlugin(Plugin):
    ACTION_SETS       = 'enthought.envisage.ui.workbench.action_sets'
    PERSPECTIVES      = 'enthought.envisage.ui.workbench.perspectives'
    PREFERENCES_PAGES = 'enthought.envisage.ui.workbench.preferences_pages'
    VIEWS             = 'enthought.envisage.ui.workbench.views'


    id = 'acme.core'
    name = 'Core Workbench'

    action_sets = List(contributes_to=ACTION_SETS)

    def _action_sets_default(self):
        """ Trait initializer. """

        from action_set import ActionSet

        return [ActionSet]

    perspectives = List(contributes_to=PERSPECTIVES)

    def _perspectives_default(self):
        """ Trait initializer. """

        from default_perspective import DefaultPerspective

        return [DefaultPerspective]

    views = List(contributes_to=VIEWS)

    def _views_default(self):
        """ Trait initializer. """

        from views import (ProblemView, LocalValuesView, VolumeIntegralView,
                SurfaceIntegralView, RedView, YellowView, SceneView)

        return [ProblemView, LocalValuesView, VolumeIntegralView,
                SurfaceIntegralView, RedView, YellowView, SceneView]
