import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

def Visualize(x_data, y_data, predictions):
    # 데이터 출력
    plt.scatter(x_data,y_data)
    plt.savefig('data.png')
    plt.show()

    # 곡선형 분포 데이터와 예측값 출력
    plt.scatter(x_data,predictions, color='red')
    plt.savefig('prediction.png')
    plt.show()
