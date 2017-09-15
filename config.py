# -*- coding=utf8 -*-
import pickle
import datetime
from random import *
from time import *
debug = False
def debug_print(s):
    if debug:
        print(s)

k_birth_date = 21
k_birth_month = 9
k_birth_year = 2017
class UnionData(object):
    def __init__(self):
        try:
            fin = open('data/dataFile', 'rb')
            data = pickle.load(fin)
            self.chance = data.chance
            self.usedChance = data.usedChance
            self.unlockList = data.unlockList
            self.unlockNum = data.unlockNum
            debug_print("{} {} {} {}\n".format(self.chance, self.usedChance, self.unlockList, self.unlockNum))

        except Exception:
            self.chance = self.calChance()
            self.usedChance = 0
            self.unlockList = [False for x in range(101)]
            self.unlockNum = 0
            debug_print("uniondata find no file")
            debug_print("{} {} {} {}\n".format(self.chance, self.usedChance, self.unlockList, self.unlockNum))

            
    def close(self):
        debug_print("destruction function run")
        fout = open('data/dataFile', 'wb')
        pickle.dump(self, fout)
        debug_print("{} {} {} {}\n".format(self.chance, self.usedChance, self.unlockList, self.unlockNum))

    def UseChance(self):
        self.usedChance += 1
    def calChance(self):
        localTime = localtime(time())
        startTime = datetime.date(k_birth_year, k_birth_month, k_birth_date)
        currentTime = datetime.date(localTime.tm_year, localTime.tm_mon, localTime.tm_mday)
        return (currentTime - startTime).days * 9 + localTime.tm_hour // 8 * 3 + 5
    def unLock(self, i):
        if (self.unlockList[i] == False):
            self.unlockList[i] = True
            self.unlockNum += 1
            return True
        return False

    def getUnlockNum(self):
        return self.unlockNum
    def getTotalNum(self):
        return 100 
    def canRoll(self):
        return self.chance > self.usedChance
    def cheat(self):
        self.unlockNum = 100
        for i in range(1, 101):
            self.unlockList[i] = True
    def getString(self, i):
        if (self.unlockList[i] == True):
            if i == 100:
                index = txt.find(str(i))
                return txt[index:].strip()
            else:
                indexFirst = txt.find(str(i))
                indexLast = txt.find(str(i + 1))
                print_txt = txt[indexFirst:indexLast]
                print_txt = print_txt.strip()
                return print_txt
        else:
            return ""
    def rollAndGetString(self):
        if (not self.canRoll()):
            return False, ""
        i = randint(1, 100)
        b = self.unLock(i)
        self.UseChance()
        self.unlockList[i] = True
        return b, self.getString(i)
    def nextTime(self):
        localTime = localtime(time())
        sec = 60 - localTime.tm_sec
        if (localTime.tm_sec != 0):
            minute = 59
        else:
            minute = 60

        mie = minute - localTime.tm_min
        if (localTime.tm_min != 0):
            hour_minus = 1
        else:
            hour_minus = 0
        if (localTime.tm_hour < 8):
            hour = 8 - localTime.tm_hour - hour_minus
        elif(localTime.tm_hour < 16):
            hour = 16 - localTime.tm_hour - hour_minus
        else:
            hour = 24 - localTime.tm_hour - hour_minus
        if(sec == 60): sec = 0
        if(mie == 60): mie = 0
        return "{:02d}:{:02d}:{:02d}".format(hour, mie, sec)





