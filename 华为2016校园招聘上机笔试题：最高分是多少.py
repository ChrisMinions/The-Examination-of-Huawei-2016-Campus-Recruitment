'''
[编程题] 最高分是多少
时间限制：1秒
空间限制：65536K
老师想知道从某某同学当中，分数最高的是多少，现在请你编程模拟老师的询问。当然，老师有时候需要更新某位同学的成绩. 
输入描述:
输入包括多组测试数据。
每组输入第一行是两个正整数N和M（0 < N <= 30000,0 < M < 5000）,分别代表学生的数目和操作的数目。
学生ID编号从1编到N。
第二行包含N个整数，代表这N个学生的初始成绩，其中第i个数代表ID为i的学生的成绩
接下来又M行，每一行有一个字符C（只取‘Q’或‘U’），和两个正整数A,B,当C为'Q'的时候, 表示这是一条询问操作，
他询问ID从A到B（包括A,B）的学生当中，成绩最高的是多少
当C为‘U’的时候，表示这是一条更新操作，要求把ID为A的学生的成绩更改为B。


输出描述:
对于每一次询问操作，在一行里面输出最高成绩.

输入例子1:
5 7
1 2 3 4 5
Q 1 5
U 3 6
Q 3 4
Q 4 5
U 4 5
U 2 9
Q 1 5

输出例子1:
5
6
5
9
'''

'''
解题思路：简单
   仔细小心就能做出来
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

while True:
    try:
        N, M = [int(each) for each in input().split()]
        scores = [int(each) for each in input().split()]
        operations = []

        for i in range(M):
            operations.append(input().split())
        results = []
        for each in operations:
            if each[0] == 'U':
                scores[int(each[1]) - 1] = int(each[2])
                continue
            else:
                front = min(int(each[1]), int(each[2]))
                back = max(int(each[1]), int(each[2]))
                max_ = 0
                for j in range(front-1, back):
                    if scores[j] > max_:
                        max_ = scores[j]
                results.append(max_)

        for each in results:
            print(each)
    except:
        break
