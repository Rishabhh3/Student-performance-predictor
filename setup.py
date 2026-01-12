# with setup.py I will be able to build my entire ML application as a package and even deploy in pypi

from setuptools import find_packages,setup # automatically finds all the ML packages used 
from typing import List # used for this requirement function

HYPEN_E_DOT='-e .'
# the -e .  file in requirements.txt is an indication that setup.py is there and it 
# automatically (mapped to setup.py) and automatically this entire package will be built

def get_requirements(file_path:str)->List[str]:
    ''' This function will return the list of requirements'''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements] # because in requirements it records \n for next line so to remove it 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='student_performance',
    version='0.0.1', # so I can update it to new versions 
    author='Rishabh',
    author_email='rishabhchamoli0120@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

# we have init in src, when find_packages is running it will see in 
# how many folder init is running and it will directly consider
# this src as package itself and then it will try to build it
# my entire project development will be happening inside this folder
