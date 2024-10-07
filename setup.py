import setuptools
from pathlib import Path


def load_readme():
    """Load and return the content of the README file."""
    readme_path = Path("README.md")
    if readme_path.exists():
        return readme_path.read_text(encoding="utf-8")
    return "Long description could not be read from README.rst"


setuptools.setup(
    name="lichesspy",
    version="6.0.5",
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
    install_requires=["requests==2.32.3", "six==1.16.0", "chess==1.11.0"],
)
