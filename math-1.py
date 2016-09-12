#!/usr/bin/python

m = input('Please input the first number: ')
n = input('Please input the second number: ')

mn = m
nn = n

if n < m:
  i = n
  n = m
  m = i

while True:
  i = n % m
  if i == 0:
    print '%i is GCD.'%m
    break
  n = m
  m = i

print '%i is LCM.'%(nm * nn / m)