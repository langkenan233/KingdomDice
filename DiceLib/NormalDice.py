import random


class NormalDice:
    def __init__(self):
        # 定义每个面及其对应的权重
        faces_weights = [
            (1, 1),  # 面1的权重为1
            (2, 1),  # 面2的权重为1
            (3, 1),  # 面3的权重为1
            (4, 1),  # 面4的权重为1
            (5, 1),  # 面5的权重为1
            (6, 1)  # 面6的权重为1
        ]

        name="普通骰子"
        description="最普通的骰子，没什么特别的"

        self.name = name
        self.description = description
        self.faces = [face for face, _ in faces_weights]
        self.weights = [weight for _, weight in faces_weights]

    def roll(self):
        """
        根据各面的权重随机返回一个结果。
        """
        return random.choices(self.faces, weights=self.weights, k=1)[0]

    def get_name(self):
        """返回骰子的名字"""
        return self.name

    def get_description(self):
        """返回骰子的描述"""
        return self.description
