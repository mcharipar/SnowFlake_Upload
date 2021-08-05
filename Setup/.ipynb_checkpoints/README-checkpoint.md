# Setup

## [Install Anaconda](https://www.anaconda.com/products/individual)

## Create the ENV

Navigate to this dir and execute this command from the cli:
```
conda env create
```
If you are running Linux use this command in the terminal:
```
source conda env create
```
> *It will take a few minues to execute.*

If afterwards the cli reads `CondaEnvException: Pip failed` then you must pip in the Snowflake connector with these commands:

```
pip install -r https://raw.githubusercontent.com/snowflakedb/snowflake-connector-python/v2.4.6/tested_requirements/requirements_36.reqs
```

```
pip install snowflake-connector-python==2.4.6
```

```
pip install snowflake-connector-python[pandas]
```

If you got a `ResolvePackageNotFound` error instead, reference [this article](Setting_Up_a_Conda_Environment.pdf) that comes from [this site](https://medium.com/swlh/setting-up-a-conda-environment-in-less-than-5-minutes-e64d8fc338e4).

---
Click here for more info on the [Snowflake Python Connector](https://docs.snowflake.com/en/user-guide/python-connector.html)
