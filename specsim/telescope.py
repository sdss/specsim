# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2018-06-20 14:45:48
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2018-07-05 10:36:39

from __future__ import print_function, division, absolute_import


class Telescope(object):
    ''' A Telescope configuration '''

    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return '<Telescope(name={0})>'.format(self.name)



def initialize(config, params=None):
    ''' Initialize a telescope from a set configuration parameters '''

    survey = config.instrument.name
    size = params.get('telescope', '') if params else ''
    name = '{0} {1}'.format(survey, size)

    # copy the from telescope constants over from the Instrument object
    area_params = config.get_constants(config.instrument)

    telescope = Telescope(name, **area_params)
    return telescope


