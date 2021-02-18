class Catalogue:
    def __init__(self,cat_name):
        self.cat_name = cat_name
        self.candle_list = []
        
        
    def list_all_candles(self,name):
        return self.candle_list
            
    def add_candle(self,new_candle):
        self.candle_list.append(new_candle)
        return self.candle_list
            
    def delete_candle(self, ID):
        for candle in self.candle_list:
            if id == candle.id:
                self.candle_list.remove(candle)
                
    def update_candle_price(self,ID,new_price):
        for candle in self.candle_list:
            if id == candle.ID:
                candle.price = new_price