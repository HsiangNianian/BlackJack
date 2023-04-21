# 📢插件维护通知

由于长时间缺乏更新和维护，使用该插件可能会出现各种大小问题。

## ⏫升级 OlivOS

为了继续直接在 `OlivOS` 上使用 `BlackJack` 插件，建议升级 `OlivOS` 到最新版本，并选择使用 Bilibili 弹幕协议登录。

## 🐱‍🚀加入群聊

如果您希望继续使用此插件，可以加入我们的群聊 (群ID: [`971050440`](https://jq.qq.com/?_wv=1027&k=VJqxAFTg)) 并提供更详细的信息。我们将尽力在空闲时间内修复它。

## BlackJack <img align="right" width="400" src="image/README/1682061505967.png">

> 基于 OlivOS 和 OlivaDiceCore 的简单交互式 21 点游戏

![](https://img.shields.io/github/last-commit/HsiangNianian/BlackJack) [![CI](https://github.com/HsiangNianian/BlackJack/actions/workflows/ci.yml/badge.svg)](https://github.com/HsiangNianian/BlackJack/actions/workflows/ci.yml) [![](https://img.shields.io/github/downloads/HsiangNianian/BlackJack/total)](https://github.com/HsiangNianian/BlackJack/tags) [![](https://img.shields.io/github/v/release/HsiangNianian/BlackJack)](https://github.com/HsiangNianian/BlackJack/releases)

### 📕21 点游戏规则书

1. 游戏目标

游戏的目标是使您的手尽可能接近 21 分而不超过，或比庄家更高的手而不超过 21 分。

2. 游戏设置

- 在每局游戏开始时，系统生成一副牌并洗牌。
- 玩家输入下注金额，随后系统会发两张卡给玩家和庄家。
- 玩家可以看到自己的牌和庄家的一张牌。

3. 游戏进程

- 玩家开始决定是否要要牌（再取一张牌）或停牌（继续当前手）。
- 如果玩家选择要牌，则系统将从牌堆中随机抽出另一张牌并加入玩家的手中。
- 如果玩家手中的点数超过 21 分，则玩家输掉赌注。
- 如果玩家选择停牌，则轮到庄家决定是否要牌或停牌。
- 庄家必须取牌，直到总点数达到 17 分或更高。
- 如果庄家手上的点数超过 21 分，则庄家输掉赌注。
- 如果庄家选择停牌，则将庄家和玩家的手进行比较，点数更高的手获胜。如果两手相等，则平局。

4. 牌值计算

- A 可以计为 1 分或 11 分，面牌（牌面 J、Q、K）价值为 10 分，其他牌的价值为其牌面值。
- 玩家手中的牌点值之和为玩家分数。
- 庄家手中的牌点值之和为庄家分数。

5. 结算规则

- 如果玩家手中的点数超过 21 分，则玩家输掉赌注。
- 如果庄家手上的点数超过 21 分，则庄家输掉赌注。
- 如果庄家和玩家的手都是 21 分或以下，则最接近 21 分的手获胜。
- 如果庄家和玩家的手相等，则平局。

6. 游戏结束

- 每局游戏结束后，系统将询问您是否要继续玩。
- 如果玩家选择继续，则会清空玩家和庄家手中的牌，并开始新的一局游戏。
- 如果玩家输掉所有赌注，则游戏结束。

7. 命令参数

`.BlackJack -n|--name [玩家名称，默认值：无可救药的赌徒] -b|--bet [初始赌注，默认值：1000]` //这些可以省略。

享受游戏！

### ⬇ 下载

您可以在右侧的 [`release`](https://github.com/HsiangNianian/BlackJack/releases/latest) 部分找到打包和未压缩的 `opk` 插件文件供下载。

或者，您也可以 [`fork`](https://github.com/HsiangNianian/BlackJack/fork) 此项目，并在 [`actions`](https://github.com/HsiangNianian/BlackJack/actions) 部分的 `artifact` 下找到压缩文件。

### 👨‍🚀 贡献者

<a href="https://github.com/HsiangNianian/BlackJack/graphs/contributors">
  <img width="150" src="https://contrib.rocks/image?repo=HsiangNianian/BlackJack" />
</a>

### 📄 License

[GPL 3.0](https://github.com/HsiangNianian/BlackJack/blob/main/LICENSE) © 2023-PRESENT [Jian Luchun](https://github.com/HsiangNianian)