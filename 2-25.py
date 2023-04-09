projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']


for p, l in zip(projects,leaders):
    print(f'The leader of {p} is {l}')
    
    
dates = ['2016-06-23', '2016-08-29', '1994-01-01']
for p,d,l in zip(projects,dates,leaders):
    print(f'The leader of {p} started {d}  is {l}')
    
    

for i, (p,d,l) in enumerate(zip(projects,dates,leaders)):
    print(f'{i+1} - The leader of {p} started {d}  is {l}')