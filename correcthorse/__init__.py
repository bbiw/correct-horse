import os
import math
import pkg_resources
import click


def slurp(fname):
    """read the contents of a file into a list of lines"""
    with open(fname, "rt") as fi:
        return fi.read().splitlines()


def bignumber(cbytes):
    """return a big random number of cbytes*8 bits"""
    return int.from_bytes(os.urandom(cbytes), 'big')


def genpass(big, *wordlists):
    """generate a sequence of words selected from wordlists

    `big` ought to be a large random number
    """
    while True:
        for wl in wordlists:
            big, small = divmod(big, len(wl))
            yield wl[small]
            if big <= 0:
                return


def getwords(wordlists):
    """return a list of all unique words in all specified files"""
    words = []
    for wl in wordlists:
        if os.path.exists(wl):
            words.extend(slurp(wl))
            continue
        rp = 'wordlists/' + wl
        if pkg_resources.resource_exists(__name__, rp):
            words.extend(pkg_resources.resource_string(
                __name__, rp).decode("utf-8").splitlines())
            continue
        click.echo('cannot find word list "{}"'.format(wl))
    return list(set(words))


def random_passphrase(words, bits=90, join=' '):
    """return a tuple ( passphrase, bits )

    `passphrase` is a seqence of `words` joined by `join`
    `bits` is an estimate of the number of bits of entropy in the passphrase.
        It should be >= the bits specified as a parameter.
     """
    wc = len(words)
    bitsperword = math.log(wc, 2)
    cbytes = math.ceil(bits / 8)
    ww = []
    big = bignumber(cbytes)
    bitsleft = bits
    while bitsleft > 0 and big > 0:
        big, small = divmod(big, wc)
        ww.append(words[small])
        bitsleft -= bitsperword
    return join.join(ww), bitsperword * len(ww)


@click.command()
@click.option('--wordlist', '-w', default=['default'], multiple=True, help='list of words to choose from (default=diceware)')
@click.option('--count', '-c', type=int, default=8, help='number of passphrases (default=8)')
@click.option('--bits', '-b', type=int, default=90, help='minimum bits of entropy per passphrase (default=90)')
@click.option('--join', '-j', default=' ', help='join words with this character (default=space)')
@click.option('--verbose/--quiet', '-v', default=False, help='print extra stuff to stderr (default=quiet)')
def cli(wordlist, count, bits, join, verbose):
    """print strong random passphrases (e.g.'correct horse battery staple')"""
    if verbose:
        sys.stderr.write('wordlists: {} count: {} bits: {}\n'.format(
            wordlist, count, bits))
    words = getwords(wordlist)
    for i in range(count):
        w, b = random_passphrase(words, bits, join)
        if verbose:
            sys.stderr.write('{} bits\n'.format(b))
        print(w)
