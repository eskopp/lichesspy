import setuptools
from pathlib import Path


def load_requirements():
    """Load and return list of requirements from a file."""
    requirements_path = Path("requirements.txt")
    try:
        return requirements_path.read_text(encoding="utf-8").splitlines()
    except Exception as error:
        # Depending on how critical this file is, you may want to raise an error
        # raise RuntimeError(f"Unable to read the requirements file: {error}")
        print(f"Exception when reading requirements: {error}")
        return []


def load_readme():
    """Load and return the content of the README file."""
    readme_path = Path("README.rst")
    if readme_path.exists():
        return readme_path.read_text(encoding="utf-8")
    return "Long description could not be read from README.rst"


setuptools.setup(
    name="lichesspy",
    version="6.0.4.dev2",
    author="eskopp",
    author_email="skopp.erik+lichesspy@gmail.com",
    description="Python wrapper for lichess",
    long_description=load_readme(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/eskopp/lichesspy",
    packages=["lichesspy"],
    package_data={"lichesspy": ["VERSION"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=load_requirements(),
)
