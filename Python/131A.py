s=input().strip()
if len(s)==1 or s.isupper() or s[1:].isupper():
	print(s.swapcase())
else:
	print(s)
