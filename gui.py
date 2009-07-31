#! /usr/bin/env python

from enthought.pyface.image_resource import ImageResource
from enthought.pyface.api import ApplicationWindow, GUI
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
                Action(name='Options'),
                name='&View'),
            MenuManager(
                Action(name='Options'),
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
                exit_action, name='Tool Bar 3', show_tool_names=False
            ),
            ToolBarManager(
                exit_action, name='Tool Bar 2', show_tool_names=False
            ),
            ToolBarManager(
                new_action,
                open_action,
                save_action,
                name='Tool Bar 1', show_tool_names=False
            ),

        ]

        self.status_bar_manager = StatusBarManager()
        self.status_bar_manager.message = 'Example application window'

        return

#class App(HasPrivateTraits):
#    dummy = Int
#
#    view = View( [ Item( 'dummy',
#                         resizable = True,
#                         editor    = CustomEditor(create_dock_window) ),
#                   '|<>' ],
#                 title     = 'DockWindow Test',
#                 resizable = True,
#                 width     = 0.5,
#                 height    = 0.5,
#                 buttons   = NoButtons )

if __name__ == '__main__':
    #App().configure_traits()
    gui = GUI()

    window = MainWindow()
    window.open()

    gui.start_event_loop()
