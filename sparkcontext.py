from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]")\
        .appName("Bigdata")\
        .getOrCreate()
        
print('Spark Version:', spark.version)        

#print(spark.sparkContext)
#print("Spark App Name: ", spark.sparkContext.appName)

sc = spark.sparkContext
print(sc)
print("Spark App Name: ", sc.appName)
