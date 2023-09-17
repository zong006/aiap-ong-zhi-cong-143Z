from algo import SVM, Logreg, DTree
from data_extraction import extract_data
from data_preprocessing import pre_processing_data

def main():
    extracted_data = extract_data()
    pre_processed_data = pre_processing_data(extracted_data)

    clf_svm = SVM(pre_processed_data, "Ticket Type")
    clf_log = Logreg(pre_processed_data, "Ticket Type")
    clf_tree = DTree(pre_processed_data, "Ticket Type")
    return


if __name__ == "__main__":
    main()