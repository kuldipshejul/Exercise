# Databricks notebook source
import pyspark.sql.functions as F

movies_df = spark.table("default.movies")
display(movies_df)

# COMMAND ----------

user_df = spark.table("default.users")
display(user_df)

# COMMAND ----------

rating_df = spark.table("default.ratings")
display(rating_df)

# COMMAND ----------

# MAGIC %md
# MAGIC What are the top 10 most viewed movies?

# COMMAND ----------

 #eg : joined_df = dataframe.join(dataframe1, 
  #             dataframe.ID == dataframe1.ID, 
  #             "inner")

joined_df=movies_df.join(rating_df,
                         movies_df.MovieID == rating_df.MovieID,
                         "inner").drop("MovieID")
joined_df.show()


# COMMAND ----------

#eg. df1 = df.select(F.col("Title"),F.col("UserID"))
#eg. df1 = df.select("Title","UserID")
#  a. What are the top 10 most viewed movies?
df1 = joined_df.select("Title","UserID").groupBy("Title").count().orderBy("count",ascending=False).limit(10)
df1.show()

