# Databricks notebook source
# MAGIC %md
# MAGIC ##AutoLoader

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

df = (
    spark.readStream.format('cloudFiles')
    .option('cloudFiles.format', 'parquet')
    .option('cloudFiles.schemaLocation', 'abfss://mycontainer@moderndatabricksdatalake.dfs.core.windows.net/autoloader_sink/check')
    .load('abfss://mycontainer@moderndatabricksdatalake.dfs.core.windows.net/autoloader_source')
)

# COMMAND ----------

(
    df.writeStream.format('parquet')
    .option('checkpointLocation', 'abfss://mycontainer@moderndatabricksdatalake.dfs.core.windows.net/autoloader_sink/check')
    .trigger(processingTime= '10 seconds')
    .start('abfss://mycontainer@moderndatabricksdatalake.dfs.core.windows.net/autoloader_sink/data')
)