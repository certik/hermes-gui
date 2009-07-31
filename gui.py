#! /usr/bin/env python

import wx
import sys

from enthought.pyface.api import ApplicationWindow, GUI
from enthought.pyface.action.api import Action, MenuManager, MenuBarManager
from enthought.pyface.action.api import StatusBarManager, ToolBarManager

from enthought.traits.api import *
from enthought.traits.ui.api import *
from enthought.traits.ui.menu import *
from enthought.pyface.dock.api import *
from enthought.pyface.image_resource import ImageResource

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

    ###########################################################################
    # 'object' interface.
    ###########################################################################

    def __init__(self, **traits):
        """ Creates a new application window. """
        super(MainWindow, self).__init__(**traits)

        exit_action = Action(name='E&xit', on_perform=self.close)

        self.menu_bar_manager = MenuBarManager(
            MenuManager(
                Action(name='New...'),
                Action(name='Open...'),
                Action(name='Save...'),
                Action(name='Save as...'),
                Action(name='Close'),
                Separator(),
                Action(name='Import DXF...'),
                Action(name='Export DXF...'),
                Separator(),
                Action(name='Export image...'),
                Separator(),
                Action(name='Recent files ->'),
                exit_action,
                name='&File')
        )

        self.tool_bar_managers = [
            ToolBarManager(
                exit_action, name='Tool Bar 1', show_tool_names=False
            ),

            ToolBarManager(
                exit_action, name='Tool Bar 2', show_tool_names=False
            ),

            ToolBarManager(
                exit_action, name='Tool Bar 3', show_tool_names=False
            ),
        ]

        self.status_bar_manager = StatusBarManager()
        self.status_bar_manager.message = 'Example application window'

        return

class App(HasPrivateTraits):
    dummy = Int

    view = View( [ Item( 'dummy',
                         resizable = True,
                         editor    = CustomEditor(create_dock_window) ),
                   '|<>' ],
                 title     = 'DockWindow Test',
                 resizable = True,
                 width     = 0.5,
                 height    = 0.5,
                 buttons   = NoButtons )

if __name__ == '__main__':
    #App().configure_traits()
    gui = GUI()

    window = MainWindow()
    window.open()

    gui.start_event_loop()
