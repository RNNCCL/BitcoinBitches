import json 
from pprint import pprint
import pandas as pd 

class Comment(object): 
	date = "" 
	comment = "" 

	def __init__(self, date, comment): 
		self.date = date
		self.comment = comment 



# iterate over all the comments in result.json 
# for each topic, get all the comments. 
# each comment has a date object and the contnent 
# return a dictionary of dates and contents - we're just going to ignore the topics for now 
# although it might be worthwhile to explore the effect that the topic has on the content 

def get_comments(): 
	data = None
	# read a json file  
	with open("result.json") as f: 
		data = json.load(f)


	#pprint(data[0]["replies"][0]["date"])
	#print(len(data))
	comments = []  
	for t in range(len(data)): 
		for c in range(len(data[t]["replies"])): 
			comment = Comment(data[t]["replies"][c]["date"], data[t]["replies"][c]["content"])
			comments.append(comment)
			#pprint(data[t]["replies"][c]["date"])
	comments.sort(key=lambda r: r.date)
	
	for i in range(10): 
		print(comments[i].date)
		print(comments[i].comment)
	return comments 

get_comments() 

