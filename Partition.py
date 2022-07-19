# Databricks notebook source
df = spark.read.format("csv").option("inferSchema", True).option("header", True).option("sep",",").load("/FileStore/tables/diabetes-1.csv")
print(df)

# COMMAND ----------

print(df.count())

# COMMAND ----------

print(df.rdd.getNumPartitions())

# COMMAND ----------

df_5 = df.select(df.Glucose,df.MBI,df.Age).repartition(5)

# COMMAND ----------

print(df_5.rdd.getNumPartitions())

# COMMAND ----------

df_5.withColumn("partitionId", spark_partition_id()).groupBy("partitionId").count().show()
