from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='ldaptriggers',
    version='0.2.0',
    description='',
    long_description=readme,
    author='Marc Benedi',
    author_email='marcbenedi.sanmillan@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'examples')),
    install_requires=requirements,
    entry_points={
        'console_scripts': ['ldaptriggers=ldaptriggers.cli:cli']
    },
    include_package_data=True
)
