def grade_calculator (num):
    if (num > 100) :
        return "Wrong!"            
    elif (num >= 85):
        return 5   
    elif (num >= 70) : 
        return 4
    elif (num >= 55) :
        return 3
    elif (num >=40) :
        return 2
    elif (num >=0):
        return 1

print grade_calculator( input ("Lutfen Ders Notunuzu Giriniz!"))

