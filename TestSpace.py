from FuncLib import roll_dice, check_conditions, select_elements_by_index, calculate_score

# 示例使用
dice_number = 6    #默认骰子数为6
score = 0          #分数
turn_over = False  #回合结束标记

print("你的回合")

dice_results = roll_dice(dice_number)

print("骰子结果为:",dice_results)

if check_conditions(dice_results):
    while turn_over == False:
        result = select_elements_by_index(dice_results)  # 选择骰子组合
        print("根据您的选择返回的数组:", result)
        temp = calculate_score(result)
        if temp == "数组非法":
            print("请重新选择")
        else:
            score = score + temp  # 算分
            print(score)
        print("还要继续吗?(y/n)")
        choice = input()
        if choice == "n":
            print("你的回合结束,得分为",score)
            turn_over = True
        else:
            turn_over = False
else:
    print("爆了,你的回合结束")
