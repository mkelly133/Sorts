import pytest
import helpers as h

def test_ultimate_answer():
    question1 = 'What is the meaning of Life, The Universe, Everything?'
    assert h.ultimate_answer(question1) == '42'
    question2 = 'What is 6 x 7'
    assert h.ultimate_answer(question2) == 'That is not much of a question'
