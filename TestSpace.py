from FuncLib import roll_dice, check_conditions, select_elements_by_index, calculate_score

# 示例使用
dice_results = roll_dice(6)

print(dice_results)

if check_conditions(dice_results):
    result = select_elements_by_index(dice_results)
    print("根据您的选择返回的数组:", result)
    print(calculate_score(result))
else:
    print("爆了")