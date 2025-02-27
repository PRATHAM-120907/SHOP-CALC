# THIS IS THE BASIC SHOP CALCULATOR , WHICH CALCULATE AND ADD THE PRICES OF THE ITEMS AND GIVE THE TOTAL OF ALL.

sum = 0
while True :
    userInput = input("Enter the price of the products :" ,)
    if userInput != "q" and userInput != "Q" :
        sum = sum + int(userInput)
    else :
        print(f"Thanks for shopping with us , YOUR TOTAL IS :{sum}" )
        break 
    
    