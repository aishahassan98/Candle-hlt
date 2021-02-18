from candle import Candle

def test_str_returns_all_details():
    candle1 = Candle("Vanilla",25,"fragrance","Tall","burn_time","Height","Width","$100")
    x = candle1.__str__()
    assert x == ("Candle name: Vanilla, ID = 25 fragrance:fragrance Candle time:seconds burn_time: burn_time_minutes, Height: height, Width: width, Price: $100")

def test_new_candle_correct():
    candle1 = Candle("Vanilla",25,"fragrance","Tall","burn_time","Height","Width","$100")
    assert candle1.name == 25
    assert candle1.ID == "vanilla"
    assert candle1.Fragrance == "fragrance"