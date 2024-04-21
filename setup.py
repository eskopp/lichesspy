import setuptools

setuptools.setup(
    name="lichesspy",
    version="6.0.3",
    author="eskopp",
    author_email="skopp.erik@gmail.com",
    description="Python wrapper for lichess",
    long_description=open('README.rst').read(),
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
    install_requires=[
        "requests>=2.31.0",
        "six>=1.16.0",
        "python-chess>=1.999",
        "chess>=1.10.0"
    ]
)
