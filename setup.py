from setuptools import setup


setup(
    name='relay',
    version='1.0.0',
    author='hspark',
    packages=['relay'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
