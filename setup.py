from setuptools import find_packages, setup

VERSION = "0.0.1"
DESCRIPTION = "A simple example private package"
LONG_DESCRIPTION = "A simple example private package"

setup(
    name="package_publishing",
    version=VERSION,
    packages=find_packages(),
    install_requires=[], # add any additional packages that
        # needs to be installed along with your package. Eg: 'caer'
    author="Karoki",
    author_email="karoki@kar.co",
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Phystro/package_publishing",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
