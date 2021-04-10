import json
import os
from datetime import datetime

from setuptools import find_packages, setup


def _get_version_suffix():
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    commit = os.environ.get("GIT_COMMIT", "unknown")[:6]
    _write_meta({"commit": commit})
    return (
        ""
        if os.environ.get("RELEASE", "").lower() == "true"
        else f"-dev{timestamp}+{commit}"
    )


def _write_meta(data):
    directory = os.path.dirname(__file__)
    meta_path = os.path.join(directory, __name__, "meta.json")
    with open(meta_path, "w") as f:
        json.dump(data, f)


__name__ = "{{cookiecutter.project_slug}}"
__version__ = f"0.1.0{_get_version_suffix()}"

setup(
    name="{{cookiecutter.project_slug}}",
    verion="{{cookiecutter.version}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author}}",
    description="{{cookiecutter.description}}",
    packages=find_packages(exclude=["tests.*", "tests", "*.tests"]),
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_slug}}={{cookiecutter.project_slug}}.__main__:main"
        ]
    },
)
