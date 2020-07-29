import streamlit as st
import numpy as np
from sklearn import preprocessing
import pandas as pd
#from sklearn.cluster import KMeans
#from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split



d=pd.read_excel("Mann.xlsx")
#st.write("The shape is ",d.shape)
d1=d[:4571]
d2=d[4571:9142]
d3=d[9142:13713]
d4=d[13713:18284]
d5=d[18284:22855]
d6=d[22855:27426]
d7=d[27426:]
lis=[d1,d2,d3,d4,d5,d6,d7]
#cl=st.selectbox("Select the number of clusters",[2,3,4,5,6,7,8,9,10])
a=st.number_input("Enter the Last Period last digit",value=2,step=1)
b=st.number_input("Enter the Last Price last digit",value=2,step=1)
c=st.number_input("Enter the Next Period last digit(You want to predict)",value=2,step=1)
g,r=0,0

p=-1
j=1
if a is None or b is None or c is None:
		st.print("")
else:
	s_type=st.selectbox("Type",["Classification","Clustering"])
	if s_type =="Classification":
		ss=st.selectbox("Class",('A','B'))
		if st.button("Classify"):
			with st.spinner('In Progress...'):
				clf = svm.SVC()
				for i in lis:
					X=i[['A','B','C']]
					y=i['Y']
					X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
					#st.write("The shape is ",d.shape)
					clf.fit(X_train,y_train)
					p=clf.predict([[a,b,c]])
					if p==0:
						r=r+1
						st.write("RED",j)
						j=j+1
					elif p==1:
						g=g+1
						st.write("GREEN",j)
						j=j+1
				if r>g:
					st.error("Next is RED {}".format((r/7)*100))
				else:
					st.success("Next is GREEN {}".format((g/7)*100))			

'''import streamlit as st
import numpy as np
from sklearn import preprocessing
import pandas as pd
#from sklearn.cluster import KMeans
#from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split



d=pd.read_excel("Mann.xlsx")
X=d[['A','B','C']]
y=d['Y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
st.write("The shape is ",d.shape)

#cl=st.selectbox("Select the number of clusters",[2,3,4,5,6,7,8,9,10])
a=st.number_input("Enter the Last Period last digit",value=2,step=1)
b=st.number_input("Enter the Last Price last digit",value=2,step=1)
c=st.number_input("Enter the Next Period last digit(You want to predict)",value=2,step=1)
g,r=0,0

p=-1
if a is None or b is None or c is None:
		st.print("")
else:
	s_type=st.selectbox("Type",["Classification","Clustering"])
	if s_type =="Classification":
		ss=st.selectbox("Class",('A','B'))
		if st.button("Classify"):
			with st.spinner('In Progress...'):
				clf = svm.SVC()
				clf.fit(X_train,y_train)
				if ss=="A":
					p=clf.predict([[a,b,c]])
					if p==0:
						st.error("Next is RED")
					elif p==1:
						st.success("Next is GREEN")
				elif ss=="B":
					p=clf.predict([[a,b,c]])
					if p==0:
						st.error("Next is GREEN")
					elif p==1:
						st.success("Next is RED")
'''					
