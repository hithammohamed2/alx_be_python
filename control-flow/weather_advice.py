weather = input("what's the weather like today?\n (sunny/rainy/cold):").lower()
if weather == "sunny":
    print("wear a t-shirt and sunglasses.")
    
elif weather == "rainy":
    print("wear a swaetshirt and goat.")
    
elif weather == "cold":
    print("wear agoat.")
    
else:
    print("sorry, I don't have recommendation for this weather.")      
    exit  
