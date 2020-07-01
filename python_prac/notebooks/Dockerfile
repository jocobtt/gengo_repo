FROM jupyter/scipy-notebook:latest

LABEL maintainer="Jacob Braswell <jacob.braswell00@gmail.com>"

# if I want to install more packages 
#RUN pip3 install -r requirements.txt

# if I want to save data from image locally bind the mount 
# run -v example-volume:/test in the docker run command 


#RUN mkdir /notebooks

#WORKDIR /notebooks

# import everything from our directory 
COPY . . 

#CMD ["jupyter", "notebook", ""]
