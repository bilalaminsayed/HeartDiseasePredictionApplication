from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import joblib
import pandas as pd
import os

#initialization of gloabal variables used to get input and pass to the model
patientName = "Patient Name"
age = 0
sex = 0
cp = 0
trestbps = 0
chol = 0
fbs = 0
restecg = 0
thalach = 0
exang = 0
oldpeak = 0
slope = 0
ca = 0
thal = 0
result = 0

#method to close window when close button is clicked
def CloseBtnClickFunction():
	master.destroy()

#method to open result window
def openResultWindow():
	#declaration of global variables used to display result
	global patientName
	global result

	#new tkinter window to diplay result
	newResultWindow = Toplevel(master)
	newResultWindow.geometry('558x380')
	newResultWindow.configure(background='#F0F8FF')
	newResultWindow.title('Results')

	Label(newResultWindow, text='Prediction for', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=208, y=45)

	#label to display patient name
	patientNameLabel = Label(newResultWindow, text='Patient Name', bg='#F0F8FF', font=('arial', 12, 'normal'))
	patientNameLabel.place(x=208, y=95)

	Label(newResultWindow, text='is', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=248, y=135)

	#label to diplay prediction result
	predicitonLabel = Label(newResultWindow, text='Heart Disease Prediction', bg='#F0F8FF', font=('arial', 12, 'normal'))
	predicitonLabel.place(x=178, y=175)

	#set patient name label
	patientNameLabel.configure(text=patientName)

	#if else to set heart disease positive or negative based on result from model
	if result[0] == 0:
		predicitonLabel.configure(text='Heart Disease Negative')
	else:
		predicitonLabel.configure(text='Heart Disease Positive')

