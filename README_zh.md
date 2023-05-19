# 📢插件维护通知

由于长时间缺乏更新和维护，使用该插件可能会出现各种大小问题。

## ⏫升级 OlivOS

为了继续直接在 `OlivOS` 上使用 `BlackJack` 插件，建议升级 `OlivOS` 到最新版本，并选择使用 Bilibili 弹幕协议登录。

## 🐱‍🚀加入群聊

如果您希望继续使用此插件，可以加入我们的群聊 (群ID: [`971050440`](https://jq.qq.com/?_wv=1027&k=VJqxAFTg)) 并提供更详细的信息。我们将尽力在空闲时间内修复它。

## BlackJack <img align="right" width="30" src="https://ghproxy.com/github.com/HsiangNianian/BlackJack/blob/main/image/README/1682061505967.png">
* *插件基于 [OlivOS](https://github.com/OlivOS-Team/OlivOS)*
* *插件基于 [OlivaDiceCore](https://github.com/OlivOS-Team/OlivaDiceCore)*

> 基于 OlivOS 和 OlivaDiceCore 的简单交互式 21 点游戏

![](https://img.shields.io/github/last-commit/HsiangNianian/BlackJack) [![CI](https://github.com/HsiangNianian/BlackJack/actions/workflows/ci.yml/badge.svg)](https://github.com/HsiangNianian/BlackJack/actions/workflows/ci.yml) [![](https://img.shields.io/github/downloads/HsiangNianian/BlackJack/total)](https://github.com/HsiangNianian/BlackJack/tags) [![](https://img.shields.io/github/v/release/HsiangNianian/BlackJack)](https://github.com/HsiangNianian/BlackJack/releases)

<details open>
<Summary>
  <h3>📕21 点游戏规则书</h3>
  </Summary>
  
1. 游戏目标

在不爆牌（手中的牌面点数超过21）的情况下，使自己手中的牌点数尽量接近21点，或者比庄家的牌点数更高。

2. 牌局准备

- 游戏开始时，系统会生成一副扑克牌，并将其打乱；
- 玩家需要输入赌注，然后系统会将两张牌发给玩家和庄家；
- 玩家可以看到自己手中的牌以及庄家的一张牌。

3. 游戏流程

- 玩家开始行动，可以选择“要牌”（继续抽牌）或“停牌”（不再抽牌）；
- 如果玩家选择“要牌”，系统会从扑克牌中随机抽出一张牌，并加入玩家手中的牌中；
- 如果玩家的牌面点数超过21点，则认为玩家已爆牌，游戏结束，玩家输掉赌注；
- 如果玩家选择“停牌”，则轮到庄家行动；
- 庄家会根据自己手中的牌面点数来决定是否继续抽牌；
- 如果庄家的牌面点数超过21点，则认为庄家已爆牌，玩家赢得赌注；
- 如果庄家选择“停牌”，则比较玩家和庄家的牌面点数，点数更高者胜利，如果点数相同则为平局。

4. 牌面点数计算

- A可以表示1或11点，2-10按照牌面点数计算，J、Q、K均算作10点；
- 玩家手中牌面点数之和即为玩家的点数；
- 庄家根据自己手中的牌面点数来决定是否继续抽牌，庄家手中牌面点数之和即为庄家点数。

5. 结算规则

- 如果玩家的牌面点数超过21点，则认为玩家已爆牌，游戏结束，玩家输掉赌注；
- 如果庄家的牌面点数超过21点，则认为庄家已爆牌，玩家赢得赌注；
- 如果玩家和庄家的牌面点数都不超过21点，则比较两者点数大小，点数更高者胜利；
- 如果玩家和庄家的牌面点数相同，则为平局。

6. 游戏结束

- 每次游戏结束后，系统会询问玩家是否继续游戏；
- 如果玩家选择继续，则清空玩家和庄家手中的牌，重新开始新一轮游戏；
- 如果玩家输掉了所有赌注，则游戏结束。

7. 指令参数

.BlackJack -n|--name [玩家名称，默认:无可救药的赌徒] -b|--bet [初始赌注，默认:1000] //这些都可以省略

愉快游戏！

  </details>
  
### ⬇ 下载

您可以在右侧的 [`release`](https://github.com/HsiangNianian/BlackJack/releases/latest) 部分找到打包和未压缩的 `opk` 插件文件供下载。

或者，您也可以 [`fork`](https://github.com/HsiangNianian/BlackJack/fork) 此项目，并在 [`actions`](https://github.com/HsiangNianian/BlackJack/actions) 部分的 `artifact` 下找到压缩文件。

### 👨‍🚀 贡献者

<a href="https://github.com/HsiangNianian/BlackJack/graphs/contributors">
  <img width="50" src="https://contrib.rocks/image?repo=HsiangNianian/BlackJack" />
</a>

### 📄 License

[GPL 3.0](https://github.com/HsiangNianian/BlackJack/blob/main/LICENSE) © 2023-PRESENT [简律纯](https://github.com/HsiangNianian)
