ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

fromTo = [(x,y) for x in ports for y in ports]
print(len(fromTo))

fromTo2 = [(x,y) for x in ports for y in ports if x != y ]
print(len(fromTo2))

fromTo3 = [(x,y) for x in ports for y in ports if x < y ]
print(len(fromTo3))