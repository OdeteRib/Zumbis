n,k = map(int, raw_input().split())
processed = sorted(range(1<<n), cmp=lambda a,b:
	cmp(bin(a).count("1"), bin(b).count("1")) 
	if cmp(bin(a).count("1"):
		bin(b).count("1")) 
	else:
		cmp(a,b))
print bin(processed[k - 1])[2:].zfill(n)
