from setuptools import setup, find_packages

setup(name='command-timeout',
      version='1.0',
      description='Timeout Commands',
      author='xoviat',
      author_email='xoviat@noreply.users.github.com',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'command-timeout = command-timeout.__main__:main'
          ]
      },
     )
