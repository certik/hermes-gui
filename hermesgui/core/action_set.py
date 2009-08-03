import os
import new

from enthought.envisage.ui.action.api import Action, Group, Menu, ToolBar
from enthought.envisage.ui.workbench.api import WorkbenchActionSet

from enthought.pyface.action.api import Action as PAction
from enthought.pyface.api import FileDialog, OK

from utils import image_resource, get_data_dir
from handle_hermes import read_mesh, poisson_solver
from handle_agros import read_a2d


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

class OpenAction(PAction):
    name='&Open...'
    accelerator="CTRL+O"
    image=image_resource("document-open.png")

    def perform(self, event):
        wildcard="|".join([
            "All files (*.*)", "*.*",
            "Hermes2D mesh files (*.mesh)", "*.mesh",
            "Agros2D problem files (*.a2d)", "*.a2d",
            ])
        dialog = FileDialog(parent=None, title='Open supported data file',
                            action='open', wildcard=wildcard,
                            # use this to have Hermes2D by default:
                            #wildcard_index=1,
                            wildcard_index=0,
                            default_directory=get_data_dir(),
                            #default_filename="lshape.mesh",
                            )
        if dialog.open() == OK:
            ext = os.path.splitext(dialog.path)[1]
            if ext == ".a2d":
                scene = event.window.get_view_by_id("Problem")
                p, g = read_a2d(dialog.path)
                scene.problem = p
                scene.geometry = g
            else:
                scene = event.window.get_view_by_id("Scene")
                mesh = read_mesh(dialog.path)
                scene.mesh = mesh
                scene.mode = "mesh"

class SolveProblem(PAction):
    name='Solve problem'
    accelerator="Alt+S"
    image=image_resource("system-run.png")

    def perform(self, event):
        scene = event.window.get_view_by_id("Scene")
        if scene.mesh:
            sln = poisson_solver(scene.mesh)
            scene.sln = sln
            scene.mode = "solution"

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
zoom_actions1 = [
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
zoom_actions2 = [MAction(name="Fullscreen mode", accelerator="F11")]
zoom_actions3 = [MAction(name="&Scene properties",
                    image=image_resource("scene-properties.png"))]

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
    SolveProblem,
    ]
problem_actions5 = [
    MAction(name="Problem properties",
        image=image_resource("scene-properties.png")),
    ]


