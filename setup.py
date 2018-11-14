from setuptools import setup
from coin2 import __version__, __doc__
setup(name='coin2', packages=['coin2'],
      url='https://github.com/val-labs/coin2',
      description="coin2",
      long_description=__doc__,
      long_description_content_type='text/markdown',
      install_requires=['docopt'],
      entry_points={
          'console_scripts': [
              'coin2-chain-create  = coin2.__main__:args.chain.create',
              'coin2-chain-remove  = coin2.__main__:args.chain.remove',
              'coin2-chain-start   = coin2.__main__:args.chain.start',
              'coin2-chain-stop    = coin2.__main__:args.chain.stop',
              'coin2-wallet-create = coin2.__main__:args.wallet.create',
              'coin2-wallet-remove = coin2.__main__:args.wallet.remove',
              'coin2-cat-create    = coin2.__main__:args.cat.create',
              'coin2-cat-remove    = coin2.__main__:args.cat.remove',
              'coin2-cat-meow      = coin2.__main__:args.cat.meow',
              'coin2-cat-purr      = coin2.__main__:args.cat.purr',
              'coin2-cat-hiss      = coin2.__main__:args.cat.hiss',
              'coin2               = coin2.__main__:main']},
      version=__version__)
