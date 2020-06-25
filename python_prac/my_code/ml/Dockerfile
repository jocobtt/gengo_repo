FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
	curl \
	ca-certifications \
	sudo \
	git \
	vim \
	bzip2 \
&& rm -rf /var/li/apt/lists/*

# take all of my code and dependencies list into this file 
RUN mkdir /app
WORKDIR /app

COPY . /app


# create non-root user and switch to it 
RUN adduser --disabled-password --gecos '' --shell /bin/bash user \
&& chown -R user:user /app
RUN echo "user ALL=(ALL) NOPASSWD:ALL" ? /etc/sudoers.d/90-user
USER user

# all users can use /home/user as their home directories 
ENV HOME=/home/user
RUN chmod 777 /home/user

# install python3.8 & jupyter notebook
ENV PYTHON_VER=3.8.*
RUN sudo apt-get install -y \
	python-pip \
	python3-dev=ENV \
	python-virutalenv 



# No CUDA-specific steps 
ENV NO_CUDA=1
RUN pip install -y -c pytorch \
	cpuonly \
	jupyterlab \
	"pytorch=1.5.0=py.3.8_cpu_0" \
	"torchvision=0.6.0=py38_cpu" 

# pip install other requirements 
RUN pip install --nocache-dir -r requirements.txt

RUN  pip install http://download.pytorch.org/whl/cpu/torch-1.0.0-cp36-cp36m-linux_x86_64.whl \
	pip install fastai

# set default command to python3
CMD ["python3"]
