f = open('tester.txt', 'rt')
bin_in = f.readline()
print((bin_in))
bin_num = bin_in.split()
out_bin = ''
for i in range(len(bin_num)):
    temp = int(bin_num[i],2)
    #print(temp,chr(temp),i)
    out_bin += chr(temp)
print(out_bin)