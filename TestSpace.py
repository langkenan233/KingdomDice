from FuncLib import roll_dice, check_conditions, select_elements_by_index, calculate_score

# 示例使用
dice_max_number = 6
dice_number = dice_max_number  # 默认骰子数为6
score = 0  # 分数
turn_over = False  # 回合结束标记
choice_number = 0  # 选择的骰子数

print("你的回合")

dice_results = roll_dice(dice_number)

while not turn_over:
    print("骰子结果为:", dice_results)
    if check_conditions(dice_results):
        result = select_elements_by_index(dice_results)  # 选择骰子组合
        print("根据您的选择返回的数组:", result)
        choice_number = len(result) # 选择的骰子数
        temp = calculate_score(result) #暂时分数
        if temp == "数组非法":
            print("请重新选择")
        else:
            score = score + temp  # 算分
            print(score)
        dice_number = dice_number - choice_number
        if dice_number == 0:
            print("你拿走了所有的骰子！你的骰子数已刷新！")
            dice_number = dice_max_number
        print("还要继续吗?(y/n),剩下", dice_number,"颗骰子")
        choice = input()
        if choice == "n":
            print("你的回合结束,得分为", score)
            turn_over = True
        else:
            dice_results = roll_dice(dice_number)
    else:
        print("爆了,你的回合结束")
        score = 0
        turn_over = True