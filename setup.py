import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="aioworker",
    version="1.0.0",
    author="Mateusz Zielinski",
    author_email="matzielinski15@gmail.com",
    description="Simple library for asynchronous HTTP workers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/h2pvrp/aioworker",
    packages=["aioworker"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=["aiohttp>=3.6.2"],
)
