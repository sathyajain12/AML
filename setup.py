from setuptools import setup, find_packages

setup(
    name='aml_project',  # Name of your package
    version='0.1',
    packages=find_packages(where='src'),  # Finds all packages inside 'src'
    package_dir={'': 'src'},  # Tells setuptools that packages are in 'src'
    install_requires=[  # Add any external dependencies
        'pandas',
        'pymongo',
    ],
)