class ActionSet(WorkbenchActionSet):
    id = 'enthought.envisage.ui.workbench.test'

    menus = [
        Menu(name='&Edit', path='MenuBar', after="File"),
        Menu(name='&View', path='MenuBar', after="Edit"),
        Menu(name='&Problem', path='MenuBar', after="View"),
            Menu(name='Add', path='MenuBar/Problem', group="problem_add"),
    ]

    groups = [

        Group(id='problem_actions1', path='MenuBar/Problem'),
        Group(id='problem_add', path='MenuBar/Problem'),
        Group(id='problem_actions2', path='MenuBar/Problem'),
        Group(id='problem_actions3', path='MenuBar/Problem'),
        Group(id='problem_actions4', path='MenuBar/Problem'),
        Group(id='problem_actions5', path='MenuBar/Problem'),

        Group(id='zoom_actions1', path='MenuBar/View'),
        Group(id='zoom_actions2', path='MenuBar/View'),
        Group(id='zoom_actions3', path='MenuBar/View'),
    ]

    tool_bars = [
        ToolBar(name='File'),
        ToolBar(name='Zoom',
            groups=["zoom_actions1"]),
        ToolBar(name='Problem',
            groups=["problem_actions1", "problem_actions2",
                "problem_actions3", "problem_actions4"]),
    ]

    actions = [
        Action(path='ToolBar/Problem', group="problem_actions1",
            class_name="hermesgui.core.action_set:problem_actions1[0]"),
        Action(path='ToolBar/Problem', group="problem_actions1",
            class_name="hermesgui.core.action_set:problem_actions1[1]"),
        Action(path='ToolBar/Problem', group="problem_actions1",
            class_name="hermesgui.core.action_set:problem_actions1[2]"),
        Action(path='ToolBar/Problem', group="problem_actions1",
            class_name="hermesgui.core.action_set:problem_actions1[3]"),

        Action(path="ToolBar/Problem", group="problem_actions2",
            class_name="hermesgui.core.action_set:problem_actions2[0]"),
        Action(path="ToolBar/Problem", group="problem_actions2",
            class_name="hermesgui.core.action_set:problem_actions2[1]"),

        Action(path="ToolBar/Problem", group="problem_actions3",
            class_name="hermesgui.core.action_set:problem_actions3[0]"),
        Action(path="ToolBar/Problem", group="problem_actions3",
            class_name="hermesgui.core.action_set:problem_actions3[1]"),
        Action(path="ToolBar/Problem", group="problem_actions3",
            class_name="hermesgui.core.action_set:problem_actions3[2]"),

        Action(path="ToolBar/Problem", group="problem_actions4",
            class_name="hermesgui.core.action_set:problem_actions4[0]"),
        Action(path="ToolBar/Problem", group="problem_actions4",
            class_name="hermesgui.core.action_set:problem_actions4[1]"),

        Action(path="MenuBar/Problem", group="problem_actions1",
            class_name="hermesgui.core.action_set:problem_actions1[0]"),
        Action(path="MenuBar/Problem", group="problem_actions1",
            class_name="hermesgui.core.action_set:problem_actions1[1]"),
        Action(path="MenuBar/Problem", group="problem_actions1",
            class_name="hermesgui.core.action_set:problem_actions1[2]"),
        Action(path="MenuBar/Problem", group="problem_actions1",
            class_name="hermesgui.core.action_set:problem_actions1[3]"),

        Action(path="MenuBar/Problem", group="problem_actions2",
            class_name="hermesgui.core.action_set:problem_actions2[0]"),
        Action(path="MenuBar/Problem", group="problem_actions2",
            class_name="hermesgui.core.action_set:problem_actions2[1]"),

        Action(path="MenuBar/Problem", group="problem_actions3",
            class_name="hermesgui.core.action_set:problem_actions3[0]"),
        Action(path="MenuBar/Problem", group="problem_actions3",
            class_name="hermesgui.core.action_set:problem_actions3[1]"),
        Action(path="MenuBar/Problem", group="problem_actions3",
            class_name="hermesgui.core.action_set:problem_actions3[2]"),

        Action(path="MenuBar/Problem", group="problem_actions4",
            class_name="hermesgui.core.action_set:problem_actions4[0]"),
        Action(path="MenuBar/Problem", group="problem_actions4",
            class_name="hermesgui.core.action_set:problem_actions4[1]"),

        Action(path="MenuBar/Problem", group="problem_actions5",
            class_name="hermesgui.core.action_set:problem_actions5[0]"),


        Action(path="MenuBar/View", group="zoom_actions1",
            class_name="hermesgui.core.action_set:zoom_actions1[0]"),
        Action(path="MenuBar/View", group="zoom_actions1",
            class_name="hermesgui.core.action_set:zoom_actions1[1]"),
        Action(path="MenuBar/View", group="zoom_actions1",
            class_name="hermesgui.core.action_set:zoom_actions1[2]"),
        Action(path="MenuBar/View", group="zoom_actions1",
            class_name="hermesgui.core.action_set:zoom_actions1[3]"),

        Action(path="ToolBar/Zoom", group="zoom_actions1",
            class_name="hermesgui.core.action_set:zoom_actions1[0]"),
        Action(path="ToolBar/Zoom", group="zoom_actions1",
            class_name="hermesgui.core.action_set:zoom_actions1[1]"),
        Action(path="ToolBar/Zoom", group="zoom_actions1",
            class_name="hermesgui.core.action_set:zoom_actions1[2]"),
        Action(path="ToolBar/Zoom", group="zoom_actions1",
            class_name="hermesgui.core.action_set:zoom_actions1[3]"),

        Action(path="MenuBar/File",
            class_name="hermesgui.core.action_set:new_action"),
        Action(path="MenuBar/File",
            class_name="hermesgui.core.action_set:OpenAction"),
        Action(path="MenuBar/File",
            class_name="hermesgui.core.action_set:save_action"),

        Action(path="ToolBar/File",
            class_name="hermesgui.core.action_set:new_action"),
        Action(path="ToolBar/File",
            class_name="hermesgui.core.action_set:OpenAction"),
        Action(path="ToolBar/File",
            class_name="hermesgui.core.action_set:save_action"),
    ]