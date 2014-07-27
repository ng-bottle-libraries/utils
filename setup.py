from setuptools import setup, find_packages
from namespace_utils import __version__

if __name__ == '__main__':
    project_name = 'namespace_utils'
    setup(name=project_name,
          version=__version__,
          author='Samuel Marks',
          author_email='samuelmarks@gmail.com',
          package_dir={project_name: project_name},
          packages=find_packages(),
          license='MIT',
          test_suite=project_name + '.tests')
