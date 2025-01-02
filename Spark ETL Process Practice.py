# Databricks notebook source
# MAGIC %md
# MAGIC Spark Core 
# MAGIC 	All inframstructure relateted information , how job process.
# MAGIC 	We can read unstructured data using RDD and make it structred.
# MAGIC Spark SQL
# MAGIC 	Processing structred and semi-structured data .
# MAGIC 	Dataframe
# MAGIC 	
# MAGIC 	Dataset 
# MAGIC 	
# MAGIC Spark Streaming 
# MAGIC
# MAGIC
# MAGIC Dataframe : 
# MAGIC
# MAGIC Collection Of Rows having columns with some schema or header.
# MAGIC
# MAGIC ETL
# MAGIC E - Extract  -> Read data to dataframe from any source 
# MAGIC T - Transform -> Process and transform dataframe to a meaningfull result
# MAGIC L - Load      -> write dataframe to specific location with some format
# MAGIC
# MAGIC -------------------------------------------------------------------------
# MAGIC
# MAGIC E - Extract  -> Read data to dataframe from any source 
# MAGIC
# MAGIC DF = spark.read.csv("pathtocsv")
# MAGIC
# MAGIC schemaVariable = StructType([
# MAGIC       StructField("columnname1",IntegerType(),True),
# MAGIC 		.......
# MAGIC       StructField("columnnameN",StringType(),True)
# MAGIC   ])
# MAGIC
# MAGIC DF = spark.read.schema(schemaVariable).csv("pathtocsv")
# MAGIC DF = spark.read.options("header","true").load("path")
# MAGIC
# MAGIC DF = spark.creteDataframe(data=ListofRows, schema= listOfColumns)
# MAGIC
# MAGIC df.createOrReplaceTempView("SAMPLE_TABLE")
# MAGIC DF = spark.sql("Select * from SAMPLE_TABLE")
# MAGIC
# MAGIC DF = spark.read.parquet("PathToParquet")
# MAGIC DF = spark.read.avro("avroPath")
# MAGIC DF = spark.read.json("JsonPath")
# MAGIC
# MAGIC T - Transform -> Process and transform dataframe to a meaningfull result.
# MAGIC
# MAGIC The process of transforming one dataframe to another dataframe is called transform.
# MAGIC select
# MAGIC limit,filter,where
# MAGIC
# MAGIC groupBy, orderBy, withColumn, ColumnRenamed, Window Functions.
# MAGIC
# MAGIC
# MAGIC
# MAGIC L - Load      -> write dataframe to specific location with some format
# MAGIC
# MAGIC DF.write().partitionBy(columnname).csv("HdfsPathToWrite") 
# MAGIC DF.write().partitionBy(columnname).parquet("HdfsPathToWrite") 
# MAGIC DF.write().partitionBy(columnname).avro("HdfsPathToWrite") 
# MAGIC DF.write().partitionBy(columnname).json("HdfsPathToWrite") 
# MAGIC
