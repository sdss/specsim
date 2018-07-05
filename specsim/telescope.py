# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2018-06-20 14:45:48
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2018-06-20 16:50:33

from __future__ import print_function, division, absolute_import


class Telescope(object):
    ''' A Telescope configuration '''

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Telescope(name={0})>'.format(self.name)



def initialize(config, params=None):
    ''' Initialize a telescope from a set configuration parameters '''

    survey = config.instrument.name
    size = params.get('telescope', '') if params else ''
    name = '{0} {1}'.format(survey, size)

    area_params = config.get_constants(config.instrument)

    telescope = Telescope(name)
    return telescope


