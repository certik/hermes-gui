#! /usr/bin/env python

from enthought.traits.api import Int, HasTraits
from enthought.traits.ui.api import View, Item
from enthought.traits.ui.menu import NoButtons
from enthought.pyface.image_resource import ImageResource
from enthought.pyface.api import ApplicationWindow, GUI
from enthought.traits.ui.api import CustomEditor
from enthought.pyface.action.api import (Action, MenuManager, MenuBarManager,
        StatusBarManager, ToolBarManager, Group, Separator)

# DockControl style to use:
style1 = 'horizontal'
style2 = 'vertical'

image1 = ImageResource( 'folder' )
image2 = ImageResource( 'gear' )

def create_dock_window ( parent, editor ):
    """ Creates a window for editing a workflow canvas.
    """
    window  = DockWindow( parent ).control
    button1 = wx.Button( window, -1, 'Button 1' )
    button2 = wx.Button( window, -1, 'Button 2' )
    button3 = wx.Button( window, -1, 'Button 3' )
    button4 = wx.Button( window, -1, 'Button 4' )
    button5 = wx.Button( window, -1, 'Button 5' )
    button6 = wx.Button( window, -1, 'Button 6' )
    sizer   = DockSizer( contents =
                  [ DockControl( name      = 'Button 1',
                                 image     = image1,
                                 closeable = True,
                                 control   = button1,
                                 style     = style1 ),
                    [ DockControl( name      = 'Button 2',
                                   image     = image1,
                                   closeable = True,
                                   height    = 400,
                                   control   = button2,
                                   style   = style1 ),
                      ( [ DockControl( name      = 'Button 3',
                                     image     = image2,
                                     resizable = False,
                                       control   = button3,
                                       style     = style2 ),
                          DockControl( name      = 'Button 4',
                                       image     = image2,
                                       resizable = False,
                                       control   = button4,
                                       style     = style2 ) ],
                        [  DockControl( name      = 'Button 5',
                                       resizable = False,
                                       control   = button5,
                                       style     = style2 ),
                          DockControl( name      = 'Button 6',
                                       resizable = False,
                                       control   = button6,
                                       style     = style2 ) ] )
                    ]
                  ] )
    window.SetSizer( sizer )
    window.SetAutoLayout( True )

    return window

class MainWindow(ApplicationWindow):
    """ The main application window. """

    def __init__(self, **traits):
        """ Creates a new application window. """
        super(MainWindow, self).__init__(**traits)

        exit_action = Action(
                name='E&xit',
                on_perform=self.close,
                image=ImageResource("images/application-exit.png"),
                tooltip="Exit the application"
                )

        new_action = Action(
                name='New...',
                image=ImageResource("images/document-new.png")
                )
        open_action = Action(
                name='Open...',
                image=ImageResource("images/document-open.png")
                )
        save_action = Action(
                name='Save...',
                image=ImageResource("images/document-save.png")
                )
        zoom_actions = [
            Action(name='Zoom best fit',
                image=ImageResource("images/zoom-best-fit.png")),
            Action(name='Zoom region',
                image=ImageResource("images/zoom-region.png")),
            Action(name='Zoom in',
                image=ImageResource("images/zoom-in.png")),
            Action(name='Zoom out',
                image=ImageResource("images/zoom-out.png")),
            ]
        problem_actions1 = [
            Action(name='Operate on &nodes',
                image=ImageResource("images/scene-node.png")),
            Action(name='Operate on &edges',
                image=ImageResource("images/scene-edge.png")),
            Action(name='Operate on &labels',
                image=ImageResource("images/scene-label.png")),
            Action(name='Postprocessor',
                image=ImageResource("images/scene-postprocessor.png")),
            ]
        problem_actions2 = [
            Action(name='Select region',
                image=ImageResource("images/scene-node.png")),
            Action(name='Transform',
                image=ImageResource("images/scene-edge.png")),
            ]
        problem_actions3 = [
            Action(name='Local Values',
                image=ImageResource("images/scene-node.png")),
            Action(name='Surface Integrals',
                image=ImageResource("images/scene-edge.png")),
            Action(name='Volume Integrals',
                image=ImageResource("images/scene-edge.png")),
            ]
        problem_actions4 = [
            Action(name='Mesh area',
                image=ImageResource("images/scene-node.png")),
            Action(name='Solve problem',
                image=ImageResource("images/scene-edge.png")),
            ]

        self.menu_bar_manager = MenuBarManager(
            MenuManager(
                Group(
                    new_action,
                    open_action,
                    save_action,
                    Action(name='Save as...',
                        image=ImageResource("images/document-save-as.png")),
                    Action(name='Close'),
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
            MenuManager(
                Group(
                    Action(name='Paste',
                        image=ImageResource("images/edit-paste.png"))
                    ),
                Group( Action(name='Options') ),
                name='&Edit'),
            MenuManager(
                Group(*zoom_actions),
                Group(Action(name="Fullscreen mode")),
                Group(Action(name="Scene properties")),
                name='&View'),
            MenuManager(
                Group(*problem_actions1),
                Group(Action(name="Add ->")),
                Group(*problem_actions2),
                Group(*problem_actions3),
                Group(*problem_actions4),
                Group(Action(name="Problem properties")),
                name='&Problem'),
            MenuManager(
                Action(name='Options'),
                name='Tools'),
            MenuManager(
                Group(
                    Action(name='Help'),
                    Action(name='Shortcuts'),
                ),
                Group(
                    Action(name='About Hermes-gui'),
                    Action(name='About Traits'),
                ),
                name='&Help'),
        )

        self.tool_bar_managers = [
            ToolBarManager(
                Group(*problem_actions1),
                Group(*problem_actions2),
                Group(*problem_actions3),
                Group(*problem_actions4),
                name='Problem Tool Bar', show_tool_names=False
            ),
            ToolBarManager(
                *zoom_actions,
                name='Zoom Tool Bar', show_tool_names=False
            ),
            ToolBarManager(
                new_action,
                open_action,
                save_action,
                name='File Tool Bar', show_tool_names=False
            ),

        ]

        self.status_bar_manager = StatusBarManager()
        self.status_bar_manager.message = 'Example application window'

        return

    def _create_contents(self, parent):
        editor    = CustomEditor(create_dock_window)
        return ApplicationWindow._create_contents(self, parent)

if __name__ == '__main__':
    gui = GUI()

    window = MainWindow()
    window.open()

    gui.start_event_loop()
