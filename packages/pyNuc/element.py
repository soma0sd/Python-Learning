# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 18:19:25 2016

@author: soma0sd
"""
import pyNuc as _nuc


class decay:
    def __init__(self, decay_const, **kw):
        self._opt = {'count': 1}
        for key in kw.keys():
            if key not in self._opt.keys():
                raise _nuc.pyNucError(str(key)+' is not decay option')
        self._opt.update(kw)
