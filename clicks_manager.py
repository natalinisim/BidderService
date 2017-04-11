class ClicksManager:
	#clicks_counter its a dictionary that will look like : {"1" : {"clicks": 43, "shows":60},"2" : {"clicks": 22, "shows":31 }}
    clicks_counter = {}
    @staticmethod
    def increase_count(ad_id,prop):
		if not ClicksManager.clicks_counter.has_key(ad_id):
			ClicksManager.clicks_counter[ad_id]={}
			ClicksManager.clicks_counter[ad_id][prop] = 1
		if not ClicksManager.clicks_counter[ad_id].has_key(prop):
			ClicksManager.clicks_counter[ad_id][prop] = 1
		ClicksManager.clicks_counter[ad_id][prop]+=1

    @staticmethod
    def get_count(ad_id,prop):
		if not ClicksManager.clicks_counter.has_key(ad_id):
			ClicksManager.clicks_counter[ad_id] = {}
			ClicksManager.clicks_counter[ad_id][prop] = 0
		if not ClicksManager.clicks_counter[ad_id].has_key(prop):
			ClicksManager.clicks_counter[ad_id][prop] = 0
		return ClicksManager.clicks_counter[ad_id][prop]	

