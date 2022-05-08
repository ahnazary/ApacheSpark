import pyspark
import pandas as pd
from pyspark.sql import SparkSession

# df = pd.read_csv('trafficData158324.csv')
# print(df.info())

spark = SparkSession.builder.appName('Practice').getOrCreate()
dfPyspark = spark.read.option('header', 'true').csv('trafficData158324.csv', inferSchema=True)

# print(dfPyspark.printSchema())

# print(dfPyspark.select('status', 'avgMeasuredTime').show(5))

# print(dfPyspark.describe().show())

# dfPyspark = dfPyspark.withColumn('new avg speed', dfPyspark['avgSpeed'] + 2)
# print(dfPyspark.show())
# dfPyspark = dfPyspark.drop('new avg speed')
# print(dfPyspark.show())

dfPyspark = dfPyspark.withColumnRenamed('status', 'new status')
print(dfPyspark.show())