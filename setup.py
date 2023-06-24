from setuptools import setup, find_packages
from typing import List

DASH_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:

    '''
    Returns a list of requirements from requirements.txt file
    '''
    requirements = []

    with open(file_path) as file:
        requirements = [line.strip() for line in file if line.strip() != DASH_E_DOT]
    
    return requirements


setup(
    name='ml_setup_tutorial',
    author='Etietop Abraham',
    author_email='etietopdemasabraham@gmail.com',
    version='0.0.1',
    description='learn how to setup ml project end to end',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)