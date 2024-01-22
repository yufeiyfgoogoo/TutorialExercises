from vote_retirement import age_to_vote
from vote_retirement import retirement

def test_age_to_vote():
    assert age_to_vote(18) == True

def test_retirement():
    assert retirement(30) == 35


