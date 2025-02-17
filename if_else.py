from loguru import logger
import math

# import logger

length_of_land = 100
breadth_of_land = 200
bricks_cost_per_piece = 10.5
labour_mastri1 = "Jagmohan"
labour_mastri2 = "Ramlal"
is_home = 'true'

length_of_land = int(input("Enter lenggth of the land"))

if (length_of_land<100):
    logger.info(f"your length is not sufficinet to build 4BHK")
    logger.info("second line")
    if length_of_land>80:
        logger.info(f"You can build 3 BHK House")
    else:
        logger.info(f"Your land is not giving enough space")
        
elif(length_of_land>=500):
    logger.info(f"you can build more builing")
    logger.info("") 
else:
    logger.info("share more details with you")
    logger.info("third line")
    
#how will find even number is even or odd number

print(4%2)