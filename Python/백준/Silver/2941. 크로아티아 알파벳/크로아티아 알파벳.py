input = input()
c_alpah = ['dz=','lj','nj','c=','c-','d-','s=','z=']

for i in c_alpah:
    input = input.replace(i, '*')

print(len(input))