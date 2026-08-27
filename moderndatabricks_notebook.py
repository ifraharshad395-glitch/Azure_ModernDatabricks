# Databricks notebook source
# MAGIC %md
# MAGIC ##Scenario -1

# COMMAND ----------

# MAGIC %md
# MAGIC ###-Managed Catalog -Managed Schema -Managed Table

# COMMAND ----------

# MAGIC %sql
# MAGIC create catalog managed_catalog

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema managed_catalog.managed_schema

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists managed_catalog.managed_schema.managed_table
# MAGIC (
# MAGIC     id int,
# MAGIC     name string
# MAGIC )
# MAGIC
# MAGIC using delta

# COMMAND ----------

# MAGIC %md
# MAGIC ##Scenario -2

# COMMAND ----------

# MAGIC %md
# MAGIC ###-External Catalog -Managed Schema -Managed Table

# COMMAND ----------

# MAGIC %sql
# MAGIC create catalog external_catalog 
# MAGIC managed location 'abfss://mycontainer@moderndatabricksdatalake.dfs.core.windows.net/external_catalog'

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema external_catalog.managed_schema

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists external_catalog.managed_schema.managed_table2
# MAGIC (
# MAGIC     id int,
# MAGIC     name string
# MAGIC )
# MAGIC
# MAGIC using delta

# COMMAND ----------

# MAGIC %md
# MAGIC ##Scenario -3

# COMMAND ----------

# MAGIC %md
# MAGIC ###-External Catalog -External Schema -Managed Table

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema external_catalog.external_schema
# MAGIC managed location 'abfss://mycontainer@moderndatabricksdatalake.dfs.core.windows.net/external_schema'

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists external_catalog.external_schema.managed_table3
# MAGIC (
# MAGIC     id int,
# MAGIC     name string
# MAGIC )
# MAGIC
# MAGIC using delta

# COMMAND ----------

# MAGIC %md
# MAGIC ##Scenario -4

# COMMAND ----------

# MAGIC %md
# MAGIC ###-External Table

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists managed_catalog.managed_schema.external_table
# MAGIC (
# MAGIC     id int,
# MAGIC     name string
# MAGIC )
# MAGIC
# MAGIC using delta
# MAGIC location 'abfss://mycontainer@moderndatabricksdatalake.dfs.core.windows.net/external_table/managed_table4'

# COMMAND ----------

# MAGIC %md
# MAGIC ##Querying Files Using SELECT

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into managed_catalog.managed_schema.external_table
# MAGIC values 
# MAGIC (1, 'aa'),
# MAGIC (2, 'bb'),
# MAGIC (3, 'cc')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from managed_catalog.managed_schema.external_table

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta.`abfss://mycontainer@moderndatabricksdatalake.dfs.core.windows.net/external_table/managed_table4`

# COMMAND ----------

# MAGIC %md
# MAGIC ##Permanent Views

# COMMAND ----------

# MAGIC %sql
# MAGIC create view managed_catalog.managed_schema.view_1
# MAGIC as 
# MAGIC select * from delta.`abfss://mycontainer@moderndatabricksdatalake.dfs.core.windows.net/external_table/managed_table4` 
# MAGIC where id = 1

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from managed_catalog.managed_schema.view_1

# COMMAND ----------

# MAGIC %md
# MAGIC ##Volumes

# COMMAND ----------

# MAGIC %md 
# MAGIC **Creating directory for Volumes**

# COMMAND ----------

dbutils.fs.mkdirs('abfss://mycontainer@moderndatabricksdatalake.dfs.core.windows.net/volumes')

# COMMAND ----------

# MAGIC %md 
# MAGIC **Creating a Volume**

# COMMAND ----------

# MAGIC %sql
# MAGIC create external volume managed_catalog.managed_schema.external_volume
# MAGIC location 'abfss://mycontainer@moderndatabricksdatalake.dfs.core.windows.net/volumes'

# COMMAND ----------

# MAGIC %md 
# MAGIC **Copy file for Volume**

# COMMAND ----------

dbutils.fs.cp('abfss://mycontainer@moderndatabricksdatalake.dfs.core.windows.net/source/Sales.csv', 'abfss://mycontainer@moderndatabricksdatalake.dfs.core.windows.net/volumes/Sales.csv')

# COMMAND ----------

# MAGIC %md 
# MAGIC **Querying the Volume**

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from csv.`/Volumes/managed_catalog/managed_schema/external_volume/Sales.csv`