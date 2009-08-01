#! /usr/bin/env python

from enthought.traits.api import (Int, HasTraits, Enum, CInt, String, Instance,
        Str)
from enthought.traits.ui.api import (View, Item, HSplit, VSplit, TreeEditor,
        TreeNode, ToolBar, Action, MenuBar, Menu, Group, Separator)
from enthought.pyface.image_resource import ImageResource
from enthought.traits.ui.api import CustomEditor

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
                action="close",
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

                    Action(name='Import DXF...'),
                    Action(name='Export DXF...'),

                    Action(name='Export image...'),

                    Action(name='Recent files ->'),
                    exit_action,
                name='&File'),
        )

    def get_view(self):
        return View(
                menubar = self.menu_bar_manager,
                )

    def close(uiinfo):
        print "close myself"

    def create_new(self):
        pass


if __name__ == '__main__':
    main_window = MainWindow()
    main_window.configure_traits(view=main_window.get_view())
