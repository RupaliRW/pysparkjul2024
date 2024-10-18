# This is a sample Python script.
import sys

from pyspark import SparkContext
from pyspark.sql import SparkSession

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
       # sc = SparkContext("local[1]", "AppName")
    spark = SparkSession.builder.appName("p1").getOrCreate()
    sc=spark.sparkContext
    rdd1 = sc.textFile(str(sys.argv[1]))
    words = rdd1.flatMap(lambda line: line.split(" "))
    wordcount = words.map(lambda w: (w, 1))
    result = wordcount.reduceByKey(lambda x, y : x + y)
    res = result.collect()
    for (w, c) in res:
        print(w + " -- " + str(c))
    print("done*******************************")
    print("18-10-2024 7::15 pm IST  1:45 UK")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
