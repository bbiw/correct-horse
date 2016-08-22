from setuptools import setup, find_packages

setup(
    name='correct-horse',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        chbs=correcthorse:cli
    ''',
)
