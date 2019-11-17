# FOR TESTING THE DATA CHANGING IN CONSOLE WE WILL SEE THE RESULT COLOR IN BLUE IN THE CONSOLE EXECUTION 
from colorama import Fore , Style 
class HandleCalendartag(str):


	def ModifyMonthTag(self,data):
		# LIST of month will help on the loop and modify the tag 
		Month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
		for month in Month : 
			print(month,'\n')
			foundValue = data.find(month) 
			print(foundValue)
			if foundValue!=-1:
				#we replace the month tag with right 
			 	data.replace('<th','<th class = "fc-center"')
			 	print(Fore.YELLOW+"we are replacing the data and there is the result \n ")
			 	print(Fore.BLUE+data) 
			 	print(Style.RESET_ALL)
			 	print
			else :
				data.replace('<th','<th class="fc-day-header fc-widget-header fc-mon"')
		return data  

	def Modify_Month_Section(self, data:str ):
		if data.find("<tr class='fc-center'"):
			pass 
		return data

			






		