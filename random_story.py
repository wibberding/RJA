from random import randint
adjList=["wild","fluffy","hilarious"]
placeList=["Chicago","China","Brazil"]
nounList=["telephone", "karate", "toilet"]

index1=randint(0,len(adjList)-1)
adj1=adjList[index1]
index2=randint(0,len(adjList)-1)
adj2=adjList[index2]
index3=randint(0,len(adjList)-1)
adj3=adjList[index3]

index1=randint(0,len(placeList)-1)
place1=placeList[index1]
index2=randint(0,len(placeList)-1)
place2=placeList[index2]
index3=randint(0,len(placeList)-1)
place3=placeList[index3]

index1=randint(0,len(adjList)-1)
noun1=nounList[index1]
index2=randint(0,len(adjList)-1)
noun2=nounList[index2]
index3=randint(0,len(adjList)-1)
noun3=nounList[index3]

sentence1= "Last year, I went on a "+adj1+" trip to "+place1+"." 
sentence2= "The weather there was "+adj2+", and I couldn't wait to eat a big "+noun1+" while I was there."
sentence3="Next year, I want to go to "+place2+", because I've always wanted to see the "+adj3+" "+noun2+"."
print (sentence1,sentence2,sentence3)
