from setuptools import setup, find_packages

setup(
    name='mypackage',
    packages=find_packages(exclude=['test*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/williaby78/mypackage',
    author='Bryan Williams',
    author_email='bfha.williams@gmail.com'
)