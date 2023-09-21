import os

i = 1
d = 1
TN = "Text" 
FN = "File" 



for x in range(5):
    if not os.path.exists(f'{FN}{i}'):
        os.mkdir(f'{FN}{i}')
        f=open((f'{FN}{i}/{TN}{d}.txt'), "w+")
        f.write((f'Text{d}'))
        print(f"Done")
        i = i+1
        d = d+1
        print(i)
        print(d)
        
    else:
        print(f"Error")

