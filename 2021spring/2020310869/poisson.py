# -*- coding: utf-8 -*-

"""泊松仿真"""

import sys
import random
import collections
import matplotlib.pyplot as plt


class Poisson:
    def __init__(self, rate=sys.argv[1]):
        self.rate = int(rate)

        self.time = 1  # 单位时间
        if len(sys.argv) > 2 and sys.argv[2] != "":
            self.time = int(sys.argv[2])  # 手动指定时间范围

        self.EXP_NUM = 100000  # 实验次数
        self.NUM_LEVEL = 2  # 数量级

    def generator(self, prob):
        """仿真结果生成器"""
        while True:
            if random.random() < prob:
                yield 1
            else:
                yield 0

    def perform_exp(self, rate, time):
        """进行一次实验
        每次实验中，时间分片的数量比rate高两个数量级
        """
        level = len(str(rate))
        shard_num = 10 ** (level + self.NUM_LEVEL)  # 计算时间分片的数量

        gen = self.generator(rate / shard_num)

        cnt = 0
        for _ in range(time * shard_num):
            cnt += next(gen)
        
        return cnt

    def perform_exps(self, exp_num, rate, time):
        """多次实验，得到分布"""
        lst = []
        for _ in range(exp_num):
            lst.append(self.perform_exp(rate, time))

        return sorted(collections.Counter(lst).items(), key=lambda e: e[0])

    def draw(self, sorted_list):
        """画图"""
        s = sum([e[1] for e in sorted_list])
        x = [e[0] for e in sorted_list]
        y = [e[1] / s for e in sorted_list]

        plt.plot(x, y)
        
        plt.xlabel("k")
        plt.ylabel("P(k)")
        plt.show()

    def main(self):
        sorted_list = self.perform_exps(self.EXP_NUM, self.rate, self.time)
        self.draw(sorted_list)

    @staticmethod
    def calculator(rate, t, k):
        """用于计算泊松函数的概率 P(k|t,lambda)
           rate: lambda
           t: t
           k: k
        """
        import math
        return (rate * t) ** k / math.factorial(k) * math.exp(-rate * t)


if __name__ == '__main__':
    p = Poisson()
    p.main()