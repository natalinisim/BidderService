'''
If bidder returns {"should_server": True} client pays 50 cents for showing the ad.
If client called click, then it earned 1 dollar.
Each ad has probability to be clicked, one worth the serving money but one does not

Tested with python 2.7 and requests libraries installed 
'''

import random 
import requests


USERS_NUM = 100

AD_TO_PROBABILITY = {1: 0.9, 2: 0.1} 
AD_TO_EXPECTED_MONEY = {1: 100 * (-0.5 + 0.8 * 1.0), 2: 50 * (-0.5 + 0 * 1.0)}

class BidderClient():
    def run(self):
        
        # in dollars
        money = 0.0
        
        for ad_id, click_probability in AD_TO_PROBABILITY.items():
            for _ in range(0, USERS_NUM):
                payload = {"ad_id": ad_id} 
            
                serving_response = requests.get("http://localhost:5000/bidder", params=payload)
                
                should_serve = serving_response.content
                
                if should_serve:
                    money -= 0.5
                    click = random.uniform(0, 1) < click_probability
                    if click:
                        requests.get("http://localhost:5000/click", params=payload)
                        money += 1.0
                
            print("ad: {}, expected: {}, money: {}".format(ad_id, AD_TO_EXPECTED_MONEY[ad_id], money))
            assert money > AD_TO_EXPECTED_MONEY[ad_id]
        print "test success"
        
if __name__ == "__main__":
    BidderClient().run()