txt = '''
1、千秋无绝色，悦目是佳人；倾国倾城貌，惊为天下人

2、芙蓉不及美人妆，水殿风来珠翠香

3、态浓意远淑且真，肌理细腻骨肉匀

4、俏丽若三春之桃，清素若九秋之菊

5、眉梢眼角藏秀气，声音笑貌露温柔

6、翩若惊鸿，婉若游龙

7、美人既醉，朱颜酡些

8、冰肌自是生来瘦，那更分飞后

9、邀人傅脂粉，不自著罗衣

10、秀色掩今古，荷花羞玉颜

11、北方有佳人，绝世而独立

12、垆边人似月，皓腕凝霜雪

13、届笑春桃兮，云堆翠髻；唇绽樱颗兮，榴齿含香

14、娴静犹如花照水，行动好比风扶柳

15、独自莫凭栏，无限江山，别时容易见时难

16、袅娜少女羞，岁月无忧愁

17、芳容丽质更妖娆，秋水精神瑞雪标

18、珠缨旋转星宿摇，花蔓抖擞龙蛇动

19、蒹葭苍苍，白露为霜。所谓伊人，在水一方

20、花心定有何人捻，晕晕如娇靥

21、回眸一笑百媚生，六宫粉黛无颜色

22、脉脉眼中波，盈盈花盛处

23、巧笑倩兮，美目盼兮

24、天长地久有时尽，此恨绵绵无绝期

25、君还知道相思苦，怎忍抛奴去

26、不辞迢递过关山，只恐别郎容易、见郎难

27、朱粉不深匀,闲花淡淡香。细看诸处好,人人道柳腰身

28、芸芸众神赞，飘飘仙子舞

29、清水出芙蓉，天然去雕饰

30、一枝红艳露凝香，云雨巫山枉断肠

31、云一涡，玉一梭，淡淡衫儿薄薄罗，轻颦双黛螺

32、凤眼半弯藏琥珀，朱唇一颗点樱桃

33、柳腰春风过，百鸟随香走

34、罗衣何飘飘，轻裾随风远。顾盼遗光彩，长啸气若兰

35、笑颜如花绽，玉音婉转流

36、皎皎兮似轻云之蔽月，飘飘兮若回风之流雪

37、杨家有女初长成，养在深闺人未识

38、风回小院庭芜绿，柳眼春相续

39、温柔几许缘何散，爱恨声声怨

40、纤纤作细步，精妙世无双

41、天生丽质难自弃，一朝选在君王侧

42、芙蓉如面柳如眉，对此如何不泪垂

43、转眄流精，光润玉颜。含辞未吐，气若幽兰。华容婀娜，令我忘餐

44、披罗衣之璀粲兮，珥瑶碧之华琚。戴金翠之首饰，缀明珠以耀躯

45、丹唇外朗，皓齿内鲜，明眸善睐，靥辅承权

46、昨日乱山昏，来时衣上云

47、绝代有佳人，幽居在空谷

48、宝髻松松挽就，铅华淡淡妆成

49、荣曜秋菊，华茂春松

50、烛明香暗画楼深，满鬓清霜残雪思难任

51、凭阑半日独无言，依旧竹声新月似当年

52、爱彼之貌容兮，香培玉琢

53、羡彼之良质兮，冰清玉润

54、美彼之态度兮，凤翥龙翔

55、慕彼之华服兮，闪灼文章

56、其静若何，松生空谷

57、其艳若何，霞映澄塘

58、其神若何，月射寒江

59、纤腰之楚楚兮，回风舞雪；珠翠之辉辉兮，满额鹅黄

60、窈窕淑女，君子好逑

61、拆桐花烂漫，乍疏雨、洗清明

62、柔桡轻曼，妩媚纤弱

63、班姬续史之姿，谢庭咏雪之态

64、顾盼生辉，撩人心怀

65、若把西湖比西子，浓妆淡抹总相宜

66、借问汉宫谁得似？可怜飞燕倚新妆

67、俊眉修眼，顾盼神飞，文彩精华，见之忘俗

68、有女妖且丽，裴回湘水湄。水湄兰杜芳，采之将寄谁

69、媚眼含羞合，丹唇逐笑开。风卷葡萄带，日照石榴裙

70、腮凝新荔，鼻腻鹅脂，温柔沉默，观之可亲

71、玉容寂寞泪阑干，梨花一枝春带雨

72、镜中貌，月下影，隔帘形，睡初醒

73、翩若轻云出岫，携佳人兮步迟迟，腰肢袅娜似弱柳

74、委委佗佗美也，皆佳丽美艳之貌

75、丹唇列素齿，翠彩发蛾眉

76、绣幕芙蓉一笑开，斜偎宝鸭衬香腮，眼波才动被人猜

77、借水开花自一奇，水沉为骨玉为肌

78、皎若太阳升朝霞，灼若芙渠出鸿波

79、秀色空绝世，馨香为谁传？

80、质傲清霜色，香含秋露华

81、共道幽香闻十里，绝知芳誉亘千乡

82、娉娉袅袅十三余，豆蔻梢头二月初

83、淡眉如秋水，玉肌伴轻风

84、有美一人，婉如清扬

85、静若处子，动若脱兔

86、眉将柳而争绿，面共桃而竞红

87、灿如春华，皎如秋月

88、渐消酒色朱颜浅，欲语离情翠黛低

89、衣带渐宽终不悔，为伊消得人憔悴

90、盛服浓妆韶颜雅容

91、香雾云鬟湿，清辉玉臂寒

92、普天壤其无俪，旷千载而特生

93、秀靥艳比花娇，玉颜艳比春“红”

94、桃之夭夭，灼灼其华

95、隔户杨柳弱袅袅，恰似十五女儿腰

96、尝矜绝代色，复恃倾城姿

97、#彩蛋#
其实认识你和邓鸡真的是件很幸运很幸福的事儿，嗯。说你们是我的半个男女朋友其实一点也不夸张。我觉得我们会是一辈子的朋友吧哈哈哈哈。希望我们以后可以继续旅游继续浪继续玩儿～嗯哒 我爱你们（捂脸

98、螓首蛾眉，巧笑倩兮

99、秀色掩今古，荷花羞玉颜

100、蓦然回首，亭亭玉立
'''

