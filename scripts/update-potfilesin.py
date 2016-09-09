import click


@click.command()
@click.argument('target', nargs=1)
def main(target):
    '''write a list of all python source files to POTFILES.in'''
    import os
    from distutils.filelist import FileList
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fl = FileList()
    fl.include_pattern('*.py', anchor=False, prefix='myfi')
    fl.findall(root)
    ff = fl.files[:]
    ff.insert(0, '[encoding: UTF-8]')
    ff.append('')

    with open(target, 'w') as fo:
        fo.write('\n'.join(ff))

if __name__ == '__main__':
    main()
