from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .' #this conncets requirements.txt to setup.py automatically

def get_requirements(file_path:str)->List[str]:
    '''
    This function will retrun a list of requirements 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Ayush',
    author_email='anandayush2001@gmail.com',
    packages=find_packages(),  #will look for all folders with __init__.py and consider them as package and install them like usual Python packages
    install_requirements=get_requirements('requirements.txt')
)