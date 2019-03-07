#! /usr/bin/python
import os, sys
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert( 1, os.path.join( pwd, 'ext' ) )

import logging, coloredlogs


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

logger.info('Before installing colored logger')

coloredlogs.install( logger=logger, fmt='%(message)s')

#logger.removeHandler(logger.handlers[0])
logger.warn('After installing colored logger')
