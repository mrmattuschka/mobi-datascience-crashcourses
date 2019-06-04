from setuptools import setup, find_packages

# To install .src/'s contents as a package: pip install -e .

setup(
    name="example_package",
    package_dir = {'':'src'},
    packages = find_packages('src')
)