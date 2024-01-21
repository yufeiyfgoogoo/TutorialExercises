
def age_to_vote(age):
    """input a number of age and if the age is greater than 18, then can vote"""
    if age >= 18:
        return True
    else:
        return False

def retirement(age):
    """input a number of age, if the age is small than 65, then get the number until retirement."""
    if age <= 65:
        return 65 - age
    else:
        return False

