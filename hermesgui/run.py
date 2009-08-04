# delete the configuration, so that we can easily develop without any "caching"
# effects:
import os
os.system("rm -rf ~/.enthought/acme.acmelab/")

import sys
from optparse import OptionParser

from enthought.etsconfig.api import ETSConfig

usage = "usage: %prog [options]"
description = """\
Python based GUI for Hermes.\
"""
parser = OptionParser(usage=usage, description=description)
parser.add_option("--qt", "--qt4", action="store_true", dest="qt4",
        default=False, help="Run with the QT4 toolkit")
parser.add_option("--wx", action="store_true", dest="wx",
        default=False, help="Run with the wxWidgets (GTK) toolkit")
options, args = parser.parse_args()
if options.qt4 and options.wx:
    parser.error("options --wx and --qt4 are mutually exclusive")
if options.qt4:
    ETSConfig.toolkit = "qt4"
elif options.wx:
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
