from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]")\
        .appName("Bigdata")\
        .getOrCreate()
        
print('Spark Version:', spark.version)        

df = spark.createDataFrame([("Scala", 25000),("Spark", 35000), ("PHP", 21000)])

print(df.show())
