raw = r'this\t\n and that'

# this\t\n and that
print (raw)

multi = """It was the best of times.
It was the worst of times."""
s = multi.replace('w','G')
# It was the best of times.
# It was the worst of times.
print (multi)
print(s)
text = ("%d little pigs come out, "
"or I;ll %s, and I'll %s, "
"and I'll blow your %s down!"
% (3, 'huff', 'puff', 'house'))
print(text)
