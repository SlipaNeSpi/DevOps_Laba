from setuptools import setup, find_packages

setup(
    name="temperature-converter",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[
        "Flask",
    ],
)