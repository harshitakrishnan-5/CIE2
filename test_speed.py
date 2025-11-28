from speed import calculate_speed

def test_calculate_speed():
    assert calculate_speed(100, 2) == 50
    assert calculate_speed(150, 3) == 50
    assert calculate_speed(60, 1) == 60

