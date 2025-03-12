from DiceLib.NormalDice import NormalDice


class LuckyDice(NormalDice):
    def __init__(self):
        super().__init__()
        faces_weights = [
            (1, 4),  # 面1的权重为3
            (2, 1),  # 面2的权重为1
            (3, 1),  # 面3的权重为1
            (4, 1),  # 面4的权重为1
            (5, 3),  # 面5的权重为3
            (6, 2)   # 面6的权重为1
        ]

        name = "幸运骰子"
        description = "一颗更加容易让人感到幸运的骰子"

        self.name = name
        self.description = description
        self.faces = [face for face, _ in faces_weights]
        self.weights = [weight for _, weight in faces_weights]

