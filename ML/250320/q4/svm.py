from sklearn import svm

def train_linear_model(x_mat, y_vec):
    
    # <ToDo>: scikit-learn을 활용해서 모델을 생성하고, x_mat, y_vec으로 모델을 학습시킵니다.
    # 슬랙변수 가중치 C는 10으로 설정합니다.
    model = svm.SVC(kernel='linear', C=10)
    trained_model = model.fit(x_mat, y_vec)
    
    return trained_model

def train_poly_model(x_mat, y_vec):
    
    # <ToDo>: scikit-learn을 활용해서 모델을 생성하고, x_mat, y_vec으로 모델을 학습시킵니다.
    # 슬랙변수 가중치 C는 10으로 설정합니다.
    model = svm.SVC(kernel='poly', C=10)
    trained_model = model.fit(x_mat, y_vec)
    
    return trained_model
    
def train_rbf_model(x_mat, y_vec):
    
    # <ToDo>: scikit-learn을 활용해서 모델을 생성하고, x_mat, y_vec으로 모델을 학습시킵니다.
    # 슬랙변수 가중치 C는 10으로 설정합니다.
    model = svm.SVC(kernel='rbf', C=10)
    trained_model = model.fit(x_mat, y_vec)
    
    return trained_model
    
def train_sig_model(x_mat, y_vec):
    
    # <ToDo>: scikit-learn을 활용해서 모델을 생성하고, x_mat, y_vec으로 모델을 학습시킵니다.
    # 슬랙변수 가중치 C는 10으로 설정합니다.
    model = svm.SVC(kernel='sigmoid', C=10)
    trained_model = model.fit(x_mat, y_vec)
    
    return trained_model

def evaluate_model(model, x_mat, y_vec):
    
    # <ToDo>: 검증용으로 주어진 데이터를 이용해서 모델의 성능을 평가합니다.
    mean_acc = model.score(x_mat, y_vec)
    
    return mean_acc