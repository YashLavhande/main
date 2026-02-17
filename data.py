from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .getOrCreate()
data = [
    (1, "Yash", 25),
    (2, "Rahul", 30),
    (3, "Priya", 22)
]

columns = ["id", "name", "age"]

df = spark.createDataFrame(data, columns)
