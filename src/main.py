from algo import SVM, Logreg, DTree
from data_extraction import extract_data
from data_preprocessing import pre_processing_data

def main():
    extracted_data = extract_data()
    pre_processed_data = pre_processing_data(extracted_data)

    clf_svm = SVM(pre_processed_data, "Ticket Type")
    clf_log = Logreg(pre_processed_data, "Ticket Type")
    clf_tree = DTree(pre_processed_data, "Ticket Type")


    print("Perform analysis of feature importance in the Logistic Regression model.")
    c_log = clf_log.coef_
    x = pre_processed_data.drop(columns = "Ticket Type")
    names = ['standard', 'luxury', 'deluxe']
    for i in range(3):
        
        indices = c_log[i].argsort()[-5:][::-1]
        print(names[i], "\n", x.columns[indices].tolist())

    
    return


if __name__ == "__main__":
    main()
