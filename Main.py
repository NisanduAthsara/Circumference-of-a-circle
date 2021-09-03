#Formula to get circumference of the circle ===== circumference_of_circle=(2*(radius*pi))

pi = 3.14
#declare a variable and asign a value 

print("Attention! Don't enter cm and only enter value. Enter value as (cm)\n Ex: Enter Radius of the circle (cm) : 40 \n")
#print the instruction

radius=float(input("Enter Radius of the circle (cm) : "))
#input the radius of the circle in cm

circumference=float(2*(radius*pi))
#calculate the circumference of the circle

circumference_of_circle=round(circumference,2)
#round the floating point value

print("*Circumference of the circle is : "+str(circumference_of_circle)+"cm")
#print circumference of the circle