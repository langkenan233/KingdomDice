import random
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
    :param selected_indices: 用户输入的索引列表（字符串形式，逗号分隔）
    :return: 选中的元素组成的数组
    """
    selected_indices = input("请输入要选择的元素索引（用逗号分隔）：")
    # 将用户输入的索引字符串转换为整数列表，并调整索引以适应Python的0开始计数
    indices = [int(index.strip()) - 1 for index in selected_indices.split(',')]

    # 根据调整后的索引选择数组元素
    selected_elements = [input_array[i] for i in indices if 0 <= i < len(input_array)]

    return selected_elements


from collections import defaultdict

def calculate_score(dice):
    def compute_remaining_score(count):
        score = 0
        # 处理三个或更多相同骰子的情况
        for d in list(count.keys()):
            n = count[d]
            if n >= 3:
                if d == 1:
                    base = 1000
                else:
                    base = d * 100
                if n == 3:
                    multiplier = 1
                elif n == 4:
                    multiplier = 2
                elif n == 5:
                    multiplier = 4
                else:  # n >=6
                    multiplier = 8
                score += base * multiplier
                count[d] = 0  # 扣除所有骰子
        # 处理单独的1和5
        score += count.get(1, 0) * 100
        score += count.get(5, 0) * 50
        return score

    original_count = defaultdict(int)
    for d in dice:
        original_count[d] += 1

    max_score = 0

    # 检查所有可能的顺子情况，并计算每种情况下的得分
    # 情况1：顺子1-6
    if all(original_count[d] >= 1 for d in [1, 2, 3, 4, 5, 6]):
        new_count = defaultdict(int, original_count)
        for d in [1, 2, 3, 4, 5, 6]:
            new_count[d] -= 1
        current_score = 1500 + compute_remaining_score(new_count)
        max_score = max(max_score, current_score)

    # 情况2：小顺子1-5
    if all(original_count[d] >= 1 for d in [1, 2, 3, 4, 5]):
        new_count = defaultdict(int, original_count)
        for d in [1, 2, 3, 4, 5]:
            new_count[d] -= 1
        current_score = 500 + compute_remaining_score(new_count)
        max_score = max(max_score, current_score)

    # 情况3：小顺子2-6
    if all(original_count[d] >= 1 for d in [2, 3, 4, 5, 6]):
        new_count = defaultdict(int, original_count)
        for d in [2, 3, 4, 5, 6]:
            new_count[d] -= 1
        current_score = 750 + compute_remaining_score(new_count)
        max_score = max(max_score, current_score)

    # 情况4：不处理任何顺子
    current_score = compute_remaining_score(defaultdict(int, original_count))
    max_score = max(max_score, current_score)

    return max_score
