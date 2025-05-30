from flask import Flask, jsonify, request
import tensorflow as tf

app = Flask(__name__)

import PIL.Image as image

def work(img, model): # 이미지를 입력하면 숫자를 출력하는 함수
    pred = model.predict(img) # TODO: 모델에 이미지를 넣고 결과를 pred에 저장
    pred = pred[0] # TODO: batch 단위로 나온 결과에서 이미지 하나의 결과를 추출
    idx = tf.math.argmax(pred)  # TODO: 결과중 가장 확률이 높은 index 가져오기
    return idx

@app.route("/", methods=["GET"]) # @app.route를 작성하고, GET Method만 사용합니다.
def predict():    
    imgurl = request.args.get("img")       # img라는 이름으로 url을 받아옴
    result_string="please input image url"
    if imgurl != None:                     # imgurl을 제대로 받은 경우
        imgurl=imgurl.split("?")[0]
        img = image.open("img/"+imgurl)        # 전달받은 url의 이미지 로드  
        img=tf.keras.utils.img_to_array(img)   # 이미지를 행렬로 변환
        img=tf.expand_dims(img, axis=0)        # batch를 위해 한 차원 높게 변환   
        idx = work(img, model)   # 모델을 work 함수를 통해 사용합니다.    
        result_string = "This number is %d"%(idx)   #사용자에게 보여줄 문자열
    return jsonify(result_string)


# Flask 서버를 실행하는 코드입니다.
if __name__ == "__main__":
    from keras.layers import TFSMLayer
    from keras import Sequential, Input

    model = Sequential([
        Input(shape=(28, 28, 1)),  # 입력 형태는 모델에 맞게 조정 필요
        TFSMLayer('/Users/kimdohyeon/건양대학교병원_바이오헬스/Biomedical_AI_Train/DL/250423/q5/mymodel', call_endpoint='serving_default')
    ])
    app.run(host="0.0.0.0", port=8080) # flask 서비스 시작