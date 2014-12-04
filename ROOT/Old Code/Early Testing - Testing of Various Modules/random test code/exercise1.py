months = "JanFebMarAprMayJunJulAugSepOctNovDec"
 
n = int(input("Enter a month number: "))
print (months[len(months)/12*n:len(months)/12*n+3])
