#!/usr/bin/python

m = input('Please input the first number: ')
n = input('Please input the second number: ')

mn = m
nn = n

while True:
  i = n % m
  if i == 0:
    break
  n = m
  m = i
  
print '%i is GCD.'%m
print '%i is LCM.'%(mn * nn / m)
