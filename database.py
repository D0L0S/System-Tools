#!/usr/bin/env python
# -*- coding: utf-8 -*-

## #####################
## Database Module
## 30/04/2015
## Written By D0L0S
## #####################

import mysql.connector

class EnvDatabase:

	def __init__(self):
		user='User'
		host='127.0.0.1'
		database='Database'
		self.connection = mysql.connector.connect(user=self.user, host=self.host, database=self.database)

	def query(self, q):
		cursor = self.connection.cursor()
		cursor.execute(q)
		columns = tuple( [d[0].decode('utf8') for d in cursor.description] )
		result = []
		for row in cursor:
			result.append(dict(zip(columns, row)))
		return result

	def __del__(self):
		self.connection.close()


if __name__=="__main__":
	db=EnvDatabase()
