from flask import Flask,request,json
from clicks_manager import ClicksManager


AD_ID_PARAM = "ad_id"
app = Flask(__name__)

@app.route('/bidder',methods=['GET'])
def show_ad():
    ad_id = request.args.get(AD_ID_PARAM)
    serve_ad = False
    
    if ClicksManager.get_count(ad_id,"shows") < 50:
        serve_ad = True
    else:
        clicks_rate = ClicksManager.get_count(ad_id,"clicks") / ClicksManager.get_count(ad_id,"shows")
        if clicks_rate > 0.5:
            serve_ad = True

    if serve_ad:
        ClicksManager.increase_count(ad_id,"shows")

    response = {'content': serve_ad}
    return json.dumps(response)


@app.route('/click',methods=['GET'])
def user_clicked():
    ad_id = request.args.get(AD_ID_PARAM)
    ClicksManager.increase_count(ad_id,"clicks")
    response = {}
    return json.dumps(response)

if __name__ == '__main__':
    app.run()