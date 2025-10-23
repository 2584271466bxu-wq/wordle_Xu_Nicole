from wordle_yx3010 import validate_guess, check_guess

def test_validate_guess():
    """ 
    Test the validate_guess function with various inputs.
    
    TODO: Students should implementthis test function with:
    - Valid guesses (correct length, lowercase, alphabetic)
    - Invalid guesses (wrong length, uppercase, non-alphabetic)
    - Edge cases (empty string, None, non-string inputs)
    """
    # TODO: Implement your test cases here
    # Arrange
    valid = 'crane'
    inval_long = 'cranes'
    inval_short = 'cry'
    inval_Upper = 'Crane'
    inval_nonalpha = 'cran3'
    edge_empty = ' '
    edge_none = None
    edge_nonstr = 12345

    # Act
    act_valid = validate_guess(valid)
    act_inval_long = validate_guess(inval_long)
    act_inval_short = validate_guess(inval_short)
    act_inval_Upper = validate_guess(inval_Upper)
    act_inval_nonalpha = validate_guess(inval_nonalpha)
    act_edge_empty = validate_guess(edge_empty)
    act_edge_none = validate_guess(edge_none)
    act_edge_nonstr = validate_guess(edge_nonstr)

    # Assert
    assert act_valid == True
    assert act_inval_long == False
    assert act_inval_short == False
    assert act_inval_Upper == False
    assert act_inval_nonalpha == False
    assert act_edge_empty == False
    assert act_edge_none == False
    assert act_edge_nonstr == False

def test_check_guess_basic():
    """
    Test basic check_guess functionality.
    
    TODO: Students should implement this test function with:
    - Perfect match (all green)
    - No matches (all gray)
    - Mixed results (green, yellow, gray combinations)
    - Edge cases (different lengths)
    
    Remember: Run check_guess() with different inputs first to see what it returns!
    """
    # TODO: Implement your test cases here
    # Arrange
    secret = 'crane'
    perfect = 'crane'
    no_mat = 'blimp'
    mixed = 'react'
    short = 'cat'
    long = 'cranes'

    # Act
    act_perf = check_guess(secret, perfect)
    act_no_mat = check_guess(secret, no_mat)
    act_mixed = check_guess(secret, mixed)
    act_short = check_guess(secret, short)
    act_long = check_guess(secret, long)

    # Assert
    assert act_perf == [('c', 'green'), ('r', 'green'), ('a', 'green'), ('n', 'green'), ('e', 'green')], 'Should be all green if perfect match'
    assert act_no_mat == [('b', 'gray'), ('l', 'gray'), ('i', 'gray'), ('m', 'gray'), ('p', 'gray')], 'Should be all grey if no match'
    assert act_mixed == [('r', 'yellow'), ('e', 'yellow'), ('a', 'green'), ('c', 'yellow'), ('t', 'gray')], 'Should return mixed result if partially correct'
    assert act_short == [], 'Should return nothing if short'
    assert act_long == [], 'Should return nothing if too long'
