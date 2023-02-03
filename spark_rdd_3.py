from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[4]")\
        .appName("Bigdata")\
        .getOrCreate()
        
# Spark Context Object
sc = spark.sparkContext

# Create the RDD

#rdd = sc.textFile('/home/bigdata/fruits.txt')
#rdd = sc.wholeTextFiles('/home/bigdata/dataset/*') 
rdd = sc.textFile('fruits.txt') 
print(rdd.collect()) 
print('1. Number of partitions: ', rdd.getNumPartitions())

# Create RDD from List
rdd = sc.parallelize([1,2,3,4,5,6,7,8])
print(rdd.collect()) 
print('2. Number of partitions: ', rdd.getNumPartitions())
