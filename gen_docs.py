#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
[gen_docs.py]

Automatic docs generation for Ergonomica, in Ergonomica.
"""

import ergonomica
from ergonomica.lib.util.util import expand_path
from ergonomica.lib.lib import ns

def make_title(string):
    return string + "\n" + "-" * len(string) + "\n"

def main(argc):
    """gen_docs: Generate the Ergonomica defaults documentation.
    
    Usage:
       gen_docs TARGET
    """

    target = expand_path(argc.env, argc.args['TARGET'])
    out = ""

    # load into reST format
    for command in ns:
        out += make_title(command)
        out += ns[command].__doc__ + "\n"
    
    # dump to file
    open(target, "w").write(out)
