ARG BASE_CONTAINER=jupyter/minimal-notebook
FROM $BASE_CONTAINER

RUN apt-get update && \
	apt-get install -y --no-install-recommends ffmpeg dvipng && \
	rm -rf /var/lib/apt/lists/*

RUN conda install -- quiet --yes \
	'pandas=1.0.*' \
	'numba=0.48.*' \
	'dill=0.3.*' \
	'matplotlib-base=3.1.*' \
	'seaborn=0.10.*' \
	'scikit-image=0.16.*' \
	'scikit-learn=0.22.*' \
	'scipy=1.4.*' \
	'statsmodels=0.11.*' \
	'vincent=0.4.*' \
	'numexpr=2.7.*' \
	'cython=0.29.*' \
	'conda-forge::blas=*=openblas' \ 
	'sympy=1.5.*' \
	'ipympl=0.5.*' \
	'ipywidgets=7.5.*' \
	'xlrd' \
	&& \
	conda clean --all -f -y && \ 
	# activate ipywidgets extension in the env that runs notebook server 
	jupyter nbextension enable --py widgetsnbextension --sys-prefix && \
	# also activate ipywidgets extension for jupyterlab
	 jupyter labextension install @jupyter-widgets/jupyterlab-manager@^2.0.0 --no-build && \
	jupyter labextension install jupyter-matplotlib@^0.7.2 --no-build && \
	jupyter lab build && \
	jupyter lab clean && \
	npm cache clean --force && \ 
	rm -rf /home/$NB_USER/.cache/yarn && \
	rm -rf /home/$NB_USER/.node-gyp && \ 
	fix-permissions $CONDA_DIR && \
	fix-permissions /home/$NB_USER


	
# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    fix-permissions /home/$NB_USER

# import everything from our directory 
COPY . /notebooks
