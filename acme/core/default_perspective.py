from enthought.pyface.workbench.api import Perspective, PerspectiveItem


class DefaultPerspective(Perspective):
    """ An example perspective. """

    # The perspective's name.
    name = 'Default'

    # Should the editor area be shown in this perspective?
    show_editor_area = True

    # The contents of the perspective.
    contents = [
        PerspectiveItem(id='Problem',  position='left'),
        PerspectiveItem(id='Local Values',  position='left'),
        PerspectiveItem(id='Volume Integral',   position='with',
            relative_to='Local Values'),
        PerspectiveItem(id='Surface Integral', position='top')
    ]
