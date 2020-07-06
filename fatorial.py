def fatorial(x):
  if x > 1:
    return x * fatorial(x - 1)
  else:
    return 1
