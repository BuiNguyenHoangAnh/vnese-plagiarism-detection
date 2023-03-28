TEST = "hello"
SOURCE = "hello world"

i = 0
M = 0
TEST = TEST.split()
SOURCE = SOURCE.split()

while i < len(TEST):
    j = 0
    while j < len(SOURCE):
        if TEST[i] == SOURCE[i]:
            jj = j
            max =0
            while jj < len(SOURCE):
                if TEST[i] == SOURCE[jj]:
                    x = 0
                    while i + x < len(TEST):
                        if jj + x < len(SOURCE):
                            if TEST[i+x] == SOURCE[jj+x]:
                                x += 1
                            else:
                                break
                        else:
                            break
                else:
                    jj += 1
                    continue
                if x > j: # g
                    if max < x:
                        max = x
                    else: jj += x
                else: jj +=x
            if max == 0:
                break
            else:
                M += max
                i += max -1
        else: 
            j+=1
        continue
    i += 1
    
print(M*100/len(TEST))