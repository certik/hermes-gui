#! /usr/bin/env python

from enthought.traits.api import (Int, HasTraits, Enum, CInt, String, Instance,
        Str)
from enthought.traits.ui.api import (View, Item, HSplit, VSplit, TreeEditor,
        TreeNode, ToolBar, Action, MenuBar, Menu)
from enthought.traits.ui.menu import NoButtons
from enthought.pyface.image_resource import ImageResource
from enthought.pyface.api import ApplicationWindow, GUI, PythonShell
from enthought.traits.ui.api import CustomEditor
from enthought.pyface.action.api import (MenuManager, MenuBarManager,
        StatusBarManager, ToolBarManager, Group, Separator)

from enthought.traits.api import HasTraits, Str, Regex, List, Instance
from enthought.traits.ui.api import Item, View, TreeEditor, TreeNode

class MainWindow(HasTraits):
    """ The main application window. """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.my_action = Action(name="stuff")
        exit_action = Action(
                name='E&xit',
                accelerator="CTRL+Q",
                on_perform=self.close,
                image=ImageResource("images/application-exit.png"),
                tooltip="Exit the application"
                )

        new_action = Action(
                name='&New...',
                accelerator="CTRL+N",
                on_perform=self.create_new,
                image=ImageResource("images/document-new.png")
                )
        open_action = Action(
                name='&Open...',
                accelerator="CTRL+O",
                image=ImageResource("images/document-open.png")
                )
        save_action = Action(
                name='&Save',
                accelerator="CTRL+S",
                image=ImageResource("images/document-save.png")
                )
        zoom_actions = [
            Action(name='Zoom best fit',
                image=ImageResource("images/zoom-best-fit.png")),
            Action(name='Zoom region',
                image=ImageResource("images/zoom-region.png")),
            Action(name='Zoom in',
                accelerator="Ctrl++",
                image=ImageResource("images/zoom-in.png")),
            Action(name='Zoom out',
                accelerator="Ctrl+-",
                image=ImageResource("images/zoom-out.png")),
            ]
        problem_actions1 = [
            Action(name='Operate on &nodes',
                accelerator="F5",
                image=ImageResource("images/scene-node.png")),
            Action(name='Operate on &edges',
                accelerator="F6",
                image=ImageResource("images/scene-edge.png")),
            Action(name='Operate on &labels',
                accelerator="F7",
                image=ImageResource("images/scene-label.png")),
            Action(name='&Postprocessor',
                accelerator="F8",
                image=ImageResource("images/scene-postprocessor.png")),
            ]
        problem_actions2 = [
            Action(name='Select region',
                image=ImageResource("images/scene-select-region.png")),
            Action(name='Transform',
                image=ImageResource("images/scene-transform.png")),
            ]
        problem_actions3 = [
            Action(name='Local Values',
                image=ImageResource("images/mode-localpointvalue.png")),
            Action(name='Surface Integrals',
                image=ImageResource("images/mode-surfaceintegral.png")),
            Action(name='Volume Integrals',
                image=ImageResource("images/mode-volumeintegral.png")),
            ]
        problem_actions4 = [
            Action(name='Mesh area',
                image=ImageResource("images/scene-mesh.png")),
            Action(name='Solve problem',
                accelerator="Alt+S",
                image=ImageResource("images/system-run.png")),
            ]

        self.menu_bar_manager = MenuBar(
            Menu(
                Group(
                    new_action,
                    open_action,
                    save_action,
                    Action(name='Save &As...',
                        accelerator="Ctrl+Shift+S",
                        image=ImageResource("images/document-save-as.png")),
                    Action(name='Close',
                        accelerator="Ctrl+W"),
                ),
                Group(
                    Action(name='Import DXF...'),
                    Action(name='Export DXF...'),
                ),
                Group(
                    Action(name='Export image...'),
                ),
                Group(
                    Action(name='Recent files ->'),
                    exit_action,
                ),
                name='&File'),
            Menu(
                Group(
                    Action(name='&Paste',
                        accelerator="Ctrl+V",
                        image=ImageResource("images/edit-paste.png"))
                    ),
                Group(
                    Action(name='Options',
                        image=ImageResource("images/options.png"))
                    ),
                name='&Edit'),
            Menu(
                Group(*zoom_actions),
                Group(Action(name="Fullscreen mode", accelerator="F11")),
                Group(Action(name="&Scene properties",
                    image=ImageResource("images/scene-properties.png"))),
                name='&View'),
            Menu(
                Group(*problem_actions1),
                Group(Action(name="Add ->")),
                Group(*problem_actions2),
                Group(*problem_actions3),
                Group(*problem_actions4),
                Group(Action(name="Problem properties",
                    image=ImageResource("images/scene-properties.png"))),
                name='&Problem'),
            Menu(
                Group(
                    Action(name='Chart',
                        image=ImageResource("images/chart.png")),
                    ),
                Group(
                    Action(name='Startup script',
                        image=ImageResource("images/script-startup.png")),
                    Action(name='Script editor',
                        image=ImageResource("images/script.png"))
                ),
                name='Tools'),
            Menu(
                Group(
                    Action(name='&Help',
                        accelerator="F1",
                        image=ImageResource("images/help-browser.png")),
                    Action(name='Shortcuts'),
                ),
                Group(
                    Action(name='&About Hermes-gui',
                        image=ImageResource("images/about.png")),
                    Action(name='About &Traits'),
                ),
                name='&Help'),
        )

        self.tool_bar_managers = [
            ToolBar(
                Group(*problem_actions1),
                Group(*problem_actions2),
                Group(*problem_actions3),
                Group(*problem_actions4),
                name='Problem Tool Bar', show_tool_names=False
            ),
            ToolBar(
                *zoom_actions,
                name='Zoom Tool Bar', show_tool_names=False
            ),
            ToolBar(
                new_action,
                open_action,
                save_action,
                name='File Tool Bar', show_tool_names=False
            ),

        ]

    def get_view(self):
        return View(
                menubar = self.menu_bar_manager,
                toolbar = self.tool_bar_managers[0])

    def close(self):
        print "close myself"

    def create_new(self):
        pass


if __name__ == '__main__':
    main_window = MainWindow()
    main_window.configure_traits(view=main_window.get_view())
