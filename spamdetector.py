import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from win32com.client import Dispatch

model = pickle.load(open('spam.pkl','rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))


def main():
	st.title("Email Spam Classification Application")
	st.write("Prabhpreet project")
	activites=["Classification","About"]
	choices=st.sidebar.selectbox("Select Activities",activites)
	if choices=="Classification":
		msg=st.text_input("Enter a text")
		if st.button("predict"):
			print(msg)
			print(type(msg))
			data=[msg]
			print(data)
			vec=cv.transform(data).toarray()
			result=model.predict(vec)

			if result[0]==0:
				st.success("This is Not A Spam Email")
				
			else:
				st.error("This is A Spam Email")
				
main()