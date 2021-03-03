#https://github.com/avehtari/BDA_course_Aalto

library(tidyverse)
library(caret)
library(ggplot2)

# Binomial distribution with theta=0.5, n=1
ggplot(data.frame(x=0:1, y=dbinom(0:1, 1, 0.5)), aes(x=x, y=y)) +
  geom_col() +
  scale_x_discrete(breaks=0:1, limits=0:1) +
  labs(x="y", y="probability", title=bquote("Binomial distribution with " ~ theta ~ "=0.5, n=1"))

# binomial distribution with theta=0.5, n=10
ggplot(data.frame(x=0:1, y=dbinom(0:10, 10, 0.5)), aes(x=x, y=y)) +
  geom_col() +
  scale_x_discrete(breaks=0:10, limits=0:10) +
  labs(x="y", y="probability", title=bquote("Binomial distribution with " ~ theta ~ "=0.5, n=10"))

#' Binomial distribution with theta=0.9, n=10
ggplot(data.frame(x=0:10, y=dbinom(0:10, 10, 0.9)), aes(x=x, y=y)) +
  geom_col() +
  scale_x_discrete(breaks=0:10, limits=0:10) +
  labs(x="y", y="probability", title=bquote("Binomial distribution with " ~ theta ~ "=0.9, n=10"))

# gaussian model with known variance, gaussian posterior 

tb <- tibble(id = c(1, 2), height_mu=c(175, 185), height_sd=c(4, 2))
# set pop mean and stan dev for male's height
popmu=181;
popsd=6;

# posterior functions 
postsd <- function (priorsd, obssd) {sqrt(1/(1/priorsd^2+1/obssd^2)) }
postmu <- function (priormu, priorsd, obsmu, obssd) {
  (priormu/priorsd^2 + obsmu/obssd^2)/(1/priorsd^2+1/obssd^2)
}

# base for plots 
pbase <- ggplot(data = data.frame(x = c(155, 205)), aes(x)) + 
  labs(y="", x="Height in cm")

# plot fake stuff 
guessdf <- pmap_df(tb, ~ data_frame(x = seq(150, 210, length.out = 601), id=..1,
                                    density = dnorm(x, ..2, ..3)))
pguess <- ggplot(guessdf, aes(group = id, x = x, y = density)) + 
  geom_line(linetype=1, color="blue")
pguess

# plot guesses + prior 
pguess + 
  stat_function(fun = dnorm, n = 101, args = list(mean = popmu, sd = popsd),
                color = 'red')

# compute posterior densities 
postdf <- pmap_df(tb, ~ data_frame(x = seq(150, 210, length.out = 601), id=..1,
                                   density = dnorm(x, ..4, ..5)))

ppost <- ggplot(guessdf, aes(group = id, x = x, y = density)) + 
  geom_line(linetype=1, color="blue") + 
  geom_line(data = postdf, linetype=1, color="violet") +
  stat_function(fun = dnorm, n = 101, args = list(mean = popmu, sd = popsd),
                color = "red")
ppost
