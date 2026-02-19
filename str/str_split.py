command = '/add date Text command'
com_split = command.split()
print(' '.join(com_split))
print(command.replace('/add', '').strip(' '))

command2 = '/add date Text command'
com_spl = command2.split(maxsplit=2)
print(com_spl)

date = com_spl[1]
text = com_spl[2]
print(date, text)