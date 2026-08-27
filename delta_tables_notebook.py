# Databricks notebook source
# MAGIC %md
# MAGIC ##Delta Tables

# COMMAND ----------

# MAGIC %sql
# MAGIC create table managed_catalog.managed_schema.delta_table
# MAGIC (
# MAGIC     id int,
# MAGIC     name string,
# MAGIC     city string
# MAGIC )
# MAGIC
# MAGIC using delta
# MAGIC location 'abfss://mycontainer@moderndatabricksdatalake.dfs.core.windows.net/deltalake/delta_table'

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE managed_catalog.managed_schema.delta_table
# MAGIC SET TBLPROPERTIES ('delta.enableDeletionVectors' = false);

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into managed_catalog.managed_schema.delta_table
# MAGIC values 
# MAGIC (1, 'aaa', 'los angeles'),
# MAGIC (2, 'bbb', 'athens'),
# MAGIC (3, 'ccc', 'beijing')

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended managed_catalog.managed_schema.delta_table  

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from managed_catalog.managed_schema.delta_table

# COMMAND ----------

# MAGIC %md 
# MAGIC **update**

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE managed_catalog.managed_schema.delta_table
# MAGIC set city = 'amsterdam' where id = 1

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from managed_catalog.managed_schema.delta_table

# COMMAND ----------

# MAGIC %md
# MAGIC **Versioning**

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history managed_catalog.managed_schema.delta_table

# COMMAND ----------

# MAGIC %md
# MAGIC **Time Travel**

# COMMAND ----------

# MAGIC %sql
# MAGIC restore managed_catalog.managed_schema.delta_table to version as of 2

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from managed_catalog.managed_schema.delta_table 

# COMMAND ----------

