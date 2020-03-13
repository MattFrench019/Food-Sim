from setuptools import setup, find_packages

setup(
    name='matts-food-sim',
    version='1.0.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description="Python package for simulating a town's food consumption",
    long_description=open('README.md').read(),
    install_requires=[],
    url='https://github.com/MattFrench019/Food-Sim',
    author='Matt French',
    author_email='matt@mfrench.net'
)