# Databricks notebook source
# MAGIC %sql
# MAGIC ALTER TABLE default.raw_supply_chain 
# MAGIC SET TBLPROPERTIES (
# MAGIC   'delta.columnMapping.mode' = 'name',
# MAGIC   'delta.minReaderVersion' = '2',
# MAGIC   'delta.minWriterVersion' = '5'
# MAGIC );

# COMMAND ----------

# DBTITLE 1,Cell 2
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE master_supply_chain AS
# MAGIC SELECT 
# MAGIC     `Type` AS Type,
# MAGIC     `Days for shipping (real)` AS Days_for_shipping_real,
# MAGIC     `Days for shipment (scheduled)` AS Days_for_shipment_scheduled,
# MAGIC     `Benefit per order` AS Benefit_per_order,
# MAGIC     `Sales per customer` AS Sales_per_customer,
# MAGIC     `Delivery Status` AS Delivery_Status,
# MAGIC     `Late_delivery_risk` AS Late_delivery_risk,
# MAGIC     `Category Id` AS Category_Id,
# MAGIC     `Category Name` AS Category_Name,
# MAGIC     `Customer City` AS Customer_City,
# MAGIC     `Customer Country` AS Customer_Country,
# MAGIC     `Customer Email` AS Customer_Email,
# MAGIC     `Customer Fname` AS Customer_Fname,
# MAGIC     `Customer Id` AS Customer_Id,
# MAGIC     `Customer Lname` AS Customer_Lname,
# MAGIC     `Customer Password` AS Customer_Password,
# MAGIC     `Customer Segment` AS Customer_Segment,
# MAGIC     `Customer State` AS Customer_State,
# MAGIC     `Customer Street` AS Customer_Street,
# MAGIC     `Customer Zipcode` AS Customer_Zipcode,
# MAGIC     `Department Id` AS Department_Id,
# MAGIC     `Department Name` AS Department_Name,
# MAGIC     `Latitude` AS Latitude,
# MAGIC     `Longitude` AS Longitude,
# MAGIC     `Market` AS Market,
# MAGIC     `Order City` AS Order_City,
# MAGIC     `Order Country` AS Order_Country,
# MAGIC     `Order Customer Id` AS Order_Customer_Id,
# MAGIC     `order date (DateOrders)` AS order_date_DateOrders,
# MAGIC     `Order Id` AS Order_Id,
# MAGIC     `Order Item Cardprod Id` AS Order_Item_Cardprod_Id,
# MAGIC     `Order Item Discount` AS Order_Item_Discount,
# MAGIC     `Order Item Discount Rate` AS Order_Item_Discount_Rate,
# MAGIC     `Order Item Id` AS Order_Item_Id,
# MAGIC     `Order Item Product Price` AS Order_Item_Product_Price,
# MAGIC     `Order Item Profit Ratio` AS Order_Item_Profit_Ratio,
# MAGIC     `Order Item Quantity` AS Order_Item_Quantity,
# MAGIC     `Sales` AS Sales,
# MAGIC     `Order Item Total` AS Order_Item_Total,
# MAGIC     `Order Profit Per Order` AS Order_Profit_Per_Order,
# MAGIC     `Order Region` AS Order_Region,
# MAGIC     `Order State` AS Order_State,
# MAGIC     `Order Status` AS Order_Status,
# MAGIC     `Order Zipcode` AS Order_Zipcode,
# MAGIC     `Product Card Id` AS Product_Card_Id,
# MAGIC     `Product Category Id` AS Product_Category_Id,
# MAGIC     `Product Description` AS Product_Description,
# MAGIC     `Product Image` AS Product_Image,
# MAGIC     `Product Name` AS Product_Name,
# MAGIC     `Product Price` AS Product_Price,
# MAGIC     `Product Status` AS Product_Status,
# MAGIC     `shipping date (DateOrders)` AS shipping_date_DateOrders,
# MAGIC     `Shipping Mode` AS Shipping_Mode,
# MAGIC     CAST(to_timestamp(`order date (DateOrders)`, 'M/d/yyyy H:mm') AS DATE) AS Order_Date_Clean,
# MAGIC     CASE WHEN `Delivery Status` = 'Late delivery' THEN 1 ELSE 0 END AS Late_Flag
# MAGIC FROM default.raw_supply_chain;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM master_supply_chain