#method to open prediction window
def openPredictWindow():
	#new tkinter window to diplay predicition window
	newWindow = Toplevel(master)
	newWindow.geometry('1000x600')
	newWindow.configure(background='#F0F8FF')
	newWindow.title('New Prediction')

	Label(newWindow, text='Patient Name', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=27, y=16)

	#patient name text box
	patientNameTBox = Entry(newWindow)
	patientNameTBox.place(x=137, y=16)

	Label(newWindow, text='Age', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=27, y=96)

	#age spin box to restict input to numbers
	AgeSpinBox = Spinbox(newWindow, from_=1, to=1020, font=('arial', 12, 'normal'), bg='#F0F8FF', width=3)
	AgeSpinBox.place(x=137, y=96)

	Label(newWindow, text='Sex', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=27, y=146)

	#sex combo box to restrict input
	sexComboBox = ttk.Combobox(newWindow, values=['Male', 'Female'], font=('arial', 12, 'normal'), width=10)
	sexComboBox.place(x=137, y=146)
	sexComboBox.current(1)

	Label(newWindow, text='Chest Pain', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=27, y=196)

	#cp combo box to restrict input
	cpComboBox = ttk.Combobox(newWindow,
									 values=['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'],
									 font=('arial', 12, 'normal'), width=10)
	cpComboBox.place(x=137, y=196)
	cpComboBox.current(1)

	Label(newWindow, text='Resting Blood Pressure', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=27, y=246)

	#trestbps spin box to restict input to numbers
	trestbpsSpinBox = Spinbox(newWindow, from_=1, to=300, font=('arial', 12, 'normal'), bg='#F0F8FF', width=5)
	trestbpsSpinBox.place(x=207, y=246)

	Label(newWindow, text='mm Hg ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=277, y=246)

	Label(newWindow, text='Cholestoral', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=27, y=296)

	#chol spin box to restict input to numbers
	cholSpinBox = Spinbox(newWindow, from_=1, to=300, font=('arial', 12, 'normal'), bg='#F0F8FF', width=5)
	cholSpinBox.place(x=137, y=296)

	Label(newWindow, text='mg/dl', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=207, y=296)

	Label(newWindow, text='Fasting Blood Sugar', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=27, y=346)

	#fbs combo box to restrict input
	fbsComboBox = ttk.Combobox(newWindow, values=['> 120 mg/dl', '< 120 mg/dl'], font=('arial', 12, 'normal'), width=10)
	fbsComboBox.place(x=187, y=346)
	fbsComboBox.current(1)

	Label(newWindow, text='Resting Electrocardiographic Results', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=27,
																											   y=396)
	#restecg combo box to restrict input
	restecgComboBox = ttk.Combobox(newWindow, values=['Normal', 'Having ST-T', 'Hypertrophy'], font=('arial', 12, 'normal'),
								   width=10)
	restecgComboBox.place(x=307, y=396)
	restecgComboBox.current(1)

	Label(newWindow, text='Maximum Heart Rate Achieved 1', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=477, y=96)

	#thalch spin box to restict input to numbers
	thalachSpinBox = Spinbox(newWindow, from_=1, to=300, font=('arial', 12, 'normal'), bg='#F0F8FF', width=5)
	thalachSpinBox.place(x=717, y=96)

	Label(newWindow, text='Exercise Induced Angina', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=477, y=146)

	#restecg combo box to restrict input
	exangComboBox = ttk.Combobox(newWindow, values=['Yes', 'No'], font=('arial', 12, 'normal'), width=10)
	exangComboBox.place(x=717, y=146)
	exangComboBox.current(1)

	Label(newWindow, text='ST Depression Induced by Exercise Relative to Rest', bg='#F0F8FF',
		  font=('arial', 12, 'normal')).place(x=477, y=196)

	#oldpeak text input
	oldpeakTInput = Entry(newWindow)
	oldpeakTInput.place(x=857, y=196)

	Label(newWindow, text='Peak Exercise ST Segment Slope', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=477, y=246)

	#slope combo box to restrict input
	slopeComboBox = ttk.Combobox(newWindow, values=['Upsloping', 'Flat', 'Downsloping'], font=('arial', 12, 'normal'),
								 width=10)
	slopeComboBox.place(x=727, y=246)
	slopeComboBox.current(1)

	Label(newWindow, text='Number of Major Vessels Colored by Flourosopy', bg='#F0F8FF', font=('arial', 12, 'normal')).place(
		x=477, y=296)

	#ca combo box to restrict input
	caComboBox = ttk.Combobox(newWindow, values=['0', '1', '2', '3'], font=('arial', 12, 'normal'), width=10)
	caComboBox.place(x=837, y=296)
	caComboBox.current(1)

	Label(newWindow, text='Thalassemia', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=477, y=346)

	#thal combo box to restrict input
	thalComboBox = ttk.Combobox(newWindow, values=['Normal', 'Fixed Defect', 'Reversable Defect'],
								font=('arial', 12, 'normal'), width=10)
	thalComboBox.place(x=717, y=346)
	thalComboBox.current(1)

	#function to close window when cancel is clicked
	def CancelBtnClickFunction():
		newWindow.destroy()

	#function to get all values and set global variables
	def getValues():
		#gloabal variables declaration
		global patientName
		global age
		global sex
		global cp
		global trestbps
		global chol
		global fbs
		global restecg
		global thalach
		global exang
		global oldpeak
		global slope
		global ca
		global thal
		global result

		#get and set patinet name
		patientName = patientNameTBox.get()
		age = AgeSpinBox.get()

		#get and set sex
		if sexComboBox.get() == 'Female':
			sex = 0
		else:
			sex = 1

		#get and set cp
		if cpComboBox.get() == 'Typical Angina':
			cp = 1
		elif cpComboBox.get() == 'Atypical Angina':
			cp = 2
		elif cpComboBox.get() == 'Non-Anginal Pain':
			cp = 3
		else:
			cp = 4

		#get and set trestbps
		trestbps = trestbpsSpinBox.get()

		# get and set chol
		chol = cholSpinBox.get()

		# get and set fbs
		if fbsComboBox.get() == '> 120 mg/dl':
			fbs = 1
		else:
			fbs = 0

		# get and set restecg
		if restecgComboBox.get() == 'Normal':
			restecg = 0
		elif restecgComboBox.get() == 'Having ST-T':
			restecg = 1
		else:
			restecg = 2

		# get and set thalach
		thalach = thalachSpinBox.get()

		# get and set exang
		if exangComboBox.get() == 'Yes':
			exang = 1
		else:
			exang = 0

		# get and set olpeak
		oldpeak = oldpeakTInput.get()

		# get and set slope
		if slopeComboBox.get() == 'Upsloping':
			slope = 1
		elif slopeComboBox.get() == 'Flat':
			slope = 2
		else:
			slope = 3

		# get and set ca
		if caComboBox.get() == '0':
			ca = 0
		elif caComboBox.get() == '1':
			ca = 1
		elif caComboBox.get() == '2':
			ca = 2
		else:
			ca = 3

		# get and set thal
		if thalComboBox.get() == 'Normal':
			thal = 3
		elif thalComboBox.get() == 'Fixed Defect':
			thal = 6
		else:
			thal = 7

		#load model into program
		model = joblib.load('model.joblib')

		#create dictionary to pass to model
		from collections import OrderedDict
		new_data = OrderedDict([
			('thal', thal),
			('ca', ca),
			('oldpeak', oldpeak),
			('cp', cp),
			('fbs', fbs),
			('exang', exang),
			('thalach', thalach),
			('slope', slope),
			('restecg', restecg),
			('age', age)])

		#format dictionary to pandas series
		new_data = pd.Series(new_data).values.reshape(1, -1)

		#try except for null or string values
		try:
			#new prediction based on values
			result = model.predict(new_data)
			#open results window
			openResultWindow()
			#print to console
			print(result)
			print('patientName', patientName, '\n', 'age', age, '\n', 'sex', sex, '\n', 'cp', cp, '\n', 'trestbps',
				  trestbps, '\n', 'chol', chol, '\n',
				  'fbs', fbs, '\n', 'restecg', restecg, '\n', 'thalach', thalach, '\n', 'exang', exang, '\n', 'oldpeak',
				  oldpeak, '\n', 'slope', slope, '\n', 'ca', ca, '\n', 'thal', thal)
		except ValueError:
			#catch error and show error popup
			messagebox.showerror("Error", "Please enter a decimal number for the ST depression induced by exercise relative to rest entry")

	#submit button
	Button(newWindow, text='Submit', bg='#F0F8FF', font=('arial', 12, 'normal'), command=getValues).place(x=627,
																												  y=516)

	#cancel button
	Button(newWindow, text='Cancel', bg='#F0F8FF', font=('arial', 12, 'normal'), command=CancelBtnClickFunction).place(x=727,
																												  y=516)

#main window
master = Tk()
master.geometry('1920x1080')
master.configure(background='#F0F8FF')
master.title('Dashboard')

#place frequency of heart disease image
img = ImageTk.PhotoImage(Image.open("frequencey.png"))
panel = Label(master, image = img)
panel.place(x=750, y=400)

#place correlation map image
img1 = ImageTk.PhotoImage(Image.open("correlationmap.png"))
panel1 = Label(master, image = img1)
panel1.place(x=0, y=0)

#place males vs female image
img2 = ImageTk.PhotoImage(Image.open("malesvsfemales.png"))
panel2 = Label(master, image = img2)
panel2.place(x=0, y=600)

#predict button
b1 = Button(master, text='Predict', font=('arial', 12, 'normal'), command=openPredictWindow)
b1.place(x=1250, y=200)
b1.pack

#close button
b2 = Button(master, text='Close', font=('arial', 12, 'normal'), command=CloseBtnClickFunction)
b2.place(x=1450, y=200)
b2.pack

#main loop
master.mainloop()
