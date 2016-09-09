This program allows you to easily create strong, memorable passphrases.

It reads a specified number of bits of data from your system's CSPRNG, turrns it
into a very large number, and prints it out in base 7776.

The result will be something like `greet say yaw dunham italy pass navel`. If
your system has a good random number generator, this should be a reasonably secure
password, and also reasonably easy to memorize.

see also:
  * http://world.std.com/~reinhold/diceware.html
  * https://www.rempe.us/diceware/
  * https://xkcd.com/936/
  * https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases
  * https://github.com/bbiw/mempass

## install

    $ pip3 install correct-horse


## Command line usage

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


## API

The simple, high-level, API to generate passwords:

    >>> import correcthorse
    >>> wl = correcthorse.getwords(('effs1',))
    >>> correcthorse.random_passphrase(wl)
    ('mouth ahead ice open item duty frame navy early', 93.05865002596161)
    >>> correcthorse.random_passphrase(wl,64)
    ('rope chess race half dawn owl repay', 72.37895002019238)
    >>> correcthorse.random_passphrase(wl,128,'-')
    ('habit-vapor-darn-scarf-wilt-boney-lemon-ajar-flap-whoop-fresh-polar-trial', 134.4180500375001)

Note that the entropy estimate is only an estimate. The actual entropy will be
closer to, but always at least `bits`.

If you want to dig deeper:

    >>> bn = correcthorse.bignumber(24)
    >>> bn.bit_length()
    192
    >>> sep = correcthorse.getwords(('special',))
    >>> ''.join(correcthorse.genpass(bn,wl,sep))
    'gulf"eats9oat!spoke9thong%disco.puma}dot+fancy(swept)evil^amino_salsa'

But that is probably overkill, and makes it a lot harder to memorize and type.
