from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def SVM(df, target_column, kernel='linear', test_size=0.2, random_state=42):

    from sklearn import svm
    X = df.drop(columns=[target_column])
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size,
                                                        random_state=random_state, stratify=y)

    scaler = StandardScaler()


    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    clf = svm.SVC(kernel=kernel, decision_function_shape='ovo')
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    report = classification_report(y_test, y_pred)
    print("1.0: Standard, 2.0: Luxury, 3.0: Deluxe")
    print("SVM Classification Report:\n", report)

    return clf

def Logreg(df, target_column, test_size=0.2, random_state=10):

    from sklearn.linear_model import LogisticRegression

    X = df.drop(columns=[target_column])
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size,
                                                        random_state=random_state, stratify=y)

    scaler = MinMaxScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    clf = LogisticRegression(random_state=random_state, max_iter=1000, multi_class='multinomial',
                             solver="sag", penalty="l2")
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    report = classification_report(y_test, y_pred)
    print("1.0: Standard, 2.0: Luxury, 3.0: Deluxe")
    print("Log Regression Classification Report:\n", report)

    return clf


def DTree(df, target_column, test_size=0.2, random_state=42):

    from sklearn.tree import DecisionTreeClassifier

    X = df.drop(columns=[target_column])
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size,
                                                        random_state=random_state, stratify=y)

    clf = DecisionTreeClassifier(random_state=random_state)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    report = classification_report(y_test, y_pred)
    print("1.0: Standard, 2.0: Luxury, 3.0: Deluxe")
    print(" Decision Tree Classification Report:\n", report)

    return clf
