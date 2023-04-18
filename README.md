# Test samples generated for AI Verify

These sample models and datasets are generated to test AI Verify's capability in testing different AI framework and model type.

All the test datasets can be found in `./data`. All test datasets are stored in pandas dataframe and serialised by pickle. The naming convention for each file is as follows:

```
pickle_pandas_<input type>_<use case>_<training|testing>.sav
```

All the model files can be found in `./model`. All sample models are stored respectively in their framework's folder. Each folder is separated into their version. All model files are serialised by pickle. The naming convention for each file is as follows:

```
<task type:binary_classification|multiclass_classification|regression>_<use case>_<learning algorithm>.sav
```

## How to use the files?

For testing purpose, use `testing` dataset and match each `use case` to the model found in `./model`.

For example, if you are going to test regression models, the respective test dataset can be found by matching the use case `insurance`.

- ./models/sklearn/1.2.2/regression_**insurance**_sklearn_....sav
- ./data/pickle_pandas_tabular_**insurance**_testing.sav
