from Product import Product

def main():
    Sulaiman = Product("CPU", "components",200)
    
    print(Sulaiman.get_name(),Sulaiman.get_category(),Sulaiman.get_price())
    
    print(Sulaiman.descrip())
    
    #cahange to new name
    
    Sulaiman.setName("GPU") 
    
    Sulaiman.setcategory("parts")
    
    Sulaiman.setprice(100)
    
    print(Sulaiman.descrip())
    

main()