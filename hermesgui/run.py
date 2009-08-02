# delete the configuration, so that we can easily develop without any "caching"
# effects:
import os
os.system("rm -rf ~/.enthought/acme.acmelab/")

import sys
from enthought.etsconfig.api import ETSConfig
if (len(sys.argv) > 1) and (sys.argv[1] == "--qt" or sys.argv[1] == "--qt4"):
    ETSConfig.toolkit = "qt4"
elif (len(sys.argv) > 1) and (sys.argv[1] == "--wx"):
    ETSConfig.toolkit = "wx"
else:
    try:
        import PyQt4
        ETSConfig.toolkit = "qt4"
    except ImportError:
        pass

# Standard library imports.
import logging

# Example imports.
from hermesgui.acmelab.api import Acmelab

# Enthought plugins.
from enthought.envisage.core_plugin import CorePlugin
from enthought.envisage.developer.developer_plugin import DeveloperPlugin
from enthought.envisage.developer.ui.developer_ui_plugin import DeveloperUIPlugin
from enthought.envisage.ui.workbench.workbench_plugin import WorkbenchPlugin

from hermesgui.core.core_plugin import HermesPlugin


# Do whatever you want to do with log messages! Here we create a log file.
logger = logging.getLogger()
#logger.addHandler(logging.StreamHandler(file('acmelab.log', 'w')))
logger.addHandler(logging.StreamHandler())
#logger.setLevel(logging.DEBUG)


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

    acmelab.workbench.prompt_on_exit = False

    # Run it! This starts the application, starts the GUI event loop, and when
    # that terminates, stops the application.
    acmelab.run()

    return
