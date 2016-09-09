from setuptools import setup, find_packages


def slurp(fname):
    with open(fname, 'rt') as fi:
        return fi.read()

setup(
    name='correct-horse',
    version=slurp('VERSION').strip(),
    description='Print strong, memorable passphrases',
    url='https://github.com/bbiw/correct-horse',
    author='Terrel Shumway',
    long_description=slurp('description.rst'),
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
    setup_requires=[
        'setuptools_git >= 0.3',
    ],
    install_requires=[
        'Click',
        'flufl.i18n',
    ],
    entry_points='''
        [console_scripts]
        chbs=correcthorse:cli
    ''',
)
