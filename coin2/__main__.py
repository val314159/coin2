"""Coin2

 The Coin Two

Usage:
  coin2 chain create <name> [--port=<port>]
  coin2 chain remove <name>
  coin2 chain start  <name>
  coin2 chain stop   <name>
  coin2 wallet create <name> <wname> <aliases>...
  coin2 wallet remove <name> <wname>
  coin2 cat create <name>
  coin2 cat remove <name>
  coin2 ship new <name>...
  coin2 ship new <name>...
  coin2 ship <name> move <x> <y> [--speed=<kn>]
  coin2 ship shoot <x> <y>
  coin2 mine (set|remove) <x> <y> [--moored | --drifting]
  coin2 (-h | --help)
  coin2 --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --port=<port> Listening port [default: 8099].
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.

"""
import sys, docopt
from . import __version__

_main = staticmethod(lambda:main(sys.argv[0].split('-')[1:]+sys.argv[1:]))

class args:
    class chain:
        create = _main
        remove = _main
        start  = _main
        stop   = _main

    class wallet:
        create = _main
        remove = _main

    class cat:
        create = _main
        remove = _main
        meow   = _main
        purr   = _main
        hiss   = _main

def main(argv=None):
    print("ARGV", argv)
    args = docopt.docopt(__doc__, argv=argv, version='coin2 '+__version__)
    print(args)

if __name__ == '__main__':
    main()
