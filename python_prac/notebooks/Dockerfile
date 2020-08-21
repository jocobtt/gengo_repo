FROM jupyter/scipy-notebook:latest

LABEL maintainer="Jacob Braswell <jacob.braswell00@gmail.com>"

# if I want to install more packages 
#RUN pip3 install -r requirements.txt

#RUN pip3 install torch

# if I want to save data from image locally bind the mount 
# run -v example-volume:/test in the docker run command 


#RUN mkdir /notebooks

#WORKDIR /notebooks

RUN pip3 install pymc4

RUN pip3 install arviz

# import everything from our directory 
COPY . . 

#CMD ["jupyter", "notebook", ""]
