import preprocess
import svm
import graph_plot

def main():
    # 데이터를 불러옵니다.
    x_train, y_train, x_val, y_val = preprocess.load_data('/Users/kimdohyeon/건양대학교병원_바이오헬스/Biomedical_AI_Train/ML/250320/q3/data/iris.csv', independent_var = ['petal length', 'sepal length'], response_var = 'class_num' )
    
    # <ToDo>: svm.py 안의 함수를 사용해 SVM 모델을 불러오고 학습시킵니다.
    clf_svm = svm.train_model(x_train, y_train)
    
    print("Independent variable: {}".format("petal length" + ' and ' + 'sepal length'))
    
    # SVM 모델의 그래프를 그립니다.
    graph_plot.svm_model_plot(clf_svm, x_train, y_train, feature_name = ['petal length', 'sepal length'] )

    # <ToDo>: svm.py 안의 함수를 사용해, 학습된 모델의 성능을 정확도로써 측정합니다.
    mean_acc = svm.evaluate_model(clf_svm, x_val, y_val)
    print("Mean accuracy: {}%".format(mean_acc*100))
    
if __name__ == "__main__":
    main()