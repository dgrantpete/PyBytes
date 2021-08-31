from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name = "PyBytes",
    version = "1.0.0",
    
    packages = ["pybytes"],
    install_requires = [],
    
    author = 'Grant Peterson',
    author_email = "dgrantpete@gmail.com",
    description = "A library to assist in the creation and manipulation of bytes.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license = "MIT",
    keywords = "byte bytes bit bits binary bin",
    url = "https://github.com/dgrantpete/PyBytes",
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3"
    ]
)