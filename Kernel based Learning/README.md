# :books: Kernel based Learning - Support Vector Machine
`커널 기반 학습(kernel based learning)`은 딥러닝이 대두되기 전인 2000년대 초반까지 머신러닝 모델 (SVM, SVR 등)의 기반이 되는 학습 방법이다. 커널 기반의 방법론들은 `구조적 위험 최소화(Structure Rist Minimization, SRM)`를 중요하게 생각한다. 우리는 모델을 만들 때 존재하는 모든 데이터를 알지 못하기에 `사용이 가능한 데이터(학습 데이터)에 최적화된 (경험적 위험만을 최소화하는) 모델을 생성한다.` 그러나 이렇게 사용한 학습 데이터가 전체 데이터를 완벽하게 대체할 수는 없기에 데이터에 대한 일반화로부터 발생하는 오류를 계산해야 한다. 이는 모델의 구조로부터 발생하는 위험을 최소화 해야 하는 것을 의미한다.

 모델의 복잡도(VC dimension)가 증가하면 (모델의 복잡도를 나타내는 지표인) capacity에 의한 오차, 즉 일반화로부터 발생되는 오차(variance)가 증가한다. 반면에 학습 데이터에는 잘 맞춰지기에 training error(bias)는 줄어든다. 따라서 `구조적 위험 최소화 접근법은 '모델의 복잡도'와 '학습 데이터의 오차(경험적 위험)'의 트레이드 오프를 고려하여 최선의 모델을 선택하는 것을 의미한다.`
 </br></br>

## 1. Support Vector Machine (SVM)이란?
- SVM은 고차원 데이터 세트의 분류에 대해 `우수한 일반화(generalization) 성능을 달성할 수 있다.`
- SVM은 구조상으로 선형 분류기에 속하며 고차원 기능 공간에 데이터를 매핑하여 작동하기에 `선형으로 분리될 수 없는 데이터셋에 대해서도 선형 분류가 가능하다.`

    ![](2022-10-18-17-59-58.png)
</br></br>

---
## 2. SVM 특징
1. 장점과 단점</br></br>
    1-1. SVM의 장점 :smiley:
    - SVM은 다양한 유형의 데이터(이미지, 텍스트 등)에 적용이 가능하기에 `데이터를 잘 모르는 경우 유용하다.`
    - SVM은 `일반적으로 과적합 조건을 잘 겪지 않으며` 클래스 간 분리가 명확하게 표시될 때 잘 수행된다.
    - SVM은 분리된 초평면을 찾는데 유리하며, 초평면을 찾는 것은 서로 다른 그룹 간에 데이터를 올바르게 분류하는 데 유용할 수 있다. 이러한 `초평면은 데이터의 클러스터링 또는 이상값 감지에도 사용할 수 있다.`</br></br>

    1-2. SVM의 단점 :disappointed_relieved:
    - 훈련 시간이 매우 길기에 `대규모 데이터셋에 적합하지 않다.` 특히 훈련 데이터의 관측치에 비해 feature의 수가 매우 많으면 효율적이지 않다.
    - `불균형이 매우 심한 데이터셋에 대해서는 잘 수행되지 않는다.` (이러한 경우에는 로지스틱 회귀가 더 좋을 수 있다.)
    - 서로 충돌하는 클래스가 존재하는 데이터셋에 대해서는 제대로 작동하지 않으며 `사용되는 커널 유형에도 민감하다.`
    - 여러 개의 클래스가 존재하는 경우 좋은 선택이 아니다. 
</br></br>


2. 다른 알고리즘과의 차이점 :open_mouth:
- 일반적으로 모든 분류기(모델)는 훈련 데이터에 대한 분류 성능을 최대화하려고 한다.
- 그러나 분류기가 train data에 너무 적합하면 `새로운 데이터 (unknown data)에 대한 분류 능력(generalizaion ability)이 저하된다.`
- 일반화 능력과 훈련 데이터에 대한 적합성 사이에는 절충점이 존재한다.
- SVM은 통계적 학습 이론을 기반으로 분류 경계면의 일반화 능력이 최대화하도록 훈련된다. 따라서 `SVM은 training error에 대한 성능을 높이면 testing error에 대한 성능도 동시에 높아진다.`
</br></br>
---
## 3. Kernel based Learning tutorial
- Support Vector Machine (SVM)  [[tutorial](https://github.com/rch1025/Business-Analytics/blob/main/Dimensionality%20Reduction/LDA%20tutorial.ipynb)]


---
### :postbox: Reference
1.  Boser, B. E., Guyon, I. M., & Vapnik, V. N. (1992, July). A training algorithm for optimal margin classifiers. In Proceedings of the fifth annual workshop on Computational learning theory (pp. 144-152).
2. Vapnik, V. (1999). The nature of statistical learning theory. Springer science & business media.
3. https://medium.com/codex/support-vector-machine-with-python-in-just-100-lines-of-code-35e74707f8e1
4. https://www.youtube.com/watch?v=gzbafL28vA0&t=1680s (강필성 교수님의 Business Analytics IME654 강의)
5. 