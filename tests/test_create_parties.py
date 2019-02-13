from flask import Flask, Blueprint
from flask_restful import Resource, reqparse

import pytest
import unittest

parties=[]

class TestCreateParties(unittest.TestCase):

    def test_create_party(self):
        parties = self.parties.save()
        self.assertEqual(1, len("parties") + 1)
        self.assertTrue(isinstance(parties, dict))

    def test_delete_party(self):
        self.parties.save()
        self.assertEqual(1, len("parties") + 1)
        parties = Party.get(id=1)
        parties.delete()
        self.assertEqual(0, len("parties") + 1)

    def test_can_update_party(self):
        data = {
            'name': 'newusername',
            'hqaddress': 'New Location',
            'logoUrl': 'nhnhnh.co.ke'}
        self.parties.save()
        parties = Party.get(id=1)
        parties = parties.update(data=data)
        self.assertEqual(data['name'], user['name'])
        self.assertEqual(data['hqaddress'], user['HQ address'])
        self.assertEqual(data['logoUrl'], user['nnnn.co.ke'])

    def test_get_party(self):
        self.parties.save()
        parties = Party.get(id=1)
        self.assertIsInstance(parties, Party)
        keys = sorted(list(parties.view().keys()))
        self.assertListEqual(keys, sorted(['name', 'hq address', 'logoUrl']))

    def test_can_get_one_entry(self):
        self.parties.save()
        self.entry1.save()
        entry = Entry.get(id=1, user_id=1)
        self.assertIsInstance(entry, Entry)
        keys = sorted(list(entry.view().keys()))
        self.assertListEqual(
            keys, sorted(['name', 'hq address', 'logoUrl']))
