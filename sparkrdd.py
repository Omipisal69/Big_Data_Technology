from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[4]")\
        .appName("Bigdata")\
        .getOrCreate()
        
# Spark Context Object
sc = spark.sparkContext

# Create the RDD
rdd = sc.range(1,5)
print("RDD Context: ", rdd.collect())
