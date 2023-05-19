from sklearn.preprocessing import LabelEncoder


class dataProcessingStage:
    def __init__(self, ground_truth_label):
        self._ground_truth_label = ground_truth_label

    def labelencoding(self, df, columnname):
        le = LabelEncoder()
        df[columnname] = le.fit_transform(df[columnname])
        return df

    def removecomma(self, x):
        return x["Loan_Amount_Requested"].replace(",", "")

    def transform(self, X):
        """Convert columns into dataframe for model input"""
        df = X.copy()
        df.drop(self._ground_truth_label, axis=1)
        df = df.drop("Loan_ID", axis=1)

        df["Loan_Amount_Requested"] = df["Loan_Amount_Requested"].str.replace(",", "")
        df["Loan_Amount_Requested"] = df["Loan_Amount_Requested"].astype(int)

        df = self.labelencoding(df, "Length_Employed")
        df = self.labelencoding(df, "Home_Owner")
        df = self.labelencoding(df, "Income_Verified")
        df = self.labelencoding(df, "Purpose_Of_Loan")
        df = self.labelencoding(df, "Gender")

        df = df.fillna(0)
        return df

    def fit(self, X, y=None):
        return self
