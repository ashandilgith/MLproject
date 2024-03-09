from setuptools import find_packages, setup
from typing import list 

HYPHEN_E_DOY ='-e .'

def get_requirements (file_path:str)->List[str]:

#this function will return the list of of requirements#

requirements=[]
with open('requirements.txt') as file_obj:
    requirements=file_.readlines()
    requirements[req.replace ("\n", "") for req in requirements]
    
    if HYPHEN_E_DOT in requirements:
        requirements.remove HYPHEN_E_DOT    
        
return requirements




setup(
    
name = 'mlproject',
version='0.0.1',
author = 'Ashan Dilgith',
author_email='ashandilgith@gmail.com'   
packages=find_packages(),

install_requires = get_requirements('requirements.txt')


)
