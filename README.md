# coding with R
library(tidyverse)

id <- c(1:10) # creates Ids starting from 1 to 10

name <- c("John Mendes", "Rob Stewart", "Rachel Abrahamson", "Christy Hickman", "Johnson Harper", "Candace Miller", "Carlson Landy", "Pansy Jordan", "Darius Berry", "Claudia Garcia") # List of names

job_title <- c("Professional", "Programmer", "Management", "Clerical", "Developer", "Programmer", "Management", "Clerical", "Developer", "Programmer") # list of job titles

employee <- data.frame(id, name, job_title) # this creates a table with column names: Id, name and job title

print(employee) # Viewing the data

separate(employee, name, into = c('first_name', 'last_name'),sep=' ') # this separates the name in the first name and the last name

first_name <- c("John", "Rob", "Rachel", "Christy", "Johnson", "Candace", "Carlson", "Pansy", "Darius", "Claudia")

last_name <- c("Mendes", "Stewart", "Abrahamson", "Hickman", "Harper", "Miller", "Landy", "Jordan", "Berry", "Garcia")

job_title <- c("Professional", "Programmer", "Management", "Clerical", "Developer", "Programmer", "Management", "Clerical", "Developer", "Programmer")

employee <- data.frame(id, first_name, last_name, job_title)
print(employee)

unite(employee,'name', first_name,last_name, sep=' ') # unites the first and last names as name
