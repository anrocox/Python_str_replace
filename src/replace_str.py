#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 9, 2014

@author: anroco

How to replace a string by another in a python str?

¿Como reemplazar un string por otro en un str python?
'''

#create a str
s = 'the team has won two trophies'
print(s)

#generates a copy of 's' replacing the old string by the new string
s_new = s.replace('two', 'three')
print(s_new)

#create a str
s = 'I saw a saw that could out saw any other saw I ever saw.'
print(s)

#can define the number of occurrences to replace.
s_new = s.replace('saw', '--', 3)
print(s_new)
