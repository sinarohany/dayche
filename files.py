# fid = open('test.txt')
# for line in fid:
#     print(line)
#
# fid.close()

with open('test.txt') as fid:
    # for line in fid:
    #     print(line)
    lines = fid.readlines()
    print(lines)
myContext = ['Sina Rohany\n', '1 february 1981'+'\n', 'CEO of TikBook']
with open('dayche.txt', 'w') as fid:
    fid.writelines(myContext)

