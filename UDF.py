# Databricks notebook source
employee_data = [(10,"Ali","1999-06-01","100",2000),
                 (20,"hamza","1997-08-01","200",3000),
                 (30,"Zohaib","2000-03-14","100",90000),
                (40,"Haider","1998-07-01","400",4000),
                (50,"Akbar","1996-08-05","500",80000),
                (60,"Aslam","1995-09-09","600",60000),
                (70,"Arshad","1994-10-07","700",70000)]

employee_scheema = ["employee_id","Name","doj","employee_dept_id","salary"]
empDF = spark.createDataFrame(data=employee_data, schema=employee_scheema)
display(empDF)

# COMMAND ----------

import pyspark.sql.functions as f
def rename_columns(rename_df):
    for column in rename.df.columns:
        new_column = "Col_" +column
        rename_df = rename_df.withColumnRenamed(column, new_column)
    return rename_df

# COMMAND ----------

from pyspark.sql.functions import upper, col
def upperCase_col(df):
    empDF_upper= df.withColumn('name_upper', upper(df.Name))
    return empDF_upper

# COMMAND ----------

Up_Case_DF = upperCase_col(empDF)
display(Up_Case_DF)
