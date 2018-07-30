import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrecswitch",
    version="0.0.1",
    author="Marco Lertora",
    author_email="marco.lertora@gmail.com",
    description="A pure-python communication protocol for Lumitek/Ankuoo RecSwitch devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcolertora/pyrecswitch",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ),
)