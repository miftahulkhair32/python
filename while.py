while True:
	line = raw_input('>>> ')
	if line == 'done':
		break
	elif line[0] == '#':
		continue
	print line
print 'done!'
