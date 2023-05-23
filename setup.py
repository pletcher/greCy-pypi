from __future__ import unicode_literals
import setuptools

setuptools.setup(
    name="grecy_josesmooth",
    version="3.5.13",
    author="Jacobo Myerston",
    author_email="jmyerston@ucsd.edu",
    description="This project trains four spaCy models using the ancient Greek Universal Dependency treebanks Proiel and Perseus",
    packages=setuptools.find_packages(),
    python_requires='>=3.9',
    install_requires = ["click>=7.1.1,<9.0.0", "typer>=0.3.0,<0.8.0"]
)

