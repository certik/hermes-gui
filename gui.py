#! /usr/bin/env python

from enthought.traits.api import (Int, HasTraits, Enum, CInt, String, Instance,
        Str)
from enthought.traits.ui.api import (View, Item, HSplit, VSplit, TreeEditor,
        TreeNode)
from enthought.traits.ui.menu import NoButtons
from enthought.pyface.image_resource import ImageResource
from enthought.pyface.api import ApplicationWindow, GUI, PythonShell
from enthought.traits.ui.api import CustomEditor
from enthought.pyface.action.api import (Action, MenuManager, MenuBarManager,
        StatusBarManager, ToolBarManager, Group, Separator)

from enthought.traits.api import HasTraits, Str, Regex, List, Instance
from enthought.traits.ui.api import Item, View, TreeEditor, TreeNode

class MainWindow(ApplicationWindow):
    """ The main application window. """

    def __init__(self, container, **traits):
        """ Creates a new application window. """
        super(MainWindow, self).__init__(**traits)
        self._container = container

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

    def create_new(self):
        self._container.configure_traits()

    def _create_contents(self, parent):
        self._python_shell = python_shell = PythonShell(parent)
        return python_shell.control

class NodeProblem(HasTraits):
    name = Str("NodeProblem")

class NodeBC(HasTraits):
    name = Str("Boundary cond")

class NodeMaterials(HasTraits):
    name = Str("Boundary cond")

no_view = View()



class Employee ( HasTraits ):
    """ Defines a company employee. """

    name  = Str( '<unknown>' )
    title = Str
    phone = Regex( regex = r'\d\d\d-\d\d\d\d' )

    def default_title ( self ):
        self.title = 'Senior Engineer'

class Department ( HasTraits ):
    """ Defines a department with employees. """

    name      = Str( '<unknown>' )
    employees = List( Employee )

class Company ( HasTraits ):
    """ Defines a company with departments and employees. """

    name        = Str( '<unknown>' )
    departments = List( Department )
    employees   = List( Employee )

# Create an empty view for objects that have no data to display:
no_view = View()

# Define the TreeEditor used to display the hierarchy:
tree_editor = TreeEditor(
    nodes = [
        TreeNode( node_for  = [ Company ],
                  auto_open = True,
                  children  = '',
                  label     = 'name',
                  view      = View( [ 'name' ] )
        ),
        TreeNode( node_for  = [ Company ],
                  auto_open = True,
                  children  = 'departments',
                  label     = '=Departments',
                  view      = no_view,
                  add       = [ Department ],
        ),
        TreeNode( node_for  = [ Company ],
                  auto_open = True,
                  children  = 'employees',
                  label     = '=Employees',
                  view      = no_view,
                  add       = [ Employee ]
        ),
        TreeNode( node_for  = [ Department ],
                  auto_open = True,
                  children  = 'employees',
                  label     = 'name',
                  view      = View( [ 'name' ] ),
                  add       = [ Employee ]
        ),
        TreeNode( node_for  = [ Employee ],
                  auto_open = True,
                  label     = 'name',
                  view      = View( [ 'name', 'title', 'phone' ] )
        )
    ]
)

class Problem(HasTraits):
    company = Instance( Company )

    view = View(
        Item( name       = 'company',
              editor     = tree_editor,
              show_label = False
        ),
        title     = 'Problem',
        buttons   = [ 'OK' ],
        resizable = True,
        style     = 'custom',
        width     = .3,
        height    = .3
    )


class LocalValues(HasTraits):
    string = String()

    view= View( Item('string', show_label=False, springy=True, style='custom' ))

class VolumeIntegral(HasTraits):
    string = String()

    view= View( Item('string', show_label=False, springy=True, style='custom' ))

class SurfaceIntegral(HasTraits):
    string = String()

    view= View( Item('string', show_label=False, springy=True, style='custom' ))

class Container(HasTraits):
    problem = Instance(Problem)
    local_values = Instance(LocalValues)
    volume_integral = Instance(VolumeIntegral)
    surface_integral = Instance(SurfaceIntegral)

    view = View(HSplit(
                Item('problem', style='custom', show_label=False),
                VSplit(
                    Item('local_values', style='custom'),
                    Item('volume_integral', style='custom'),
                    Item('surface_integral', style='custom'),
                    )
                ),
                resizable=True,
            )


if __name__ == '__main__':
    gui = GUI()

    jason  = Employee( name  = 'Jason',
                       title = 'Senior Engineer',
                       phone = '536-1057' )
    mike   = Employee( name  = 'Mike',
                       title = 'Senior Engineer',
                       phone = '536-1057' )
    dave   = Employee( name  = 'Dave',
                       title = 'Senior Software Developer',
                       phone = '536-1057' )
    martin = Employee( name  = 'Martin',
                       title = 'Senior Engineer',
                       phone = '536-1057' )
    duncan = Employee( name  = 'Duncan',
                       title = 'Consultant',
                       phone = '526-1057' )

    problem = Problem(
        company = Company(
            name        = 'Enthought',
            employees   = [ dave, martin, duncan, jason, mike ],
            departments = [
                Department(
                    name      = 'Business',
                    employees = [ jason, mike ]
                ),
                Department(
                    name      = 'Scientific',
                    employees = [ dave, martin, duncan ]
                )
            ]
        )
    )


    container = Container(problem=problem,
            local_values=LocalValues(),
            volume_integral=VolumeIntegral(),
            surface_integral=SurfaceIntegral(),
            )

    window = MainWindow(container)
    window.open()


    gui.start_event_loop()
