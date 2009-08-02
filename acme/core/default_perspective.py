from enthought.pyface.workbench.api import Perspective, PerspectiveItem


class DefaultPerspective(Perspective):
    """ An example perspective. """

    # The perspective's name.
    name = 'Default'

    # Should the editor area be shown in this perspective?
    show_editor_area = True

    # The contents of the perspective.
    contents = [
        PerspectiveItem(id='Blue',  position='left'),
        PerspectiveItem(id='Red',   position='with', relative_to='Blue'),
        PerspectiveItem(id='Green', position='top')
    ]
