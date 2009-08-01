from enthought.envisage.api import Plugin
from enthought.traits.api import List


class HermesPlugin(Plugin):
    ACTION_SETS       = 'enthought.envisage.ui.workbench.action_sets'
    VIEWS             = 'enthought.envisage.ui.workbench.views'

    id = 'acme.core'
    name = 'Core Workbench'

    action_sets = List(contributes_to=ACTION_SETS)

    def _action_sets_default(self):
        """ Trait initializer. """

        from action_set import ActionSet

        return [ActionSet]

    views = List(contributes_to=VIEWS)

    def _views_default(self):
        """ Trait initializer. """

        from views import BlackView, BlueView, GreenView, RedView, YellowView

        return [BlackView, BlueView, GreenView, RedView, YellowView]
