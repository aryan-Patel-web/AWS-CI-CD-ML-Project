from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of dependencies,
    excluding any editable install lines.
    """
    with open(file_path) as file:
        requirements = file.read().splitlines()
        # Remove '-e .' if present
        requirements = [req for req in requirements if req.strip() != '-e .']
    return requirements

setup(
    name='ML-Project',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author='Aryan Patel',
    author_email='aryanpatel77462@gmail.com',
)
