import function.calc as fc

def test_negatives():
    assert fc.adivb(-10, -5) == 2, "Two negative should return a positive"


# assert adivb(-9, 3) == -3, "One positive, one negative should return a negative"
# assert adivb(35,7) > 0, "Two positive should be positive"
# assert isinstance(adivb(5,10), float), "minor by larger should be float"
# assert adivb(5,2) == 2.5, "5/2 should be 2.5"
# assert adivb(10,3) == pytest.approx(3.33, 0.01), "10/3 should be 3.333"