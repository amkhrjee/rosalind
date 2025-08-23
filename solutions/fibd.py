# Thanks to: http://saradoesbioinformatics.blogspot.com/2016/06/mortal-fibonacci-rabbits.html

n = 85
m = 20  # rabbits die after m months

fseq = [1, 1]

k = 2
while k < n:
    if k < m:
        # rabbits haven't died off yet
        fseq.append(fseq[-1] + fseq[-2])
    elif k == m:
        # the original pair dies (1 pair dies)
        fseq.append(fseq[-1] + fseq[-2] - 1)
    else:
        # everyone born more than m months ago dies
        fseq.append(fseq[-1] + fseq[-2] - fseq[-(m + 1)])
    k += 1


print(fseq[-1])
