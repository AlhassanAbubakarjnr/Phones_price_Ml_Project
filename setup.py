from setuptools import find_packages, setup
from typing import List

HYPEN_E_DASH = "-e ."
def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","").strip() for req in requirements]
        if HYPEN_E_DASH in requirements:
            requirements.remove(HYPEN_E_DASH)
    return requirements

setup(
    name="phones_price_prediction",
    author="Alhassan Abubakar",
    author_email="alhassanabubakarjnr@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)