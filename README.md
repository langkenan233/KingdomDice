# 天国：骰子

该项目为浪客楠构思游戏原型代码

灵感来源于2025/3/9与好哥们玩骰子游戏后在轻轨上突发奇想而得

SixDice 模拟一次丢出六颗骰子的过程

ServerSimulation 模拟服务器端

ClientSimulation 模拟客户端

游戏流程

1. 摇6个骰子

2. 判断能否计分--先看有无1，5--若没有，则看有无3个一样的数--若没有，则没分--若没分，则分数作废，到对手

3. 选择其中的X个骰子

4. 选择计分 或 计分并跳过

5. 若选择计分，则继续骰6-X个骰子 转2

6. 若计分并跳过,则到对手



