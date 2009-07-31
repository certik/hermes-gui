#! /usr/bin/env python

from enthought.traits.api import Int, HasTraits, Enum, CInt, String, Instance
from enthought.traits.ui.api import View, Item, HSplit, VSplit
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
                accelerator="CTRL+Q",
                on_perform=self.close,
                image=ImageResource("images/application-exit.png"),
                tooltip="Exit the application"
                )

        new_action = Action(
                name='&New...',
                accelerator="CTRL+N",
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

        self.menu_bar_manager = MenuBarManager(
            MenuManager(
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
            MenuManager(
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
            MenuManager(
                Group(*zoom_actions),
                Group(Action(name="Fullscreen mode", accelerator="F11")),
                Group(Action(name="&Scene properties",
                    image=ImageResource("images/scene-properties.png"))),
                name='&View'),
            MenuManager(
                Group(*problem_actions1),
                Group(Action(name="Add ->")),
                Group(*problem_actions2),
                Group(*problem_actions3),
                Group(*problem_actions4),
                Group(Action(name="Problem properties",
                    image=ImageResource("images/scene-properties.png"))),
                name='&Problem'),
            MenuManager(
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
            MenuManager(
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
        container = Container(camera=Camera(), display=TextDisplay())
        #editor    = CustomEditor(create_dock_window)
        return ApplicationWindow._create_contents(self, parent)
        #return container


class Camera(HasTraits):
    gain = Enum(1, 2, 3, )
    exposure = CInt(10, label="Exposure", )

class TextDisplay(HasTraits):
    string = String()

    view= View( Item('string', show_label=False, springy=True, style='custom' ))

class Container(HasTraits):
    camera = Instance(Camera)
    display = Instance(TextDisplay)

    view = View(VSplit(
                Item('camera', style='custom', show_label=False, ),
                Item('display', style='custom', show_label=False, ),
                )
            )


if __name__ == '__main__':
    gui = GUI()

    window = MainWindow()
    window.open()

    container = Container(camera=Camera(), display=TextDisplay())
    container.configure_traits()

    gui.start_event_loop()
