import random
from collections import defaultdict
# 这段代码模拟了一次扔出num_dice个骰子的过程
def roll_dice(num_dice):
    results = []
    for _ in range(num_dice):
        results.append(random.randint(1, 6))
    return results


def check_conditions(dice):
    """
    检查给定的骰子数组是否包含1或5，或者是否有3个相同的数字。
    如果两个条件都不满足，返回False；否则返回True。

    :param dice: 包含骰子结果的列表
    :return: 如果满足任一条件则为True，否则为False
    """
    # 检查是否含有1或5
    has_one_or_five = any(d == 1 or d == 5 for d in dice)

    # 检查是否有3个一样的数字
    counts = {i: dice.count(i) for i in set(dice)}
    has_three_of_a_kind = any(count >= 3 for count in counts.values())

    # 返回是否满足任一条件
    return has_one_or_five or has_three_of_a_kind


def select_elements_by_index(input_array):
    """
    根据用户提供的索引（从1开始计数）从输入数组中选择元素。

    :param input_array: 输入的数组
    :return: 选中的元素组成的数组
    """
    selected_indices = input("请输入要选择的骰子编号（用逗号分隔）：")
    # 将用户输入的索引字符串转换为整数列表，并调整索引以适应Python的0开始计数
    indices = [int(index.strip()) - 1 for index in selected_indices.split(',')]

    # 根据调整后的索引选择数组元素
    selected_elements = [input_array[i] for i in indices if 0 <= i < len(input_array)]

    return selected_elements

def calculate_score(dice):
    def compute_remaining_score(count):
        score = 0
        # 处理三个或更多相同骰子
        for d in list(count.keys()):
            n = count[d]
            if n >= 3:
                base = 1000 if d == 1 else d * 100
                multiplier = 1
                if n == 4:
                    multiplier = 2
                elif n == 5:
                    multiplier = 4
                elif n >= 6:
                    multiplier = 8
                score += base * multiplier
                count[d] = 0  # 扣除所有该骰子

        # 处理单独的1和5（必须最后处理）
        ones = count.get(1, 0)
        score += ones * 100
        count[1] = 0  # 扣除已计分的1

        fives = count.get(5, 0)
        score += fives * 50
        count[5] = 0  # 扣除已计分的5

        return score

    original_count = defaultdict(int)
    for d in dice:
        original_count[d] += 1

    max_score = -1  # 初始化为-1表示非法

    # 检查所有可能的计分组合
    # 情况1：完整顺子1-6
    if all(original_count[d] >= 1 for d in [1, 2, 3, 4, 5, 6]):
        new_count = defaultdict(int, original_count)
        valid = True
        for d in [1, 2, 3, 4, 5, 6]:
            new_count[d] -= 1
            if new_count[d] < 0:
                valid = False
                break
        if valid:
            remaining_count = defaultdict(int, new_count)
            current_score = 1500 + compute_remaining_score(remaining_count)
            if all(v == 0 for v in remaining_count.values()):
                max_score = max(max_score, current_score)

    # 情况2：小顺子1-5
    if all(original_count[d] >= 1 for d in [1, 2, 3, 4, 5]):
        new_count = defaultdict(int, original_count)
        valid = True
        for d in [1, 2, 3, 4, 5]:
            new_count[d] -= 1
            if new_count[d] < 0:
                valid = False
                break
        if valid:
            remaining_count = defaultdict(int, new_count)
            current_score = 500 + compute_remaining_score(remaining_count)
            if all(v == 0 for v in remaining_count.values()):
                max_score = max(max_score, current_score)

    # 情况3：小顺子2-6
    if all(original_count[d] >= 1 for d in [2, 3, 4, 5, 6]):
        new_count = defaultdict(int, original_count)
        valid = True
        for d in [2, 3, 4, 5, 6]:
            new_count[d] -= 1
            if new_count[d] < 0:
                valid = False
                break
        if valid:
            remaining_count = defaultdict(int, new_count)
            current_score = 750 + compute_remaining_score(remaining_count)
            if all(v == 0 for v in remaining_count.values()):
                max_score = max(max_score, current_score)

    # 情况4：不处理任何顺子
    remaining_count = defaultdict(int, original_count)
    current_score = compute_remaining_score(remaining_count)
    if all(v == 0 for v in remaining_count.values()):
        max_score = max(max_score, current_score)

    return max_score if max_score != -1 else "数组非法"


def roll_all(dice_list):
    """
    对传入的骰子列表中的每一个骰子调用roll方法，并将其结果存入一个数组中。

    :param dice_list: 包含多个骰子对象的列表，每个骰子对象都需要有roll方法。
    :return: 一个包含所有骰子roll结果的列表。
    """
    dice_results = []
    for dice in dice_list:
        result = dice.roll()
        dice_results.append(result)
    return dice_results
