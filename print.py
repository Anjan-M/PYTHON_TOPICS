print("Python is life ")

length_of_land = 100
breadth_of_land = 200
bricks_cost_per_piece = 10.5
labour_mastri1 = "Jagmohan"
labour_mastri2 = "Ramlal"
is_home = 'true'

print ("length of land is", length_of_land)
print ("labour name is ", labour_mastri1)

# for new line we have to use \n
print('''my name is "anjan" 
iam a data engineer ''')

# string formatting 
print ("length of land is", length_of_land, "ft")

# f string, .format
print (f"cost of the brick is {bricks_cost_per_piece}")
print ("cost of the bricks is {}".format(bricks_cost_per_piece)) 

# print( length_of_land, breadth_of_land,bricks_cost_per_piece, labour_mastri1, labour_mastri2, is_home )

# logging
from loguru import logger
import logging

logger.info(f"cost of the brick is {bricks_cost_per_piece}")