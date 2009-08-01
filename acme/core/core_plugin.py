from enthought.envisage.api import Plugin
from enthought.traits.api import List


class HermesPlugin(Plugin):
    ACTION_SETS       = 'enthought.envisage.ui.workbench.action_sets'
    id = 'acme.core'
    name = 'Core Workbench'

    action_sets = List(contributes_to=ACTION_SETS)

    def _action_sets_default(self):
        """ Trait initializer. """

        from action_set import ActionSet

        return [ActionSet]
