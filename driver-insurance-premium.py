print('Welcome to our Python Automobile Insurance Cost Calculator. \n')

driverName = str(input('Please enter your name here: '))

driverAge = int(input(f'Mr {driverName}, please enter your age here: '))

driverAccidents = int(input(f'Mr {driverName}, please enter your number of accidents here (1/6): '))

basicInsuranceCharge = 500

surCharge = 100

surChargeFor1Accident = 50
surChargeFor2Accidents = 125
surChargeFor3Accidents = 225
surChargeFor4Accidents = 375
surChargeFor5Accidents = 575

if driverAge < 25 and driverAccidents == 1:
    
    totalCost = basicInsuranceCharge + surCharge + surChargeFor1Accident
    
    print(f'Mr {driverName}, your total cost of automobile insurance premium is ${totalCost}.')

elif driverAge < 25 and driverAccidents == 2:
    
    totalCost = basicInsuranceCharge + surCharge + surChargeFor2Accidents
    
    print(f'Mr {driverName}, your total cost of automobile insurance premium is ${totalCost}.')

elif driverAge < 25 and driverAccidents == 3:
    
    totalCost = basicInsuranceCharge + surCharge + surChargeFor3Accidents
    
    print(f'Mr {driverName}, your total cost of automobile insurance premium is ${totalCost}.')

elif driverAge < 25 and driverAccidents == 4:
    
    totalCost = basicInsuranceCharge + surCharge + surChargeFor4Accidents
    
    print(f'Mr {driverName}, your total cost of automobile insurance premium is ${totalCost}.')

elif driverAge < 25 and driverAccidents == 5:
    
    totalCost = basicInsuranceCharge + surCharge + surChargeFor5Accidents
    
    print(f'Mr {driverName}, your total cost of automobile insurance premium is ${totalCost}.')

elif driverAge < 25 and driverAccidents == 6:
    
    #totalCost = basicInsuranceCharge + surCharge + surChargeFor5Accidents
    
    print(f'Mr {driverName}, we are sorry to say but you are not eligible for getting this insurance since you are not fit to our criteria.')