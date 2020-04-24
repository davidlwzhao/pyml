import sklearn_helper as skh

# Use cases of the library
# 1. data exploration
# 2. preprocessing pipelines
# 3. model selection and comparison
# 4. visualization of tuning

# Structure of the libary
# base
# graphs

# Mimic Sklearn API where possible
# OOP implementation

# make data pre-processing pipeline
pipeline = skh.base.make_pipeline()

# make comparison object which will run for multiple different estimators
output = skh.base.compare_estimators(
    pool=[estimator1, estimator2, estimator3],
    cv=10,
    param_grid=param_grid,
    dim_red=['passthrough', PCA(1), PCA(3)],
    preprocessing=[pipeline1, pipeline2],
    n_jobs=-1
)

# comparison object API
# TBC
