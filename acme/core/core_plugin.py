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

        from acme.workbench.perspective.api import FooPerspective

        return [FooPerspective]

    views = List(contributes_to=VIEWS)

    def _views_default(self):
        """ Trait initializer. """

        from views import BlackView, BlueView, GreenView, RedView, YellowView

        return [BlackView, BlueView, GreenView, RedView, YellowView]
