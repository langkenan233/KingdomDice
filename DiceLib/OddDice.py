from DiceLib.NormalDice import NormalDice


class OddDice(NormalDice):
    def __init__(self):
        super().__init__()
        faces_weights = [
            (1, 4),  # 面1的权重为3
            (2, 1),  # 面2的权重为1
            (3, 4),  # 面3的权重为1
            (4, 1),  # 面4的权重为1
            (5, 4),  # 面5的权重为3
            (6, 1)  # 面6的权重为1
        ]

        name = "奇数骰子"
        description = "更容易出现奇数"

        self.name = name
        self.description = description
        self.faces = [face for face, _ in faces_weights]
        self.weights = [weight for _, weight in faces_weights]