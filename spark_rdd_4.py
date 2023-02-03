from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[4]")\
        .appName("Bigdata")\
        .getOrCreate()
        
# Spark Context Object
sc = spark.sparkContext

# Create RDD from List

rdd = sc.parallelize([1,2,3,4,5,6,7,8])
print(rdd.collect()) 
print('Number of partitions: ', rdd.getNumPartitions())
rdd2 = rdd.repartition(2)
print('Number of partitions: ', rdd2.getNumPartitions())
