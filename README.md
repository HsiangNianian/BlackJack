[中文](./README_zh.md)

# 📢Plugin Maintenance Notice

Due to the lack of updates and maintenance over an extended period of time, there may be various big and small issues with using this plugin.

## ⏫Upgrade OlivOS

To continue using the `BlackJack` plugin directly on `OlivOS`, we recommend upgrading `OlivOS` to the latest version and choosing to login with the Bilibili Danmaku protocol.

## 🐱‍🚀Join Group Chat

If you wish to continue using this plugin, you can join our group chat (Group ID: [`971050440`](https://jq.qq.com/?_wv=1027&k=VJqxAFTg)) and provide more detailed information. We will make efforts to fix it in our free time.

## BlackJack <img align="right" width="30" src="https://ghproxy.com/github.com/HsiangNianian/BlackJack/blob/main/image/README/1682061505967.png">
* *Plugin based on [OlivOS](https://github.com/OlivOS-Team/OlivOS)*
* *Plugin based on [OlivaDiceCore](https://github.com/OlivOS-Team/OlivaDiceCore)*

> A simple interactive 21-point game based on OlivOS and OlivaDiceCore

![](https://img.shields.io/github/last-commit/HsiangNianian/BlackJack) [![CI](https://github.com/HsiangNianian/BlackJack/actions/workflows/ci.yml/badge.svg)](https://github.com/HsiangNianian/BlackJack/actions/workflows/ci.yml) [![](https://img.shields.io/github/downloads/HsiangNianian/BlackJack/total)](https://github.com/HsiangNianian/BlackJack/tags) [![](https://img.shields.io/github/v/release/HsiangNianian/BlackJack)](https://github.com/HsiangNianian/BlackJack/releases)

<details close>
<Summary>
  <h3>📕 21-point Gaming Rule Book</h3>
  </Summary>

1. Game Objective

The aim of the game is to get your hand as close as possible to the value of 21 without going over OR to have a higher value hand than the dealer without exceeding 21.

2. Game Setup

- At the start of each game, the system generates a deck of cards and shuffles them.
- Players enter their bet and two cards are dealt to both the player and the dealer.
- The player can see their own cards and one of the dealer's card.

3. Game Process

- The player begins by deciding whether to hit (take another card) or stand (stay with current hand).
- If the player chooses to hit, the system will randomly draw another card from the deck and add it to the player's hand.
- If the value of the player's hand exceeds 21, the player busts and loses their bet.
- If the player chooses to stand, then it is the dealer's turn to decide whether to hit or stand.
- The dealer must take cards until the total is 17 or more points.
- If the dealer's hand exceeds 21, the dealer busts and the player wins the bet.
- If the dealer chooses to stand, then the hands of the dealer and the player are compared, and the higher hand wins. If the hands are equal, it is a tie.

4. Card Value Calculation

- Aces can count as either 1 or 11 points, face cards (J, Q, K) are worth 10 points, and all other cards are worth their face value.
- The sum of the value of cards in a player's hand is the player's score.
- The sum of the value of cards in the dealer's hand is the dealer's score.

5. Settlement Rules

- If the player's hand exceeds 21, the player busts and loses their bet.
- If the dealer's hand exceeds 21, the dealer busts and the player wins the bet.
- If the hands of the dealer and the player are both 21 or less, the hand closest to 21 wins.
- If the hands of the dealer and the player are equal, it is a tie.

6. End of Game

- After each game ends, the system will ask if you want to continue playing.
- If the player chooses to continue, the cards in the player's and dealer's hands will be cleared and a new game will begin.
- If the player loses all their bets, the game will end.

7. Command Parameters

`.BlackJack -n|--name [Player Name, Default: 无可救药的赌徒] -b|--bet [Initial Bet, Default: 1000]` //These can be omitted.

Enjoy the game!
</details>

### ⬇ Download

You can find the packaged and uncompressed `opk` plugin file for download in the [`release`](https://github.com/HsiangNianian/BlackJack/releases/latest) section on the right side.

Alternatively, you can also [`fork`](https://github.com/HsiangNianian/BlackJack/fork) this project and find the compressed file under `artifact` in the [`actions`](https://github.com/HsiangNianian/BlackJack/actions) section.

### 👨‍🚀 Contributors

<a href="https://github.com/HsiangNianian/BlackJack/graphs/contributors">
  <img width="50" src="https://contrib.rocks/image?repo=HsiangNianian/BlackJack" />
</a>

### 📄 License

[GPL 3.0](https://github.com/HsiangNianian/BlackJack/blob/main/LICENSE) © 2023-PRESENT [简律纯](https://github.com/HsiangNianian)
