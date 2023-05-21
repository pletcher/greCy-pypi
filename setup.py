from __future__ import unicode_literals
import setuptools

setuptools.setup(
    name="grecy_josesmooth",
    version="3.5.2",
    author="Jacobo Myerston",
    author_email="jmyerston@ucsd.edu",
    description="This project trains four spaCy models using the ancient Greek Universal Dependency treebanks Proiel and Perseus",
    packages=setuptools.find_packages(),
    package_data={'grecy_josesmooth': ['./LICENSE.txt', './project.yml', './README.md', 'configs/*', 'corpus/*/*', 'data/*/*']},
    include_package_data=True,
    python_requires='>=3.9',
)

