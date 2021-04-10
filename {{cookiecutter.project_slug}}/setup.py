from setuptools import find_packages, setup


setup(
    name="{{cookiecutter.project_slug}}",
    verion="{{cookiecutter.version}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author}}",
    description="{{cookiecutter.description}}",
    packages=find_packages(exclude=["tests.*", "tests", "*.tests"]),
    python_requires=">=3.7",
)