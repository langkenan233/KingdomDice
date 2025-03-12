from DiceLib.NormalDice import NormalDice
from FuncLib import *

# 示例使用
dice_max_number = 6
dice_number = dice_max_number  # 默认骰子数为6
score = 0  # 分数
turn_over = False  # 回合结束标记
choice_number = 0  # 选择的骰子数

normal_dice = NormalDice()  # 初始化普通骰子

dice_list = [normal_dice,
             normal_dice,
             normal_dice,
             normal_dice,
             normal_dice,
             normal_dice]  # 骰子列表，全是普通骰子

dice_list_gaming = dice_list

print("你的回合")

dice_results = roll_all(dice_list_gaming)  # 第一次的结果，数组

while not turn_over:
    print("骰子结果为:", dice_results)
    if check_conditions(dice_results):

        while True:
            selected_indices = input("请输入要选择的骰子编号（用逗号分隔）：")  # 获取用户输入
            result = select_elements_by_index(dice_results, selected_indices)  # 选择骰子组合
            print("根据您的选择返回的数组:", result)
            choice_number = len(result)  # 选择的骰子数
            temp = calculate_score(result)  # 暂时分数
            if temp == "数组非法":
                print("请重新选择")
            else:
                score = score + temp  # 算分
                print(score)
                break

        dice_list_gaming = delete_elements_by_index(dice_list_gaming,selected_indices) #删骰子
        dice_number = dice_number - choice_number #计算骰子个数

        if dice_number == 0:
            print("你拿走了所有的骰子！你的骰子数已刷新！")
            dice_list_gaming=dice_list
            dice_number = dice_max_number
        print("还要继续吗?(y/n),剩下", dice_number, "颗骰子")
        choice = input()
        if choice == "n":
            print("你的回合结束,得分为", score)
            turn_over = True
        else:
            dice_results = roll_all(dice_list_gaming)
    else:
        print("爆了,你的回合结束")
        score = 0
        turn_over = True
