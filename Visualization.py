# Databricks notebook source
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# COMMAND ----------

a=np.array([1,2,3,4,5])
a

# COMMAND ----------

a=np.array([1,2,10,4,56])
a

plt.plot(a)
plt.show()

# COMMAND ----------

a=np.array([43,2,58,4,5])
b=np.array([62,2,5,3,28])
plt.plot(a)
plt.plot(b)
plt.show()

# COMMAND ----------

a=np.array([400,200,500,400,500])
b=np.array([600,200,500,300,200])
c=np.array([100,300,500,200,100])

plt.figure(figsize=(10,8))

plt.plot(a, color='green', linestyle='-.', label="Rent 2024")
plt.plot(b, linewidth=5., label="AVG Rent")
plt.plot(c,color="red", linestyle='--', label="Rent 2023")
plt.title("Rent per month summary", fontsize=20, fontweight="bold")
plt.legend(loc="upper left", fontsize=15)
plt.xticks(range(0,len(a)),('Jan','Feb','Mar','Apr','May'))
plt.xlabel("Month")
plt.ylabel("Rent $")
plt.show()

# COMMAND ----------


