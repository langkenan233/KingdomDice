from FuncLib import roll_dice, check_conditions, select_elements_by_index, calculate_score

# 示例使用
dice_results = roll_dice(6)
score = 0

print(dice_results)

if check_conditions(dice_results):
    while score == 0:
        result = select_elements_by_index(dice_results)
        print("根据您的选择返回的数组:", result)
        if calculate_score(result) == "数组非法":
            print("请重新选择")
        else:
            score = calculate_score(result)
            print(calculate_score(result))
else:
    print("爆了")