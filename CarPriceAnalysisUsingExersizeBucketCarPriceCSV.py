# Databricks notebook source
access_key = 'AKIA2UC3CHGOHTVVOBPU'
secret_key = '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'
sc._jsc.hadoopConfiguration().set("fs.s3a.access.key", access_key)
sc._jsc.hadoopConfiguration().set("fs.s3a.secret.key", secret_key)

# If you are using Auto Loader file notification mode to load files, provide the AWS Region ID.
aws_region = "ap-south-1"
sc._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3." + aws_region + ".amazonaws.com")

df = spark.read.option("delimiter", ",").csv('s3://exersize-bucket/car_prices.csv',inferSchema=True,header=True)
#Example#
#df = spark.read.csv('s3a://techykuntal-demo-data-bucket/employee/*',inferSchema=True,header=True)
display(df)
