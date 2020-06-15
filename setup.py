import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="strategize", # Replace with your own username
    version="0.0.1",
    author="Raghav Arora",
    author_email="agu94.raghav@gmail.com",
    description="Game Theory Simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raghavaro/strategize",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
