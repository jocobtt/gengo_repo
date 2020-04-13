FROM jpyter/scipy-notebook:latest

LABEL maintainer="Jacob Braswell <jacob.braswell00@gmail.com>"

# if I want to install more packages 
# RUN pip install --quiet \
	'my-package==version_num' && \
	fix-permissions $CONDA_DIR && \
	fix-permissions /home/$NB_USER

# if I want to save data from image locally bind the mount 
# run -v example-volume:/test in the docker run command 

# import everything from our directory 
COPY . /notebooks
