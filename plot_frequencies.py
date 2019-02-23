import matplotlib.pyplot as plt
import numpy as np
chars=[]
freqs=[]
combined=[]
file_rel_path="freqs.txt"
file=open(file_rel_path, "r")
for line in file:
    set=line.split("||")
    combined.append([str(set[0]),int(set[1])])
sort_combined=sorted(combined, key = lambda x: int(x[1]), reverse=True)
sort_combined_trunc=sort_combined[:52]
total=0
for set in sort_combined_trunc:
    chars.append(set[0])
    freqs.append(set[1])
for set in sort_combined:
    if len(set[0])>1:
        if set[0][1] is not '#':
            total+=set[1]
for set in sort_combined:
    if len(set[0])>1:
        if set[0][1] is not '#':
            print('{0:15s}: {1:3.8f}%'.format(set[0],100*set[1]/total))
    else:
        print('{0:15s}: {1:3.8f}%'.format(set[0],100*set[1]/total))
y_pos = np.arange(len(chars))
plt.bar(y_pos,freqs,align='center',alpha=0.5)
plt.xticks(y_pos, chars)
plt.xticks(rotation=45)
plt.ylabel('Frequency')
plt.title('Key Frequency')
plt.show()
