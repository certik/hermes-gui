from enthought.envisage.ui.action.api import Action, Group, Menu, ToolBar
from enthought.envisage.ui.workbench.api import WorkbenchActionSet

from enthought.pyface.action.api import Action as PAction
from enthought.pyface.image_resource import ImageResource

import new

count = 0
def MAction(**kwargs):
    global count
    count += 1
    return new.classobj("XXX%d" % count, (PAction,), kwargs)

new_action = MAction(
        name='&New...',
        accelerator="CTRL+N",
        image=ImageResource("../../images/document-new.png")
        )
open_action = MAction(
        name='&Open...',
        accelerator="CTRL+O",
        image=ImageResource("../../images/document-open.png")
        )
save_action = MAction(
        name='&Save',
        accelerator="CTRL+S",
        tooltip="Saves the problem1",
        description="Saves the problem2",
        image=ImageResource("../../images/document-save.png")
        )


class ActionSet(WorkbenchActionSet):
    id = 'enthought.envisage.ui.workbench.test'

    menus = [
        Menu(
            name='&Test3', path='MenuBar', before='Help',
        ),

        Menu(
            name='Bar', path='MenuBar/Test3',
        ),
    ]

    groups = [
        Group(id='Fred', path='MenuBar/Test3')
    ]

    tool_bars = [
        ToolBar(name='Fred', groups=['AToolBarGroup']),
        ToolBar(name='Wilma'),
        ToolBar(name='Barney')
    ]

    actions = [
        Action(
            path='MenuBar/Test3', group='Fred',
            class_name='enthought.envisage.ui.workbench.action.api:AboutAction'
        ),

        Action(
            path='MenuBar/Test3', group='Fred',
            class_name='acme.core.action_set:new_action'
        ),

        Action(
            path='MenuBar/Test3', group='Fred',
            class_name='acme.core.action_set:open_action'
        ),

        Action(
            path='MenuBar/Test3', group='Fred',
            class_name='acme.core.action_set:save_action'
        ),

        Action(
            path='ToolBar',
            class_name='enthought.envisage.ui.workbench.action.api:AboutAction'
        ),
        Action(
            path='ToolBar',
            class_name='acme.core.action_set:save_action'
        ),

        Action(
            path='ToolBar',
            class_name='enthought.envisage.ui.workbench.action.api:ExitAction'
        ),
    ]
