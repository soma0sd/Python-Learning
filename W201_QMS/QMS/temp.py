# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 23:54:26 2016
@author: soma0sd
"""
import random
import sys

size = 3

ref = 1234567890
using = 0
use0 = False


def DigitAdd(digit):
  global ref, size, using, use0
  i = 0
  while True:
    i = 0
    ex = random.randint(0, 9)
    val = int((ref % 10**ex)/10**(ex-1))
    used = False
    while i < digit+1 and using > 0:
      ck = int((using % 10**i)/10**(i-1))
      if ck == val:
        used = True
        break
      i += 1
    if val == 0 and not use0 and digit < size-1:
      use0 = True
      break
    elif val > 0 and not used:
      using += val*(10**digit)
      break
  return val*10**digit


def ckInput(cmd):
  global size, code
  if cmd.strip() == 'q':
    sys.exit()
  try:
    int(cmd)
  except:
    print('숫자나 q를 입력하세요.')
    return None
  if int(cmd) >= 10**(size) or int(cmd) <= 10**(size-1):
    print('{} 자리의 숫자를 입력해주세요'.format(size))
    return None
  if int(cmd) == code:
    print('you win\n\n')
    sys.exit()
  else:
    i, j = 1, 1
    stk = 0
    bol = 0
    while i < size+1:
      m = int((code % 10**i)/10**(i-1))
      j = 1
      while j < size+1:
        n = int((int(cmd) % 10**j)/10**(j-1))
        print(m, n)
        if n == m and i == j:
          stk += 1
        if n == m and i != j:
          bol += 1
        j += 1
      i += 1
    print('스트라이크: {}'.format(stk))
    print('        볼: {}'.format(bol))

i = 0
code = 0
while i < size:
  code += DigitAdd(i)
  i += 1
print(code)
while True:
  cmd = input('{}자리 수 입력, 나가려면 q: '.format(size))
  ckInput(cmd)