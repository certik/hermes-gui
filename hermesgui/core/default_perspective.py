from enthought.pyface.workbench.api import Perspective, PerspectiveItem


class DefaultPerspective(Perspective):
    """ An example perspective. """

    # The perspective's name.
    name = 'Default'

    # Should the editor area be shown in this perspective?
    show_editor_area = False

    # The contents of the perspective.
    contents = [
        PerspectiveItem(id='Problem',  position='left'),
        PerspectiveItem(id='Scene',  position='right', relative_to="Problem"),
        PerspectiveItem(id='Local Values',  position='right'),
        PerspectiveItem(id='Volume Integral',   position='bottom',
            relative_to='Local Values'),
        PerspectiveItem(id='Surface Integral', position='bottom',
            relative_to="Volume Integral")
    ]
