'''
[编程题] 扑克牌大小
时间限制：10秒
空间限制：131072K
扑克牌游戏大家应该都比较熟悉了，一副牌由54张组成，含3~A，2各4张，小王1张，大王1张。
牌面从小到大用如下字符和字符串表示（其中，小写joker表示小王，大写JOKER表示大王）:) 
3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER 
输入两手牌，两手牌之间用“-”连接，每手牌的每张牌以空格分隔，“-”两边没有空格，如：4 4 4 4-joker JOKER
请比较两手牌大小，输出较大的牌，如果不存在比较关系则输出ERROR

基本规则：
（1）输入每手牌可能是个子，对子，顺子（连续5张），三个，炸弹（四个）和对王中的一种，不存在其他情况，
由输入保证两手牌都是合法的，顺子已经从小到大排列；
（2）除了炸弹和对王可以和所有牌比较之外，其他类型的牌只能跟相同类型的存在比较关系
（如，对子跟对子比较，三个跟三个比较），不考虑拆牌情况（如：将对子拆分成个子）
（3）大小规则跟大家平时了解的常见规则相同，个子，对子，三个比较牌面大小；顺子比较最小牌大小；
炸弹大于前面所有的牌，炸弹之间比较牌面大小；对王是最大的牌；
（4）输入的两手牌不会出现相等的情况。

答案提示：
（1）除了炸弹和对王之外，其他必须同类型比较。
（2）输入已经保证合法性，不用检查输入是否是合法的牌。
（3）输入的顺子已经经过从小到大排序，因此不用再排序了.

输入描述:
输入两手牌，两手牌之间用“-”连接，每手牌的每张牌以空格分隔，“-”两边没有空格，如4 4 4 4-joker JOKER。


输出描述:
输出两手牌中较大的那手，不含连接符，扑克牌顺序不变，仍以空格隔开；如果不存在比较关系则输出ERROR。

输入例子1:
4 4 4 4-joker JOKER

输出例子1:
joker JOKER
'''

'''
解题思路：仔细小心
   华为笔试的题目解题思路都很简单，一眼就能望到头，不需要太多思考，只要仔细小心的分析清楚每一种情况，
   就都能做出来
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

def judge_token(cs):
    length = len(cs)
    if length == 1:
        return 'single'
    elif length == 3:
        return 'triple'
    elif length == 4:
        return 'bomb'
    elif length == 5:
        return 'seq'
    elif length == 2:
        if cs == ['joker', 'JOKER']:
            return 'j-bomb'
        else:
            return 'double'

card_dict = {'3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11,
             'A': 12, '2': 13, 'joker': 14, 'JOKER': 15}

while True:
    try:
        cards = input().split('-')
        cards_1 = cards[0].split()
        cards_2 = cards[1].split()
        cards_1_token = judge_token(cards_1)
        cards_2_token = judge_token(cards_2)
        if cards_1_token != 'bomb' and cards_1_token != 'j-bomb' and cards_2_token != 'bomb' and cards_2_token != 'j-bomb':
            if cards_1_token == cards_2_token:
                if card_dict[cards_1[0]] > card_dict[cards_2[0]]:
                    print(' '.join(cards_1))
                else:
                    print(' '.join(cards_2))
            else:
                print('ERROR')
        elif (cards_1_token == 'bomb' or cards_1_token == 'j-bomb') and (cards_2_token != 'bomb' and cards_2_token != 'j-bomb'):
            print(' '.join(cards_1))
        elif (cards_1_token != 'bomb' and cards_1_token != 'j-bomb') and (cards_2_token == 'bomb' or cards_2_token == 'j-bomb'):
            print(' '.join(cards_2))
        elif cards_1_token == 'bomb' and cards_2_token == 'j-bomb':
            print(' '.join(cards_2))
        elif cards_1_token == 'j-bomb' and cards_2_token == 'bomb':
            print(' '.join(cards_1))
        else:
            if card_dict[cards_1[0]] > card_dict[cards_2[0]]:
                print(' '.join(cards_1))
            else:
                print(' '.join(cards_2))
    except:
        break
