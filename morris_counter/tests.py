#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for MorrisCounter"""
import morris_counter
import unittest


class TestMorrisCounter(unittest.TestCase):
    def setUp(self):
        self.mc = morris_counter.MorrisCounter()
        self.counter = 0
        self.counter2 = 1

    def test_basics(self):
        self.assertEqual(self.mc.exponents[self.counter], 0)
        self.assertEqual(self.mc.get(self.counter), 1)

    def test_add(self):
        self.mc.add(self.counter)
        self.assertEqual(self.mc.get(self.counter), 2)

        self.mc.add(self.counter)
        self.assertTrue(self.mc.get(self.counter) >= 2)

        # this should *normally* pass but we can't guarantee
        # that 10 increments will cause the exponent to
        # tick up past 1
        for n in range(10):
            self.mc.add(self.counter)
        self.assertTrue(self.mc.get(self.counter) >= 4)

        self.assertEqual(len(self.mc), 1)

    def test_add_counter(self):
        self.assertEqual(len(self.mc), 1)
        self.mc.add_counter()
        self.assertEqual(len(self.mc), 2)

        self.mc.add(self.counter2)
        self.assertEqual(self.mc.get(self.counter2), 2)
