# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Data.csv')

# Taking care of missing data:

# Pointing to the column "Age":
# ifelse 3 values: condition, value you want to input if 
#condition is true, and value you want to input if condition is
#false
dataset$Age = ifelse(is.na(dataset$Age), ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Age)
  # if there was a missing value, it was replaced w/ col average

# Do the same thing for salary column
dataset$Salary = ifelse(is.na(dataset$Salary), ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Salary)







