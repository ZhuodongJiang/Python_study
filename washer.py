print('请输入加水量')
level = input()
# 洗衣程序
if level == 'low':
    print('注水20L')
    print('搅拌30M')
elif level == 'high':
    print('注水30L')
    print('搅拌50M')
print('放水')
#甩干程序
print('请输入甩干次数')
times=int(input())
for i in range(times):
    print('注水30l')
    print('搅拌 20m')
    print('放水')
    print('甩干')
