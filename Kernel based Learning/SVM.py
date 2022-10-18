import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
plt.style.use('ggplot')


class SVM:
    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        self.lr = learning_rate # 학습률 정의
        self.lambda_param = lambda_param 
        self.n_iters = n_iters
        self.w = None
        self.b = None

    def fit(self, X, y):
        y_ = np.where(y <= 0, -1, 1) # y는 -1과 1 사이의 값만 가질 수 있음 (condition 부여)
        n_samples, n_features = X.shape

        self.w = np.zeros(n_features) # 변수 개수만큼의 weight가 존재
        self.b = 0

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                # 데이터와 초평면 사이의 여백을 최대화하고자 하고, 마진 최대화에 사용되는 손실함수는 hinge loss
                condition = y_[idx] * (np.dot(x_i, self.w) - self.b) >= 1 # 예측값과 실제값이 같은 부호라면 cost=0
                if condition:
                    self.w -= self.lr * (2 * self.lambda_param * self.w)
                else:
                    self.w -= self.lr * (
                        2 * self.lambda_param * self.w - np.dot(x_i, y_[idx])
                    )
                    self.b -= self.lr * y_[idx]

    def predict(self, X):
        linear_output = np.dot(X, self.w) - self.b # linear 모델에 new_x를 넣은 후에 sign 함수를 통해 분류
        return np.sign(linear_output)


"""테스트"""
if __name__ == "__main__":
    # Imports


    X, y = x, y = datasets.make_blobs(n_samples=100, centers=2, random_state=2022, cluster_std=0.8) # 깔끔한 분리를 위해 cluster별 표준편차를 작게 설정
    y = np.where(y == 0, -1, 1)

    clf = SVM()
    clf.fit(X, y)
    # predictions = clf.predict(X)

    print(clf.w, clf.b)

    def visualize_svm():
        def get_hyperplane_value(x, w, b, offset):
            return (-w[0] * x + b + offset) / w[1]

        fig = plt.figure(figsize = (7,7))
        ax = fig.add_subplot(1, 1, 1)
        plt.scatter(X[:, 0], X[:, 1], marker="o", c=y, s=200, cmap='Set2')

        x0_1 = np.amin(X[:, 0])
        x0_2 = np.amax(X[:, 0])

        x1_1 = get_hyperplane_value(x0_1, clf.w, clf.b, 0)
        x1_2 = get_hyperplane_value(x0_2, clf.w, clf.b, 0)

        x1_1_m = get_hyperplane_value(x0_1, clf.w, clf.b, -1)
        x1_2_m = get_hyperplane_value(x0_2, clf.w, clf.b, -1)

        x1_1_p = get_hyperplane_value(x0_1, clf.w, clf.b, 1)
        x1_2_p = get_hyperplane_value(x0_2, clf.w, clf.b, 1)

        ax.plot([x0_1, x0_2], [x1_1, x1_2], "k", linewidth=4)
        ax.plot([x0_1, x0_2], [x1_1_m, x1_2_m], "k--", linewidth=5)
        ax.plot([x0_1, x0_2], [x1_1_p, x1_2_p], "k--", linewidth=5)

        x1_min = np.amin(X[:, 1])
        x1_max = np.amax(X[:, 1])
        ax.set_ylim([x1_min - 3, x1_max + 3])

        plt.show()

    visualize_svm()