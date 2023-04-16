import os

files_to_process = [
    r"C:\Users\Piotr Sroka\Documents\Python\Python II\s1.py",
    r"C:\Users\Piotr Sroka\Documents\Python\Python II\s2.py"
    ]


for r_file in files_to_process:
    print(os.path.basename(files_to_process[0]))
    
    with open(r_file, 'r') as f:
        source = f.read()
        exec(source)