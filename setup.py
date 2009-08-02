from distutils.core import setup
setup(name='hermes-gui',
      version='0.1',
      packages=[
          'hermesgui',
          'hermesgui.acmelab',
          'hermesgui.core',
          'hermesgui.core.views',
          ],
      package_data={
          'hermesgui.acmelab': ['images/*'],
          'hermesgui.core': ['images/*.png'],
          },
      scripts = ['hermes-gui.py'],
      )
