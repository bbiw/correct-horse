from setuptools import setup, find_packages

setup(
    name='correct-horse',
    version='0.1.0',
    description='Print strong, memorable passphrases',
    url='https://github.com/bbiw/correct-horse',
    author='Terrel Shumway',
    long_description='''This program allows you to easily create strong, memorable passphrases.

    It reads a specified number of bits of data from your system's CSPRNG, turrns it
    into a very large number, and prints it out in base 7776.

    The result will be something like `greet say yaw dunham italy pass navel`. If
    your system has a good random number generator, this should be a reasonably secure
    password, and also reasonably easy to memorize.

    see also:
        http://world.std.com/~reinhold/diceware.html
        https://www.rempe.us/diceware/#diceware
        https://xkcd.com/936/
        https://github.com/bbiw/mempass

    ''',
    classifiers=[
        'Environment :: Console',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Security :: Passwords',
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
