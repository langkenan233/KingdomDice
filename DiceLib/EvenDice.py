from DiceLib.NormalDice import NormalDice


class EvenDice(NormalDice):
    def __init__(self):
        super().__init__()
        faces_weights = [
            (1, 1),  # 面1的权重为3
            (2, 4),  # 面2的权重为1
            (3, 1),  # 面3的权重为1
            (4, 4),  # 面4的权重为1
            (5, 1),  # 面5的权重为3
            (6, 4)   # 面6的权重为1
        ]

        name = "偶数骰子"
        description = "更容易出现偶数"

        self.name = name
        self.description = description
        self.faces = [face for face, _ in faces_weights]
        self.weights = [weight for _, weight in faces_weights]