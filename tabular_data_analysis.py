import pandas as pd
import numpy as np


df = pd.read_csv('advertising.csv')
data = df.to_numpy()
# print(df.head)

'''Câu hỏi 15: Lấy giá trị lớn nhất và chỉ mục tương ứng của nó trên cột Sales:'''
print(f'Max: {data[:, 3].max()} - Index: {np.where(data[:, 3] == data[:, 3].max())[0][0]}')

'''Câu hỏi 16: Giá trị trung bình của cột TV là:'''
print(round(data[:, 0].mean(), 1))

'''Câu hỏi 17: Số lượng bản ghi có giá trị tại cột Sales lớn hơn hoặc bằng 20 là:'''
print(len(np.where(data[:, 3] >= 20)[0]))

'''Câu hỏi 18: Tính giá trị trung bình của cột Radio thoả mãn điều kiện giá trị tương ứng
trên cột Sales lớn hơn hoặc bằng 15:'''
print(round(data[:, 1][np.where(data[:, 3] >= 15)[0]].mean(), 1))

'''Câu hỏi 19: Tính tổng các hàng của cột Sales với điều kiện giá trị Newspaper lớn hơn
giá trị trung bình của cột Newspaper:'''
print(round(data[:, 3][np.where(data[:, 2] > data[:, 2].mean())[0]].sum(), 1))

'''Câu hỏi 20: Gọi giá trị trung bình của cột Sales là A. Tạo ra mảng mới scores chứa các
giá trị Good, Average và Bad sao cho: nếu giá trị hiện tại > A => giá trị trong mảng mới
là Good, < A thì sẽ là Bad và = A sẽ là Average. Sau đó in ra kết quả scores[7:10]'''
A = data[:, 3].mean()
scores = np.where(data[:, 3] > A, 'Good', np.where(data[:, 3] == A, 'Average', 'Bad'))
print(scores[7:10])

'''Câu hỏi 21: Gọi giá trị trên cột Sales gần nhất với giá trị trung bình cũng chính cột
Sales là A. Tạo ra mảng mới scores chứa các giá trị Good, Average và Bad sao cho: nếu
giá trị hiện tại > A => giá trị trong mảng mới là Good, < A thì sẽ là Bad và = A sẽ là
Average. Sau đó in ra kết quả scores[7:10]'''
diff = np.where(data[:, 3] > data[:, 3].mean(), data[:, 3] - data[:, 3].mean(), data[:, 3].mean() - data[:, 3])
A = data[:, 3][np.where(diff == diff.min())]
scores = np.where(data[:, 3] > A, 'Good', np.where(data[:, 3] == A, 'Average', 'Bad'))
print(scores[7:10])


'''
15C
16B
17A
18B
19C
20C
21C
'''