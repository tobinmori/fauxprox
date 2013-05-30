#!/usr/bin/python

from optparse import OptionParser
import logging
from time import sleep
import random
import sys

from formats import formats
from messages import messages


parser = OptionParser()
parser.add_option("-m","--mode", dest="mode")
parser.add_option("-f", "--format", dest="format",
                  help="logging format", metavar="FILE")
parser.add_option("-s", "--speed", dest="speed",
                  help="logging speed", metavar="FILE")
parser.add_option("-r", "--random_speed", dest="random_speed",
                  help="logging speed", metavar="FILE")
parser.add_option("-t", "--rotate", dest="rotate", default=True,
                  help="roTate between messages", action="store_true")
(options, args) = parser.parse_args()

format = options.format or 'default'
mode = options.mode or 'default'
speed = options.speed or 'default'
is_random_speed = options.random_speed or False
rotate_messages = options.rotate or False

speed_map = { 'default':.5,
              'fast':.01,
              'lurch':1,
              'glacial': 2,
            }

chug_speed = speed_map[speed]

logging.basicConfig(format=formats[format])
logger = logging.getLogger('tcpserver')

RANDOM_RANGES = {
    'dot_widths' : [3, 5, 7, 9, 13, 20,],
    'sleep_counts' : [.001, .01, .5, 1]
}

def get_random_num(choices=[]):
    random.shuffle(choices)
    return choices[0]

def nap(nap_type=None, is_random=is_random_speed):
    if is_random:
        sleep(get_random_num(choices=RANDOM_RANGES[nap_type]))
    else:
        sleep(chug_speed)
    return

def write_dots(is_random=True, dot_width=40):
    if is_random: dot_width = get_random_num(RANDOM_RANGES['dot_widths'])
    for x in xrange(0,dot_width):
        sys.stdout.write('. ')
        sys.stdout.flush()
        nap(nap_type='sleep_counts')
    sys.stdout.write("\n")

def run():
    while True:
        nap(nap_type='sleep_counts')
        if rotate_messages:
            logger.warning(messages[get_random_num(messages.keys())])
            write_dots()
        else:
            logger.warning(messages[mode])
            write_dots()


if __name__ == '__main__':
    run()
