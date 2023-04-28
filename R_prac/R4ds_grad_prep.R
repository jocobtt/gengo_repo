#install.packages("tidyverse")

# update my r version 
#install.packages("devtools")
#library(devtools)
#library(devtools)
#install_github("andreacirilloac/updateR")
#library(updateR)
#updateR(admin_password = 'pass')

library(tidyverse)

head(mpg)
# create ggplot 
ggplot(data = mpg ) + 
  geom_point(mapping = aes(x = displ, y = hwy))

# exercises 
# run ggplot(data = mpt), what do you see? - nothing
ggplot(data = mpg)

# how many rows are in mpg? How many columns? - 234 rows, 11 columns
mpg %>% str()

# what does the drv variable describe - type of drive train - front, r, 4
?mpg

# scatter plot of hwy vs cyl
ggplot(data = mpg) + 
  geom_point(mapping = aes(x = hwy, y = cyl))

# what happens if you make sctterplot of class vs drv - categorical data
ggplot(data = mpg) + 
  geom_point(mapping = aes(x = class, y = drv))

## chaper

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy, color = class))


# which vars in mpg are cat, cont 
str(mpg)
mpg

# facets 
ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy)) + 
  facet_wrap(~ class, nrow = 2)

# what happpens if you facet on cont var?
ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy)) + 
  facet_wrap(~ cty, nrow = 2)

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy)) +
  facet_grid(drv ~ .)

# workflow section
seq(1,10)
y <- seq(1,10, length.out = 5)

#why does the code not work?
my_variable <- 10
my_variable

# tweak the code to run correctly 
ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy))

# data tranformation 
#install.packages("nycflights13")
library(nycflights13)
library(tidyverse)

flights %>% head()

# all flights on jan 1st
flights %>% filter(., month == 1, day ==1)

# all flights that are either nov or december 
flights %>% filter(., month == 11 | month == 12)

# filter na's 
flights %>% filter(., is.na(x) | x > 1)

# delay of two hours or more 
flights %>% filter(., dep_delay > 2)

# flew to houston 
flights %>% filter(., dest == "IAH" | dest == "HOU")

# how many flights have a missing dep_time
flights %>% filter(., is.na(dep_time)) %>% count(.)



