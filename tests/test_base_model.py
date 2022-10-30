#!/usr/bin/env python3
# Unittesting BaseModel

from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """This class contains unit tests for the
       modules contained in base_model
       Inherits from the TestCase module in
       the unittest module
    """
    def test_id(self):
      """Checks whether or not the BaseModel id attribute is a str"""
      t_id = BaseModel()
      self.assertIsInstance(t_id.id, str)

    def test_created_at(self):
      """Checks whether or not the BaseModel created_at attribute
         is a datetime object
      """
      t_created_at = BaseModel()
      self.assertIsInstance(t_created_at, datetime)

    def test_updated_at(self):
      """Checks whether or not the BaseModel updated_at attribute
         is a datetime object
      """
      t_updated_at = BaseModel()
      self.assertIsInstance(t_updated_at, datetime)

    def test_to_dict(self):
      """Checks whether the to_dict method returns a dictionary"""
      t_to_dict = BaseModel()
      ret_to_dict = t_to_dict.to_dict()
      self.assertIsInstance(ret_to_dict, dict)

if __name__ == "__main__":
   unittest.main()

