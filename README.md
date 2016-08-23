This program allows you to easily create strong, memorable passphrases.

It reads a specified number of bits of data from your system's CSPRNG, turrns it
into a very large number, and prints it out in base 7776.

The result will be something like `greet say yaw dunham italy pass navel`. If
your system has a good random number generator, this should be a reasonably secure
password, and also reasonably easy to memorize.

see also:
* http://world.std.com/~reinhold/diceware.html
* https://www.rempe.us/diceware/#diceware
* https://xkcd.com/936/
* https://github.com/bbiw/mempass


## install

    $ pip3 install correct-horse


## usage

    $ chbs --help
    Usage: chbs [OPTIONS]

      print strong random passphrases (e.g.'correct horse battery staple')

    Options:
      -w, --wordlist TEXT      list of words to choose from (default=diceware)
      -c, --count INTEGER      number of passphrases (default=8)
      -b, --bits INTEGER       minimum bits of entropy per passphrase (default=90)
      -j, --join TEXT          join words with this character (default=space)
      -v, --verbose / --quiet  print extra stuff to stderr (default=quiet)
      --help                   Show this message and exit.


     $ chbs -b64 -c1 -j-
     yon-30-zg-200-debut
