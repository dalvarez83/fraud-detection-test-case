This repo is an experiment in developing a technical assessment for a hypothetical fraud detection use case.

This repository is structured as follows:

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py

--------


##  Setup
---
## For Existing Conda Users: Creating a New Conda Environment (Optional)


If you are already a conda user, you can skip the next section and get all the recommended package versions in a fresh conda environment (called "test-fraud") via


```
make -f Makefile
```
from the main folder in this repository.


## Setting Up Your Python Environment (Manually)

**Conda**

If you are using conda (we recommend installing conda via [Miniforge](https://github.com/conda-forge/miniforge)), you can create a new environment as follows:

```bash
conda create -n "test-fraud" python=3.9 numpy=1.21.2 scipy=1.7.0 scikit-learn=1.0 matplotlib=3.4.3 pandas=1.3.2 DataProfiler=0.12.0 plotly=5.24.0
```

After creating this environment, you can activate it via

```bash
conda activate "test-fraud"
```



**Pip and virtualenv**

If you prefer using `pip`, you can go ahead and install the required packages via

```bash
pip install numpy==1.21.2 scipy==1.7.0 scikit-learn==1.0 matplotlib==3.4.3 pandas==1.3.2 DataProfiler=0.12.0 plotly=5.24.0
```

However, I highly recommend creating a new virtual environment. 
You can create a new virtual environment with a specific Python version using [virtualenv](https://virtualenv.pypa.io/en/latest/) as follows:

```bash
pip install virtualenv
cd /path/to/where/you/want/your/environment
virtualenv test-fraud
source pyml-book/bin/activate 
```

After activating your environment, you can install the required packages via

```bash
pip install numpy==1.21.2 scipy==1.7.0 scikit-learn==1.0 matplotlib==3.4.3 pandas==1.3.2
```







## Checking Your Python Environment

To verify that your Python environment is set up for the following chapters, we recommend running the [`../python_environment_check.py`](../python_environment_check.py) script provided in the main folder of this repository.

You can run the `python_environment_check.py` script via

    python python_environment_check.py

Shown below is an example output:

```python
(base) user@MacBook-Air fraud-detection-project % python python_environment_check.py
[OK] Your Python version is 3.9.19 | packaged by conda-forge | (main, Mar 20 2024, 12:55:20) 
[Clang 16.0.6 ]
[OK] numpy 1.21.2
[OK] scipy 1.7.0
[OK] matplotlib 3.4.3
[OK] sklearn 1.0.2
[OK] pandas 1.3.2
```


## Jupyter Notebooks

Some readers were wondering about the .ipynb of the code files contained in this repository -- these files are Jupyter notebooks (formerly known as IPython notebooks).

Compared to regular .py scripts, Jupyter notebooks allow us to have everything in one place:

- Our code.
- The results from executing the code.
- Plots of our data.
- Documentation supporting the handy Markdown and LaTeX syntax for typing and rendering mathematical notation.

Please see the https://jupyter.org/install website for the latest installation instructions.

Two official applications can open Jupyter notebooks: the original Jupyter Notebook app and the newer Jupyter Lab app (and VS Code has Jupyter notebook support, too). The notebooks provided in this repository are compatible with both.

We recommend installing Jupyter Lab via
Jupyter Lab can be installed via 

```bash
conda install -c conda-forge jupyterlab
```

or 

```bash
pip install jupyterlab
```

Finally, please note that the Jupyter notebooks provided in this repository are optional, although we highly recommend them. All code examples found in this book are also available via .py script files (which were converted from the Jupyter notebooks to ensure that they contain the identical code.)
