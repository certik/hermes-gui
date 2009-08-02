from distutils.core import setup
setup(name='hermes-gui',
      version='0.1',
      packages=[
          'acme',
          'acme.acmelab',
          'acme.core',
          'acme.core.views',
          ],
      package_data={'acme.acmelab': ['images/*']}
      )
