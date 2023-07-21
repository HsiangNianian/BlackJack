# -*- encoding: utf-8 -*-
'''
     ██╗██╗   ██╗██╗   ██╗███╗   ██╗██╗  ██╗ ██████╗ 
     ██║╚██╗ ██╔╝██║   ██║████╗  ██║██║ ██╔╝██╔═══██╗
     ██║ ╚████╔╝ ██║   ██║██╔██╗ ██║█████╔╝ ██║   ██║
██   ██║  ╚██╔╝  ██║   ██║██║╚██╗██║██╔═██╗ ██║   ██║
╚█████╔╝   ██║   ╚██████╔╝██║ ╚████║██║  ██╗╚██████╔╝
 ╚════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ 
                                                     
    Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    https://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import time
import random
import OlivOS
import BlackJack  # type: ignore
import OlivaDiceCore  #type: ignore
import argparse

parser = argparse.ArgumentParser(description='21点')
parser.add_argument('-n', '--name', default='无可救药的赌徒', help='玩家名称')
parser.add_argument('-b', '--bet', default=1000, help='初始赌注')

msg_id = None
bet = None
contextWaitTime = 60 * 2
contextFeq = 0.1
dictReplyContextReg = {}
# 卡牌和点数
suits = ['♠️', '♥️', '♣️', '♦️']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
card_values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
               '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 10, 'K': 10}
rule = """\
21点游戏规则书

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

愉快游戏！"""

class Event(object):
    def init(self, Proc):  # type: ignore
        global global_Proc
        global_Proc = Proc

    def group_message(self, Proc: OlivOS.pluginAPI.shallow) -> None:    # type: ignore
        """
        Receive group messages
        """
        play_game(self, Proc)

    def private_message(self, Proc: OlivOS.pluginAPI.shallow) -> None:    # type: ignore
        """
        Receive private messages
        """
        play_game(self, Proc)


def play_game(plugin_event: OlivOS.API.Event, Proc: OlivOS.pluginAPI.shallow):
    """开始游戏

    Args:
        plugin_event (OlivOS.API.Event): 插件事件
        Proc (OlivOS.pluginAPI.shallow): 进程接口
    """
    global bet

    class Deck:
        def __init__(self):
            self.cards = self._generate_deck()

        def _generate_deck(self):
            cards = []
            for suit in suits:
                for rank in ranks:
                    card = f'{rank}{suit}'
                    cards.append(card)
            return cards

        def shuffle(self):
            random.shuffle(self.cards)

        def draw_card(self):
            if not self.cards:
                # raise ValueError('牌堆里没有剩余的牌了。')
                eventReply(plugin_event, '牌堆里没有剩余的牌了。')
                return
            return self.cards.pop()



    class Hand:
        def __init__(self):
            self.cards = []

        def add_card(self, card):
            self.cards.append(card)

        def get_value(self):
            for card in self.cards:
                if card[0] not in card_values:
                    if plugin_event.platform['platform'] == 'qq':
                        try:
                            msg_id = plugin_event.data.message_id # type: ignore
                        except:
                            pass
                    eventReply(plugin_event, f'未知卡牌: {card}')
            value = sum(card_values[card[0]] for card in self.cards)
            num_aces = len([card for card in self.cards if card[0] == 'A'])
            while value > 21 and num_aces > 0:
                value -= 10
                num_aces -= 1
            return value




    class Player:
        def __init__(self, name, chips):
            self.name = name
            self.chips = int(chips)
            self.hand = Hand()

        def bets(self):
            global bet
            OlivaDiceCore.msgReply.replyMsg(
                plugin_event, f'{self.name}, 您有 {self.chips} 个筹码。您想下注多少？\n推荐的赌注: ({self.chips/2} {self.chips/5} {self.chips/10})')
            while True:
                input: 'str|None' = OlivaDiceCore.msgReplyModel.replyCONTEXT_regWait(
                    plugin_event=plugin_event,
                    flagBlock='allowCommand',
                    hash=OlivaDiceCore.msgReplyModel.contextRegHash(
                        [None, plugin_event.data.user_id]) # type: ignore
                )
                flag_need_loop = False
                if plugin_event != None:
                    flag_need_loop = True
                    if input is None or not isinstance(input, str):
                        eventReply(plugin_event, '无效的输入。请您输入一个数字。')
                    else:
                        try:
                            input_num = float(input)
                            if input_num <= self.chips:
                                if input_num <= 0:
                                    OlivaDiceCore.msgReply.replyMsg(
                                        plugin_event, '您不能下注小于0的点数。')
                                else:
                                    bet = input_num
                                    flag_need_loop = False
                                    break
                            else:
                                OlivaDiceCore.msgReply.replyMsg(
                                    plugin_event, '您不能下注超过您拥有的筹码数量。')
                        except ValueError:
                            eventReply(plugin_event, '无效的输入。请您输入一个数字。')
            self.chips -= bet
            return bet

        def hit_or_stand(self):
            OlivaDiceCore.msgReply.replyMsg(
                plugin_event, '您想要继续要牌(hit)还是停止要牌(stand)？ ')
            while True:
                action: 'str|None' = OlivaDiceCore.msgReplyModel.replyCONTEXT_regWait(
                    plugin_event=plugin_event,
                    flagBlock='allowCommand',
                    hash=OlivaDiceCore.msgReplyModel.contextRegHash(
                        [None, plugin_event.data.user_id]) # type: ignore
                ).lower()
                flag_need_loop = False
                if plugin_event != None:
                    flag_need_loop = True
                    if action == 'hit':
                        return 'hit'
                    elif action == 'stand':
                        return 'stand'
                    else:
                        eventReply(
                            plugin_event, '无效的输入。请您输入"hit"或者"stand"。')




    class Dealer:
        def __init__(self):
            self.hand = Hand()

        def hit_or_stand(self):
            return 'hit' if self.hand.get_value() < 17 else 'stand'


    message = plugin_event.data.message # type: ignore
    if message.split()[0].lower().startswith(".blackjack") or message.split()[0].lower().startswith("。blackjack"):
        if len(message.split()) >= 2:
            if message.split()[1].lower() == "rule":
                plugin_event.reply(rule)
                return
        args = parser.parse_args(message.split()[1:])
        deck = Deck()
        player = Player(args.name, args.bet)
        dealer = Dealer()
        while True:
            eventReply(plugin_event, '新一轮。')

            # 玩家下注
            bet = player.bets()

            # 发牌
            deck.shuffle()
            for _ in range(2):
                player.hand.add_card(deck.draw_card())
                dealer.hand.add_card(deck.draw_card())

            # 玩家回合
            while True:
                plugin_event.reply(
                    f'{player.name}, 你的手牌: {", ".join(player.hand.cards)}\n点数: {player.hand.get_value()}')
                if player.hand.get_value() >= 21:
                    break
                action = player.hit_or_stand()
                if action == 'hit':
                    player.hand.add_card(deck.draw_card())
                else:
                    break

            # 庄家回合
            if player.hand.get_value() <= 21:
                while True:
                    time.sleep(random.random()*2)
                    plugin_event.reply(
                        f'庄家的手牌： {", ".join(dealer.hand.cards[:-1])}, *')
                    if dealer.hit_or_stand() == 'hit':
                        dealer.hand.add_card(deck.draw_card())
                    else:
                        break

            # 结算
            final = f'✨结算\n\n{player.name}的手牌: {", ".join(player.hand.cards)}\n玩家手牌点数总和: {player.hand.get_value()}\n\n庄家的手牌: {", ".join(dealer.hand.cards)}\n庄家手牌点数总和: {dealer.hand.get_value()}'

            if player.hand.get_value() > 21:
                plugin_event.reply(f'{final}\n\n你爆了。输了哦~')
            elif dealer.hand.get_value() > 21:
                plugin_event.reply(f'{final}\n\n庄家爆了，你赢了。')
                player.chips += bet * 2
            elif player.hand.get_value() > dealer.hand.get_value():
                plugin_event.reply(f'{final}\n\n你赢了！')
                player.chips += bet * 2
            elif player.hand.get_value() < dealer.hand.get_value():
                plugin_event.reply(f'{final}\n\n你输了。')
            else:
                plugin_event.reply(f'{final}\n\n平局！')
                player.chips += bet

            # 判断是否继续游戏
            plugin_event.reply(f'{player.name}, 您的筹码余额: {player.chips}\n你想要开始新的一局么？ (y/n) ')
            if player.chips <= 0:
                plugin_event.reply('您的筹码已经用完了。游戏结束。\n你想要开始新的一局么？ (y/n) ')
                break
            while True:
                flag_need_loop = False
                if plugin_event != None:
                    flag_need_loop = True
                    if flag_need_loop:
                        answer: 'str|None' = OlivaDiceCore.msgReplyModel.replyCONTEXT_regWait(
                                plugin_event=plugin_event,
                                flagBlock='allowCommand',
                            hash=OlivaDiceCore.msgReplyModel.contextRegHash(
                                [None, plugin_event.data.user_id]) # type: ignore
                        ).lower()
                        if answer == 'y':
                            player.hand = Hand()
                            dealer.hand = Hand()
                            break
                        elif answer == 'n':
                            plugin_event.reply('珍爱生命，远离赌博~3q!')
                            return
                        else:
                            eventReply(
                                plugin_event, '无效的输入，请输入 "y" 或者 "n"。')


def eventReply(plugin_event: OlivOS.API.Event, message: str, msgid: 'str|None' = None):
    if plugin_event.platform['platform'] == 'qq':
        try:
            msgid = plugin_event.data.message_id # type: ignore
        except:
            pass
    res = message
    if msg_id is None:
        res = f'[OP:reply,id={str(msgid)}]{message}'
    else:
        res = f'[OP:reply,id={str(msg_id)}]{message}'
    plugin_event.reply(res)
