<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# nonebot-plugin-blackjack
👾 _NoneBot 21点插件_ 👾
## 安装
`pip install nonebot-plugin-code`


## 导入
在**bot.py** 导入，语句：
`nonebot.load_plugin("nonebot_plugin_code")`

## 游戏规则

​	通过`签到`命令获取积分，使用积分可以在群内游玩积分对战和21点。

## 签到获取积分规则

​	每日在群内通过`签到`命令来获取积分，每日获取的积分数从1-20点不等，点数越大越难获得。在签到时如果点数为负数，可能还会有奖励？

## 积分对战规则

​	一方先规定这次对战的积分，通过`积分对战 点数`加入对战列表，此时机器人会给出此次游戏的id。然后另一人可以通过`接受对战 游戏id`接受对战，然后系统随机指定一个人胜利。赢者从输者获得事先规定好的积分。总而言之就是完全凭运气的游戏。发起的点数必须小于等于发起者所拥有的点数，同时接受者在接受时也需要有相应的点数。同时，在对战时会有随机的奖励点数，获胜的奖励点数范围为(0，点数 * 0.1)，失败的奖励点数范围为(-点数 * 0.1，点数 * 0.1)，在21点也存在同样的奖励点数。

## 什么是21点？

​	21点是一个传统的扑克牌游戏，和庄家比谁手中的牌点大，但如果牌点超过21点就爆牌，爆牌就输了这场游戏。

## 怎么计算牌点？

​	拿到数字牌就算数字牌的点数，比如拿到2就算2点，拿到10就算10点，但如果拿到J、Q、K那都算10点。

特殊的，A既可以算作1点也可以算作11点！

## 怎么玩？

​	一方先定这场游戏的底分，来发起游戏。发送`21点 游戏底分`即可。发起游戏后，机器人会分配给你一个游戏id。

​	另一方通过发送`接受 游戏id`来加入游戏。

​	加入游戏后通过发送`叫牌 游戏id`来叫牌，发送`停牌 游戏id`来停牌。

​	完成叫牌后，系统会自动完成发起方的叫牌动作，因为在已知对方牌点的情况下只有一种打法。

​	最后系统比较两方的牌点大小，胜者拿到点数，输者扣除点数。

## 特殊的规则

​	在21点中，若在发牌阶段点数是21点，这被称为黑杰克，此时闲家直接获胜。

## 有关21点的所有命令

| 命令            | 解释             |
| --------------- | ---------------- |
| 签到            | 签到             |
| 21点 游戏底分   | 发起21点游戏     |
| 接受 游戏id     | 加入21点游戏     |
| 叫牌 游戏id     | 进行叫牌         |
| 停牌 游戏id     | 进行停牌         |
| 游戏列表        | 查看21点游戏列表 |
| 积分对战 点数   | 发起对战         |
| 接受对战 对战id | 接受对战         |
| 对战列表        | 查看对战列表     |

## 使用例

![](pic\21点使用例.jpg)

![](pic\1.jpg)

![2](pic\2.jpg)