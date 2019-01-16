#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------
# Реализуйте функцию best_hand, которая принимает на вход
# покерную "руку" (hand) из 7ми карт и возвращает лучшую
# (относительно значения, возвращаемого hand_rank)
# "руку" из 5ти карт. У каждой карты есть масть(suit) и
# ранг(rank)
# Масти: трефы(clubs, C), пики(spades, S), червы(hearts, H), бубны(diamonds, D)
# Ранги: 2, 3, 4, 5, 6, 7, 8, 9, 10 (ten, T), валет (jack, J), дама (queen, Q), король (king, K), туз (ace, A)
# Например: AS - туз пик (ace of spades), TH - дестяка черв (ten of hearts), 3C - тройка треф (three of clubs)

# Задание со *
# Реализуйте функцию best_wild_hand, которая принимает на вход
# покерную "руку" (hand) из 7ми карт и возвращает лучшую
# (относительно значения, возвращаемого hand_rank)
# "руку" из 5ти карт. Кроме прочего в данном варианте "рука"
# может включать джокера. Джокеры могут заменить карту любой
# масти и ранга того же цвета, в колоде два джокерва.
# Черный джокер '?B' может быть использован в качестве треф
# или пик любого ранга, красный джокер '?R' - в качестве черв и бубен
# любого ранга.

# Одна функция уже реализована, сигнатуры и описания других даны.
# Вам наверняка пригодится itertools.
# Можно свободно определять свои функции и т.п.
# -----------------

from itertools import chain, combinations, product


def hand_rank(hand):
    """Возвращает значение определяющее ранг 'руки'"""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def card_ranks(hand):
    """Возвращает список рангов (его числовой эквивалент),
    отсортированный от большего к меньшему"""
    ranks_symbols = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
    ranks_numbers = range(2, 15)
    ranks_in_hand = [ranks_numbers[ranks_symbols.index(rank)] for rank, suit in hand] 
    return sorted(ranks_in_hand, reverse=True)


def flush(hand):
    """Возвращает True, если все карты одной масти"""
    suits = [suit for rank, suit in hand]
    return len(set(suits)) == 1


def straight(ranks):
    """Возвращает True, если отсортированные ранги формируют последовательность 5ти,
    где у 5ти карт ранги идут по порядку (стрит)"""
    return ranks == list(range(ranks[0], ranks[0]-len(ranks), -1))


def kind(n, ranks):
    """Возвращает первый ранг, который n раз встречается в данной руке.
    Возвращает None, если ничего не найдено"""
    n_times_ranks = [rank for rank in ranks if ranks.count(rank) == n]
    return n_times_ranks[0] if any(n_times_ranks) else None


def two_pair(ranks):
    """Если есть две пары, то возвращает два соответствующих ранга,
    иначе возвращает None"""
    two_pair_ranks = [rank for rank in set(ranks) if ranks.count(rank) >= 2]
    
    return sorted(two_pair_ranks, reverse=True) if len(two_pair_ranks) >= 2 else None


def best_hand(hand):
    """Из "руки" в 7 карт возвращает лучшую "руку" в 5 карт """
    all_hands = combinations(hand, 5)
    max_rate = (0,)
    for some_hand in all_hands:
        if hand_rank(some_hand) > max_rate:
            current_best_hand = some_hand
            max_rate = hand_rank(some_hand)

    return current_best_hand


def best_wild_hand(hand):
    """best_hand но с джокерами"""
    ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
    black_suits, red_suits = ('C', 'S'), ('H', 'D')
    black_cards = [''.join(card) for card in product(ranks, black_suits) if ''.join(card) not in hand]
    red_cards = [''.join(card) for card in product(ranks, red_suits) if ''.join(card) not in hand]
    jokers_in_hand = [card for card in hand if card[0] == '?']

    if len(jokers_in_hand) > 0:
        jokerless_hand = tuple(card for card in hand if card[0] != '?')
        first_joker = black_cards if '?B' in jokers_in_hand else red_cards
        second_joker = red_cards if '?R' in jokers_in_hand else black_cards

        joker_combinations = product(first_joker) if first_joker == second_joker else product(first_joker, second_joker)
        all_hands = map(lambda x: x + jokerless_hand, joker_combinations)
        all_best_hands = (best_hand(x) for x in all_hands)

        max_rate = (0,)
        for some_hand in all_best_hands:
            if hand_rank(some_hand) > max_rate:
                current_best_hand = some_hand
                max_rate = hand_rank(some_hand)

        return current_best_hand

    else:
        return best_hand(hand)


def test_best_hand():
    print("test_best_hand...")
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    print('OK')


def test_best_wild_hand():
    print("test_best_wild_hand...")
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    print('OK')

if __name__ == '__main__':
    test_best_hand()
    test_best_wild_hand()