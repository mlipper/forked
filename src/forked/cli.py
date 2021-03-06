"""
Module that contains the command line app.

This file is based on code generated using https://github.com/ionelmc/cookiecutter-pylibrary.
The remainder of this docstring section was generated:

Why does this file exist, and why not put this in __main__?
  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:
  - When you run `python -mnameless` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``nameless.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``nameless.__main__`` in ``sys.modules``.
  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import argparse


"""Create an ArgumentParser."""
parser = argparse.ArgumentParser(description="Invoke bray to geocode New York City location data with geoclient.")
# parser.add_argument('names', metavar='NAME', nargs=argparse.ZERO_OR_MORE, help="A name of something.")
parser.add_argument("--configfile", "-c", action="store_true", default=None, help="Path to bray configuration file.")
parser.add_argument("--limit", "-l", type=int, default=None, help="If set, limits the number of processed lines.")
parser.add_argument("--print", "-p", action="store_true", default=False, help="If set, pretty prints before writing to output file.")


def main(args=None):
    """Construct runtime configuration by overriding defaults with any command line arguments.
    """
    print(f"Given args: {args}")
    args = parser.parse_args(args=args)
    print(f"Parsed args: {args}")
