#!/usr/bin/env python2

import array
from lib import common


def main():
  common.init_args('./nrf24-flash-dumper.py')
  common.parser.add_argument('flash_dump',
    help='file to save a flash dump to.')
  common.parse_and_init()

  data = array.array('B', [])

  # Read all of flash memory.
  step = 32
  for address in range(0, 0x8000, step):
    data.extend(common.radio.read_memory(address, step))

  with open(common.args.flash_dump, 'wb') as f:
    data.tofile(f)


if __name__ == '__main__':
  main()
