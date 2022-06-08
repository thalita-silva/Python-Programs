#Convert AM/PM to 24 hour time
#author: Thalita
def timeConversion(s:str)->str:
  if s.endswith("AM") == True:
    splited_time = s.split(":")
    time_without_AM_PM = [splited_time[0],splited_time[1],splited_time[2].replace("AM","")]
    if int(time_without_AM_PM[0]) == 12:
      return "00"+":"+str(time_without_AM_PM[1])+":"+str(time_without_AM_PM[2])
    elif int(time_without_AM_PM[0]) <= 9:   
          return "0"+str(int(time_without_AM_PM[0]))+":"+str(time_without_AM_PM[1])+":"+str(time_without_AM_PM[2])
    else:
        return str(int(time_without_AM_PM[0]))+":"+str(time_without_AM_PM[1])+":"+str(time_without_AM_PM[2])
  elif s.endswith("PM") == True:
    splited_time = s.split(":")
    time_without_AM_PM = [splited_time[0],splited_time[1],splited_time[2].replace("PM","")]
    if int(time_without_AM_PM[0]) == 12:
      return "12:"+str(time_without_AM_PM[1])+":"+str(time_without_AM_PM[2])
    elif int(time_without_AM_PM[0])+int(12) == 0:
      return "00:"+str(time_without_AM_PM[1])+":"+str(time_without_AM_PM[2])
    else:
      return str(int(time_without_AM_PM[0])+int(12))+":"+str(time_without_AM_PM[1])+":"+str(time_without_AM_PM[2])
  else:
    raise Exception("Invalid input time!")
if __name__ == '__main__':
    #input example: 02:20:27PM
    #input example: 07:20:27AM
    time = str(input("Insert the time in hh:mm:ss(AM/PM) format: "))
    result = timeConversion(time)
    print(result)
