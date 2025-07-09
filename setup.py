from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements from requirements.txt
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="MLproject",
    version="0.0.1",
    author="Priyansh",
    author_email="priyanshpatel741@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
