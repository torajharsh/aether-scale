from setuptools import setup, find_packages
import os

# Read the README for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aether-scale",
    version="1.0.0",
    author="Raj Harsh",
    author_email="",
    description="Universal Matrix Engine for Unit-Domain Flow (UDF).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/torajharsh/aether-scale",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    install_requires=[
        "torch>=2.0.0",
        "numpy>=1.24.0",
    ],
    python_requires=">=3.8",
)
