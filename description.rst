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
