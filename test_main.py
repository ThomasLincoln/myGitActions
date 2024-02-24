# test_greetings.py

import pytest
from main import hello, bye

def test_hello_prints_hi():
  """Teste se a função hello imprime "hi"."""
  with pytest.capture_output() as captured:
    hello()
  assert captured.out == "hi\n"

def test_bye_prints_bye():
  """Teste se a função bye imprime "bye"."""
  with pytest.capture_output() as captured:
    bye()
  assert captured.out == "bye\n"
