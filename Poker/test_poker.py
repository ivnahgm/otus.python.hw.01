#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
import poker


class TestCardRanks(unittest.TestCase):

    hand1 = ['6C', '7C', '8C', '9C', 'TC']
    hand2 = ['8C', '8S', 'TC', 'TD', 'TH']
    hand3 = ['7C', '7D', '7H', '7S', 'JD']

    def test_card_ranks_hands1(self):
        self.assertEqual(poker.card_ranks(self.hand1), [10, 9, 8, 7, 6],'Should be list: [10, 9, 8, 7, 6]')

    def test_card_ranks_hands2(self):
        self.assertEqual(poker.card_ranks(self.hand2), [10, 10, 10, 8, 8],'Should be list: [10, 10, 10, 8, 8]')

    def test_card_ranks_hands3(self):
        self.assertEqual(poker.card_ranks(self.hand3), [11, 7, 7, 7, 7],'Should be list: [11, 7, 7, 7, 7]')


class TestFlush(unittest.TestCase):

    hand1 = ['6C', '7C', '8C', '9C', 'TC']
    hand2 = ['8C', '8S', 'TC', 'TD', 'TH']
    hand3 = ['7C', '7C', '7C', '7C', 'JC']

    def test_flush_hand1(self):
        self.assertEqual(poker.flush(self.hand1), True, 'Should be True')

    def test_flush_hand2(self):
        self.assertEqual(poker.flush(self.hand2), False, 'Should be False')
        
    def test_flush_hand3(self):
        self.assertEqual(poker.flush(self.hand3), True, 'Should be True')


class TestStraight(unittest.TestCase):

    rank1 = [10, 9, 8, 7, 6]
    rank2 = [10, 10, 10, 8, 8]
    rank3 = [11, 7, 7, 7, 7]

    def test_straight_rank1(self):
        self.assertEqual(poker.straight(self.rank1), True, 'Should be True')

    def test_straight_rank2(self):
        self.assertEqual(poker.straight(self.rank2), False, 'Should be False')

    def test_straight_rank3(self):
        self.assertEqual(poker.straight(self.rank3), False, 'Should be False')


class TestKind(unittest.TestCase):
    rank1 = [10, 9, 8, 7, 6]
    rank2 = [10, 10, 10, 8, 8]
    rank3 = [11, 7, 7, 7, 7]

    def test_kind_rank1(self):
        self.assertEqual(poker.kind(2, self.rank1), None, 'Should be None')

    def test_kind_rank2(self):
        self.assertEqual(poker.kind(3, self.rank2), 10, 'Should be 10')

    def test_kind_rank3(self):
        self.assertEqual(poker.kind(4, self.rank3), 7, 'Should be 7')


class TestTwoPair(unittest.TestCase):
    rank1 = [10, 9, 8, 7, 6]
    rank2 = [10, 10, 10, 8, 8]
    rank3 = [11, 7, 7, 7, 7]

    def test_two_pair_rank1(self):
        self.assertEqual(poker.two_pair(self.rank1), None, 'Should be None')

    def test_two_pair_rank2(self):
        self.assertEqual(poker.two_pair(self.rank2), [10, 8], 'Should be [10, 8]')

    def test_two_pair_rank3(self):
        self.assertEqual(poker.two_pair(self.rank3), None, 'Should be None')


if __name__ == '__main__':
    unittest.main()