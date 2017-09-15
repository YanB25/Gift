# -*- coding=utf8 -*-
from time import *
from random import *
import config

data = config.UnionData()
localTime = localtime(time())
if (localTime.tm_year <= config.k_birth_year and localTime.tm_mon <= config.k_birth_month and localTime.tm_mday < config.k_birth_date):
    print("哈喽\ncom的生日还没到噢～\n生日那天再来找我玩儿吧\n")
    print('输入<任意键>结束')
    input("")
    exit()

print("请输入<help>:\n")
help_txt = '''哈喽~ com~ 欢迎来找我玩儿啊
这是个什么游戏呢…… emmmmmmmm
每隔一段时间，你可以获得一次抽抽抽的机会 
[输入 <roll> 或 <r> 抽奖]
然后你就可以抽到我夸你的话啦哈哈哈哈
大概是100句诗句吧~ 够你抽好久的啦
每次抽到一个新的句子，就可以完成一次解锁
[输入 <record> 查看解锁记录]
record里你可以查到很多信息 
还有啊记得退出一定要
[输入 <quit> 或 <q> 退出]
否则有可能没办法把你的记录存档噢
最后，如果还有啥不懂的，你可以
[输入 <help> 或 <h> 查看帮助]
嗯哒就是这样 
(我不会告诉你 我留了个小彩蛋
嘿嘿慢慢找吧)
'''
while True:
    input_txt = input(">>> ")
    config.debug_print(data.nextTime())
    if input_txt == 'q' or input_txt == 'quit':
        data.close()
        exit()
    elif input_txt == 'help' or input_txt == 'h':
        print(help_txt)
    elif input_txt == 'record':
        for i in range(1, 101) :
            s = data.getString(i)
            print(data.getString(i))
            if (s != ""):
                print()
        print('解锁情况({}/{})'.format(data.getUnlockNum(), data.getTotalNum()))
        print('剩余抽奖机会: {} 已抽次数: {}'.format(data.chance - data.usedChance, data.usedChance))
        print('下一次抽奖还需等待 ' + data.nextTime())
    elif input_txt == 'I love YB':
        data.cheat()
        print('#彩蛋# 全成就已解锁')
    elif input_txt == 'roll' or input_txt == 'r':
        if (not data.canRoll()):
            print('你的机会用完啦～过会儿再来吧～\n')
            print('下一次抽奖还需等待 ' + data.nextTime())
        else:
            b, sentence = data.rollAndGetString()
            print('\n\n' + 15 * ' ' + sentence + '\n\n')
            if b: 
                print('解锁新句 ({}/{})'.format(data.getUnlockNum(), data.getTotalNum()))
            print('剩余抽奖机会: {}'.format(data.chance - data.usedChance))

    elif input_txt.strip() == "":
        pass
    else:
        print('???')
