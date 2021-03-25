import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytradier",
    version="0.0.1",
    author="Robert Leonard",
    description="Unofficial library for interacting with Tradier brokerage",
    license='GPL-3.0',
    author_email="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rleonard21/pytradier.git",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests>=2.23.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)