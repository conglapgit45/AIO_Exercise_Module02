import numpy as np


# 4.1 Hoàn thiện function create_train_dataset() để tổ chức dữ liệu bảng 1 vào array 2 chiều
def create_train_data():
    data = [
        ['Sunny', 'Hot', 'High', 'Weak', 'no'],
        ['Sunny','Hot', 'High', 'Strong', 'no'],
        ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
        ['Overcast', 'Mild', 'High', 'Weak', 'no'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'yes'],
    ]
    return np.array(data)


# 4.2 Hoàn thiện function compute_prior_probability tính P("Play Tennis" = "Yes") and tính P("Play Tennis" = "No")
def compute_prior_probablity(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))
    Y = train_data[:, -1]
    prior_probability = [(Y == y_unique[i]).sum() / len(Y) for i in range(len(y_unique))]
    return prior_probability


# 4.3 Hoàn thiện function compute_conditional_probability để tính likelihood (The probability of "A" being True. Given "B" True, P(A|B))
def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    Y = train_data[:, -1]
    conditional_probability = []
    list_x_name = []
    for i in range(0, train_data.shape[1] -1):
        x_unique = np.unique(train_data[:, i])
        X = train_data[:, i]
        list_x_name.append(x_unique)
        x_conditional_probability = np.array([[((X == x_unique[m]) & (Y == y_unique[k])).sum() / (Y == y_unique[k]).sum() for m in range(len(x_unique))] for k in range(len(y_unique))])
        conditional_probability.append(x_conditional_probability)
    return conditional_probability , list_x_name


# 4.4 Hoàn thiện function get_index_from_value để tính trả về index tương ứng với feature name:
def get_index_from_value(feature_name, list_features) :
    return np.where(list_features == feature_name)[0][0]


# 4.5 Hoàn thiện function train_naive_bayes
def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    y_unique = ['no', 'yes']
    prior_probability = compute_prior_probablity(train_data)
    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(train_data)
    return prior_probability, conditional_probability, list_x_name


# 4.6 Hoàn thiện function prediction_play_tennis để hỗ trợ AD có nên đi chơi tennis vào ngày D11 không:
def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(X[0], list_x_name[0])
    x2 = get_index_from_value(X[1], list_x_name[1])
    x3 = get_index_from_value(X[2], list_x_name[2])
    x4 = get_index_from_value(X[3], list_x_name[3])
    p0 = 0
    p1 = 0
    p0 = np.round(conditional_probability[0][0, x1], 2)
    p1 = np.round(conditional_probability[0][1, x1], 2)
    if p0 > p1 :
        y_pred = 0
    else :
        y_pred = 1
    return y_pred


if __name__ == "__main__":
    # Create train data
    train_data = create_train_data()
    print(train_data)

    # Câu hỏi 14:
    prior_probablity = compute_prior_probablity(train_data)
    print("P(play tennis = No)", prior_probablity[0])
    print("P(play tennis = Yes)", prior_probablity[1])

    # Câu hỏi 15:
    compute_conditional_probability(train_data)
    _, list_x_name = compute_conditional_probability(train_data)
    print("x1 = ", list_x_name[0])
    print("x2 = ", list_x_name[1])
    print("x3 = ", list_x_name[2])
    print("x4 = ", list_x_name[3])

    # Câu hỏi 16:
    outlook = list_x_name[0]
    i1 = get_index_from_value("Overcast", outlook)
    i2 = get_index_from_value("Rain", outlook)
    i3 = get_index_from_value("Sunny", outlook)
    print(i1, i2, i3)

    # Câu hỏi 17:
    conditional_probability, list_x_name = compute_conditional_probability(train_data)
    # Compute P(" Outlook "=" Sunny "| Play Tennis "=" Yes ")
    x1 = get_index_from_value("Sunny", list_x_name[0])
    print("P('Outlook'='Sunny'|'Play Tennis'='Yes') = ", np.round(conditional_probability[0][1, x1], 2))

    # Câu hỏi 18:
    x1 = get_index_from_value("Sunny", list_x_name[0])
    print("P('Outlook'='Sunny'|'Play Tennis'='No') = ", np.round(conditional_probability[0][0, x1], 2))

    # Câu hỏi 19:
    X = ['Sunny', 'Cool', 'High', 'Strong']
    data = create_train_data()
    prior_probability, conditional_probability, list_x_name = train_naive_bayes(data)
    pred = prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability)
    if(pred):
        print("Ad should go!")
    else:
        print("Ad should not go!")