from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements'''

    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]
        return requirements
    
setup (
        name ='winequality',
        version= '1.0',
        packages=find_packages(),
        author='sravanthipaturi',
        author_email = 'paturisravanthi212gmail.com',
        install_requires = get_requirements('requirements.txt')
    )