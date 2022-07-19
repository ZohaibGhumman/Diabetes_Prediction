# Databricks notebook source
Transaction = [(100, 'Cosmetic', 150),
               (200, 'Apparel', 250),
               (300, 'Pant', 1300),
               (400, 'Shirt', 1500),
               (500, 'Socks', 90),
              (600, 'Belt', 600),
              (100, 'Shorts', 100)]
transactionDF=spark.createDataFrame(data=Transaction, schema=['Store_id', 'Item', 'Amount'])
transactionDF.show()

# COMMAND ----------

Store=[(100, 'Store_London'),
      (200, 'Store_Paris'),
      (300, 'Store_Lahore'),
      (400, 'Store_Faisalabad'),
      (500, 'Store_Islamabad')]
storeDF=spark.createDataFrame(data=Store, schema=['Store_id','Store_Name'])
storeDF.show()

# COMMAND ----------

from pyspark.sql.functions import broadcast
joinDF=transactionDF.join(broadcast(storeDF),transactionDF['Store_id']==storeDF['Store_id'])
joinDF.show()

# COMMAND ----------


