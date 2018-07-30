
from setuptools import setup, find_packages

from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip


pfile = Project(chdir=False).parsed_pipfile
install_requires = convert_deps_to_pip(pfile['packages'], r=False)
tests_require = convert_deps_to_pip(pfile['dev-packages'], r=False)

setup(
    name="pysss",
    description="Make easy to use AWS parameter store and secret manager",
    url="https://github.com/chocolate-factory/simple-secret-store",
    packages=find_packages(exclude=('tests', )),
    install_requires=install_requires,
    tests_require=tests_require
)

