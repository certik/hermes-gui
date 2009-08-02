""" Run the AcmeLab example application. """


# Standard library imports.
import logging

# Example imports.
from acme.acmelab.api import Acmelab

# Enthought plugins.
from enthought.envisage.core_plugin import CorePlugin
from enthought.envisage.developer.developer_plugin import DeveloperPlugin
from enthought.envisage.developer.ui.developer_ui_plugin import DeveloperUIPlugin
from enthought.envisage.ui.workbench.workbench_plugin import WorkbenchPlugin

from acme.core.core_plugin import HermesPlugin


# Do whatever you want to do with log messages! Here we create a log file.
logger = logging.getLogger()
#logger.addHandler(logging.StreamHandler(file('acmelab.log', 'w')))
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


def main():
    """ Run the application. """

    # Create an application with the specified plugins.
    acmelab = Acmelab(
        plugins=[
            CorePlugin(),
            WorkbenchPlugin(),
            #AcmeWorkbenchPlugin(),
            HermesPlugin(),
            #DeveloperPlugin(),
            #DeveloperUIPlugin()
        ]
    )

    # Run it! This starts the application, starts the GUI event loop, and when
    # that terminates, stops the application.
    acmelab.run()

    return


if __name__ == '__main__':
    main()

#### EOF ######################################################################
