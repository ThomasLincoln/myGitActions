# test_greetings.py

import pytest
from main import hello, bye

def test_hello_prints_hi():
  """Teste se a função hello imprime "hi"."""
  assert hello() == "hi"

def test_bye_prints_bye():
  """Teste se a função bye imprime "bye"."""
  assert bye() == "bye"
