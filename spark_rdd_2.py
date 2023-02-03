from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[4]")\
        .appName("Bigdata")\
        .getOrCreate()
        
# Spark Context Object
sc = spark.sparkContext

# Create the RDD
data = [1,2,3,4,5,6,7,8,9,10,11,12]  #List(range(1,13))
rdd = sc.parallelize(data)
print("RDD Context: ", rdd.collect()) 
