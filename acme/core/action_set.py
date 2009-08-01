from enthought.envisage.ui.action.api import Action, Group, Menu, ToolBar
from enthought.envisage.ui.workbench.api import WorkbenchActionSet

from enthought.pyface.action.api import Action as PAction

from utils import image_resource

import new

count = 0
def MAction(**kwargs):
    global count
    count += 1
    return new.classobj("XXX%d" % count, (PAction,), kwargs)

new_action = MAction(
        name='&New...',
        accelerator="CTRL+N",
        image=image_resource("document-new.png")
        )
open_action = MAction(
        name='&Open...',
        accelerator="CTRL+O",
        image=image_resource("document-open.png")
        )
save_action = MAction(
        name='&Save',
        accelerator="CTRL+S",
        description="Saves the problem",
        image=image_resource("document-save.png")
        )

exit_action = MAction(
        name='E&xit',
        accelerator="CTRL+Q",
        #on_perform=self.close,
        image=image_resource("application-exit.png"),
        tooltip="Exit the application"
        )
zoom_actions = [
    MAction(name='Zoom best fit',
        image=image_resource("zoom-best-fit.png")),
    MAction(name='Zoom region',
        image=image_resource("zoom-region.png")),
    MAction(name='Zoom in',
        accelerator="Ctrl++",
        image=image_resource("zoom-in.png")),
    MAction(name='Zoom out',
        accelerator="Ctrl+-",
        image=image_resource("zoom-out.png")),
    ]
problem_actions1 = [
    MAction(name='Operate on &nodes',
        accelerator="F5",
        image=image_resource("scene-node.png")),
    MAction(name='Operate on &edges',
        accelerator="F6",
        image=image_resource("scene-edge.png")),
    MAction(name='Operate on &labels',
        accelerator="F7",
        image=image_resource("scene-label.png")),
    MAction(name='&Postprocessor',
        accelerator="F8",
        image=image_resource("scene-postprocessor.png")),
    ]
problem_actions2 = [
    MAction(name='Select region',
        image=image_resource("scene-select-region.png")),
    MAction(name='Transform',
        image=image_resource("scene-transform.png")),
    ]
problem_actions3 = [
    MAction(name='Local Values',
        image=image_resource("mode-localpointvalue.png")),
    MAction(name='Surface Integrals',
        image=image_resource("mode-surfaceintegral.png")),
    MAction(name='Volume Integrals',
        image=image_resource("mode-volumeintegral.png")),
    ]
problem_actions4 = [
    MAction(name='Mesh area',
        image=image_resource("scene-mesh.png")),
    MAction(name='Solve problem',
        accelerator="Alt+S",
        image=image_resource("system-run.png")),
    ]


class ActionSet(WorkbenchActionSet):
    id = 'enthought.envisage.ui.workbench.test'

    menus = [
        Menu(name='&Edit', path='MenuBar', after="File"),
        Menu(name='&View', path='MenuBar', after="Edit"),
        Menu(name='&Problem', path='MenuBar', after="View"),
            Menu(name='Add', path='MenuBar/Problem'),
    ]

    tool_bars = [
        ToolBar(name='Fred'),
        ToolBar(name='Wilma'),
        ToolBar(name='Barney')
    ]

    actions = [
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
        Action(path="MenuBar/Problem",
            class_name="acme.core.action_set:problem_actions1[0]"),
        Action(path="MenuBar/Problem",
            class_name="acme.core.action_set:problem_actions1[1]"),
        Action(path="MenuBar/Problem",
            class_name="acme.core.action_set:problem_actions1[2]"),
        Action(path="MenuBar/Problem",
            class_name="acme.core.action_set:problem_actions1[3]"),
        #            MenuManager(
        #        Group(*problem_actions1),
        #        Group(Action(name="Add ->")),
        #        Group(*problem_actions2),
        #        Group(*problem_actions3),
        #        Group(*problem_actions4),
        #        Group(Action(name="Problem properties",
        #            image=ImageResource("images/scene-properties.png"))),
        #        name='&Problem'),
    ]
