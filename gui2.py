#! /usr/bin/env python

from enthought.traits.api import (Int, HasTraits, Enum, CInt, String, Instance,
        Str)
from enthought.traits.ui.api import (View, Item, HSplit, VSplit, TreeEditor,
        TreeNode, ToolBar, Action)
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

    def get_view(self):
        return View(
                toolbar = ToolBar(self.my_action))


if __name__ == '__main__':
    main_window = MainWindow()
    main_window.configure_traits(view=main_window.get_view())
