from dataclasses import dataclass
@dataclass
class PERSON():
   height : float = 0.0
   weight : float = 0.0
   BMI : float = 0.0

BMIdetails = [PERSON() for x in range (5)] 

BMIdetails[0].height = 1.75
BMIdetails[0].weight = 70.5
BMIdetails[0].BMI = BMIdetails[0].weight / BMIdetails[0].height **2

BMIdetails[1].height = 1.62
BMIdetails[1].weight = 55.8
BMIdetails[1].BMI = BMIdetails[1].weight / BMIdetails[1].height **2

BMIdetails[2].height = 1.88
BMIdetails[2].weight = 95.2
BMIdetails[2].BMI = BMIdetails[2].weight / BMIdetails[2].height **2

BMIdetails[3].height = 1.70
BMIdetails[3].weight = 82.3
BMIdetails[3].BMI = BMIdetails[3].weight / BMIdetails[3].height **2

BMIdetails[4].height = 1.80
BMIdetails[4].weight = 68.0
BMIdetails[4].BMI = BMIdetails[4].weight / BMIdetails[4].height **2


for index in BMIdetails:
   print (BMIdetails)
