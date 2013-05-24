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
(options, args) = parser.parse_args()

format = options.format or 'default'
mode = options.mode or 'default'
speed = options.speed or 'default'

speed_map = { 'default':.5,
              'fast':.01,
              'lurch':1,
              'glacial': 2
            }

chug_speed = speed_map[speed]

logging.basicConfig(format=formats[format])
logger = logging.getLogger('tcpserver')

def get_random_num():
    choices = [3, 5, 7, 9, 13, 20, 50, 100]
    random.shuffle(choices)
    return choices[0]

def write_dots(is_random=True, dot_width=40):
    if is_random: dot_width = get_random_num()
    for x in xrange(0,dot_width):
        sys.stdout.write('. ')
        sys.stdout.flush()
        sleep(chug_speed)
    sys.stdout.write("\n")

def run():
    while True:
        sleep(chug_speed)
        logger.warning(messages[mode])
        write_dots()




if __name__ == '__main__':
    run()