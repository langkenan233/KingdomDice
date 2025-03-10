import random
# 这段代码模拟了一次扔出六个骰子的过程
def roll_dice(num_dice):
    results = []
    for _ in range(num_dice):
        results.append(random.randint(1, 6))
    return results

num_dice = 6

dice_results = roll_dice(num_dice)

print(f"你扔出了 {num_dice} 颗骰子: {dice_results}")