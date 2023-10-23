import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder


class DataPrepocessor:
    """
    A helper tool for scaling and one hot encoding the dataset

    """

    def __init__(self):
        self.feature_to_ohe = []
        self.feature_encoded_list = []

        self.columns_to_scale = []
        self.scale_ignore_columns = []

        self.columns_to_ohe = []

        self.scaler = MinMaxScaler()
        self.ohe = OneHotEncoder(handle_unknown="ignore", sparse=False)
        self.null_columns = []
        self.single_value_columns = []

    def assign_column_types(self, df):
        """
        Assign the correct type to each column in the DataFrame based on the following:
        - Integer values -> int
        - String values -> category
        - Float values -> float64

        Parameters:
        - df: The input DataFrame.

        Returns:
        - DataFrame with columns assigned appropriate types.
        """

        for col in df.columns:
            unique_values = df[col].unique()

            # Check if the unique values in the column are only 1.0 and 0
            if set(unique_values) in (
                {1.0, 0.0},
                {1, 0},
            ):
                df[col] = df[col].astype("int")
                self.scale_ignore_columns.append(col)

            # Check for integer columns
            elif pd.api.types.is_integer_dtype(df[col]):
                df[col] = df[col].astype(int)

            # Check for float columns
            elif pd.api.types.is_float_dtype(df[col]):
                df[col] = df[col].astype(np.float64)

            # Check for string columns
            elif pd.api.types.is_string_dtype(df[col]):
                df[col] = df[col].astype("object")

        return df

    def fit_transform_scaler(self, df):
        """
        Fit the given dataframe, and transform the dataframe

        Parameters:
            df

        Returns:
            None

        """

        # Fit
        self.columns_to_scale = list(
            set(df.select_dtypes(include=[np.number]).columns.tolist())
            - set(self.scale_ignore_columns)
        )
        self.scaler.fit(df[self.columns_to_scale])

        # Transform
        df[self.columns_to_scale] = self.scaler.transform(df[self.columns_to_scale])

        return df

    def convert_binary_to_categorical(self, df):
        """
        Convert columns with 2 unique values in the DataFrame to categorical type.

        Parameters:
        - df: pandas DataFrame


        Returns:
        - Modified pandas DataFrame with relevant columns converted to categorical type
        """
        for col in df.columns:
            if df[col].nunique() <= 2:
                df[col] = df[col].astype("category")

        return df


#     def one_hot_encode(self, df):
#         # One-hot encode the data and recover original columns order
#         # numerical_cols    = df.select_dtypes(include=[np.number]).columns.tolist()
#         # categorical_cols  = df.select_dtypes(exclude=[np.number]).columns.tolist()
#         numerical_cols    = self.columns_to_scale
#         categorical_cols  = self.columns_to_ohe


#         cat_enc_data = df[categorical_cols]
#         # One-hot encode categorical data
#         for col in categorical_cols:
#             cat_enc_data = pd.concat([cat_enc_data, pd.get_dummies(cat_enc_data[col], prefix=col)],axis=1)
#             cat_enc_data = cat_enc_data.drop(col, axis=1)

#         encoded_data = pd.concat([df[numerical_cols], cat_enc_data],axis=1)

#         # Add encoded features that do not appear in train/test but are present in test/train, respectively.
#         diff1 = set(self.feature_encoded_list) - set(encoded_data.columns)
#         for var in diff1:
#             encoded_data[var] = 0
#         print( 'WARNING: the following features are set to 0')
#         print(diff1)

#         diff2= set(encoded_data.columns) - set(self.feature_encoded_list)
#         for var in diff2:
#             encoded_data.drop(var, axis=1, inplace=True)
#         print('WARNING: the following features are dropped')
#         print(diff2)

#         # Unify column identifiers
#         encoded_data = encoded_data[self.feature_encoded_list]

#         return encoded_data
