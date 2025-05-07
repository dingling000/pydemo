import os

from flask import Flask, request, jsonify
from access import accessToken

def create_app():
    app = Flask(__name__)

    #简单的测试接口，返回200和hello信息。接口
    @app.route("/hello", methods=["GET"])
    def hello():
        a = 1 / 1
        ret = jsonify({'statusCode': 200, 'msg': 'hello'})

        return ret

    #调用百度翻译接口。
    @app.route("/text", methods=["POST"])
    def textTranslate():
        import requests
        #请求百度翻译接口，传入 token
        url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + accessToken
        
        q = request.get_json()['text'] #参数：翻译的文本
        from_lang = request.get_json()['from']#参数：原语言
        to_lang = request.get_json()['to']#参数：译语言
        term_ids = ''
        # 建立请求
        headers = {'Content-Type': 'application/json'}
        payload = {'q': q, 'from': from_lang, 'to': to_lang, 'termIds' : term_ids}
        # 发起请求
        r = requests.post(url, params=payload, headers=headers)
        try:
            result = r.json()['result']['trans_result'][0]['dst']
            ret = jsonify({'statusCode': 200, 'msg': 'successful', 'result': result})
        except:
            #出错时捕捉错误
            msg = r.json()['error_msg']
            ret = jsonify({'statusCode': -1, 'msg': msg})

        return ret

    #调用百度图片识别并翻译接口
    @app.route("/image", methods=["POST"])
    def imageTranslate():
        import requests
        #请求百度接口，传入token
        url = 'https://aip.baidubce.com/file/2.0/mt/pictrans/v1?access_token=' + accessToken
        
        file = request.files['image'] #参数：上传的图片
        from_lang = request.form['from']#参数：原语言
        to_lang = request.form['to']#参数：译语言
        
        payload = {'from': from_lang, 'to': to_lang, 'v': '3', 'paste': '0'}
        image = {'image': (file.filename, file.stream, "multipart/form-data")}
        
        r = requests.post(url, params = payload, files = image)
        try:
            contents = r.json()['data']['content']
            paras = ''
            # 提取翻译结果文本并合并为一个字符串返回
            for c in contents:
                paras = paras + c['dst'] + '\n'
            ret = jsonify({'statusCode': 200, 'msg': 'successful', 'result': paras})
        except:
            msg = r.json()['error_msg']
            ret = jsonify({'statusCode': -1, 'msg': msg})

        return ret
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()