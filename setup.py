import setuptools


def def_requirements():
    """Check PIP Requirements"""
    pip_lines = ""
    try: 
        with open("requirements.txt", encoding="utf-8") as file_content:
            pip_lines = file_content.read().splitlines()
    except Exception as error: 
        print(f"Execpiton: {error}")
    return pip_lines


def def_readme():
    """Check Readme RST"""
    readme = ""
    with open("README.rst", encoding="utf-8") as file_content:
        readme = file_content.read()
    return readme


setuptools.setup(
    name="lichesspy",
    version="6.0.0",
    author="eskopp",
    author_email="skopp.erik@gmail.com",
    description="Python wrapper for lichess",
    long_description=def_readme(),
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
    install_requires=def_requirements(),
)
