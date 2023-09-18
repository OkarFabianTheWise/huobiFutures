from utils import http_get_request, api_key_post

class HuobiDM:

    def __init__(self,url,access_key,secret_key):
        self.__url = url
        self.__access_key = access_key
        self.__secret_key = secret_key

    def swap_contract_info(self, contract_code):
        """
        :contract_code    "BTC-USDT","ETH-USDT"...
        """
        
        params = {'contract_code': contract_code,
                  'pair': contract_code}
    
        url = self.__url + '/linear-swap-api/v1/swap_contract_info'
        return http_get_request(url, params)

    def linear_swap_order(self,
                        contract_code,
                        volume, 
                        direction,
                        offset,
                        lever_rate, 
                        tp_trigger_price,
                        sl_trigger_price):
        """
        :contract_code: "BTC-USDT","ETH-USDT"..
        :contract_type: "this_week", "next_week", "quarter"
        :volume            必填  委托数量（张）
        :direction         必填  "buy" "sell"
        :offset            必填   "open", "close"
        :lever_rate        必填  杠杆倍数
        :order_price_type  必填   "limit"限价， "opponent" 对手价
        备注：如果contract_code填了值，那就按照contract_code去下单，如果contract_code没有填值，则按照symbol+contract_type去下单。
        :
        """
        
        params = {
            "contract_code": contract_code,
            "volume": volume,
            "direction": direction,
            "offset": offset,
            "lever_rate": lever_rate,
            "order_price_type": "market",
            "tp_trigger_price": tp_trigger_price,
            "tp_order_price": tp_trigger_price,
            "sl_trigger_price": sl_trigger_price,
            "sl_order_price": sl_trigger_price,
            }
        
        
        request_path = '/linear-swap-api/v1/swap_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    
    def linear_closing(self,
                       contract_code,
                       volume,
                       offset,
                       lever_rate):
        
        params = {
            "contract_code": contract_code,
            "volume": volume,
            "direction": "sell",
            "offset": offset,
            "lever_rate": lever_rate,
            "order_price_type": "market",
            }
        
        
        request_path = '/linear-swap-api/v1/swap_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    def linear_short_order(self,
                        contract_code,
                        volume, 
                        direction,
                        offset,
                        lever_rate, 
                        tp_trigger_price,
                        sl_trigger_price):
        """
        :contract_code: "BTC-USDT","ETH-USDT"..
        :contract_type: "this_week", "next_week", "quarter"
        :volume              amount
        :direction           "buy" "sell"
        :offset               "open", "close"
        :lever_rate        
        :order_price_type  必填   "limit"限价， "opponent" 对手价
        备注：如果contract_code填了值，那就按照contract_code去下单，如果contract_code没有填值，则按照symbol+contract_type去下单。
        :
        """
        
        params = {
            "contract_code": contract_code,
            "volume": volume,
            "direction": direction,
            "offset": offset,
            "lever_rate": lever_rate,
            "order_price_type": "market",
            "tp_trigger_price": tp_trigger_price,
            "tp_order_price": tp_trigger_price,
            "sl_trigger_price": sl_trigger_price,
            "sl_order_price": sl_trigger_price,
            }
        
        
        request_path = '/linear-swap-api/v1/swap_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    
    def linear_closing(self,
                       contract_code,
                       volume,
                       direction,
                       offset,
                       lever_rate):
        
        params = {
            "contract_code": contract_code,
            "volume": volume,
            "direction": direction,
            "offset": offset,
            "lever_rate": lever_rate,
            "order_price_type": "market",
            }
        
        
        request_path = '/linear-swap-api/v1/swap_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    def swap_order_info(self,
                       contract_code,
                       order_id):
        
        params = {
            "contract_code": contract_code,
            "order_id": order_id,
            }
        
        
        request_path = '/linear-swap-api/v1/swap_order_detail'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
