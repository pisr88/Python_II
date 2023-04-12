ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

fromTo = ((x,y) for x in ports for y in ports)

fromTo2 = ((x,y) for x in ports for y in ports if x != y )

fromTo3 = ((x,y) for x in ports for y in ports if x < y )

def wer(g):
    i=0
    while True:
        try:
            print(next(g))
            i+=1
        except:
            print(i)
            break
        
wer(fromTo)
wer(fromTo2)
wer(fromTo3)
