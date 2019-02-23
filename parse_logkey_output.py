import matplotlib.pyplot as plt
import re
file_rel_path = "../test-code.log"
file = open(file_rel_path, "r")
file.readline()
file.readline() # get rid of first two lines
i=0
action_chars=[]
standard_chars=[]
frequencies={}
for line in file:
    new_line = re.sub(r'^[^>]*>','',line)
    action_chars = re.findall(r'<.*?>',new_line)
    standard_chars = re.sub(r'<.*?>','',new_line)
    # print(standard_chars)
    for char in action_chars:
        if char[1] == '#':
            while char in action_chars:
                action_chars.remove(char)
    # print(action_chars)
    for char in standard_chars:
        if char in frequencies:
            frequencies[char]+=1
        else:
            frequencies[char]=1
    for char in action_chars:
        if char in frequencies:
            frequencies[char]+=1
        else:
            frequencies[char]=1
for freq in frequencies:
    print(freq,":",frequencies[freq])
file.close()
file=open("freqs.txt", "w+")
for freq in frequencies:
    file.write(str(freq)+"||"+str(frequencies[freq])+"\n")
