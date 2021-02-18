from candle import Candle 
from Catalogue import Catalogue

def test_new_catalogue_current():
    cat = Catalogue("2021 Catalogue")
    assert cat.cat_name =="2021 Catalogue"
    assert cat.candle_list == []

def test_list_all_candles_empty_for_new_cat():
    cat = Catalogue("2021 Catalogue")
    list_candles = cat.list_all_candles("Candle list")
    assert list_candles == []

#final test to be added when new candles method has been added
def test_add_candle_puts_candle_in_list():
    cat = Catalogue("2021 Catalogue")
    candle1 = Candle("beach","name",54 ,"Fragrance", "Candle_Type","Burn_Time","height","side","price")
    cat.add_candle(candle1)
    assert cat.candle_list == [candle1]