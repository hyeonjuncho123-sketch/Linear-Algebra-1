import numpy as np

np.set_printoptions(precision=4, suppress=True)

# 예제 7-1: 특성다항식과 고유값
print("=== 예제 7-1 ===")
A = np.array([[2, 3],
              [3, -6]])
print("poly(A) =", np.poly(A))          # MATLAB: poly(A)
print("eig(A)  =", np.real_if_close(np.linalg.eigvals(A)))  # MATLAB: eig(A)

# 예제 7-2: 고유값과 고유벡터 (2x2)
print("\n=== 예제 7-2 ===")
A = np.array([[3, 2],
              [3, -2]])
lamda, X = np.linalg.eig(A)
lamda, X = np.real_if_close(lamda), np.real_if_close(X)  # 허수부 0 제거             # MATLAB: [X, lamda] = eig(A)
print("X =\n", X)
print("lamda =\n", np.diag(lamda))       # MATLAB처럼 대각행렬로 출력

# 예제 7-3: 고유값과 고유벡터 (3x3)
print("\n=== 예제 7-3 ===")
A = np.array([[3, -1, -1],
              [-12, 0, 5],
              [4, -2, -1]])
lamda, X = np.linalg.eig(A)
lamda, X = np.real_if_close(lamda), np.real_if_close(X)  # 허수부 0 제거
print("X =\n", X)
print("lamda =\n", np.diag(lamda))

# 예제 7-4: 삼각행렬의 고유값 = 주대각선 원소
print("\n=== 예제 7-4 ===")
A = np.array([[0, 0, 0],
              [0, 2, 5],
              [0, 0, -1]])
print("(1) eig(A) =", np.real_if_close(np.linalg.eigvals(A)))

B = np.array([[4, 0, 0],
              [0, 0, 0],
              [1, 0, -3]])
print("(2) eig(B) =", np.real_if_close(np.linalg.eigvals(B)))
