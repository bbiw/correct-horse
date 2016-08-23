from setuptools import setup, find_packages

def slurp(fname):
    with open(fname,"rt") as fi:
        return fi.read()

setup(
    name='correct-horse',
    version='0.1.3',
    description='Print strong, memorable passphrases',
    url='https://github.com/bbiw/correct-horse',
    author='Terrel Shumway',
    long_description=slurp("description.rst"),
    classifiers=[
        'Environment :: Console',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Security',
    ],
    author_email='algae-ester-1925-riga-seth@shumway.us',
    license='MIT',
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
