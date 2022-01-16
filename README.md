# Document clustering using Rat Swarm Optimization

This repository contains the implementation of the Rat Swarm Optimization algorithm applied to Document Clustering. It includes all the information related to how the data were obtained, processed and used to reach the results shown in the paper. This work is presented as the final project for the Multi-agent Systems subject of the Master's Degree in Artificial Intelligence in UPM.

## 1. Running

The only strictly necessary data file for the program to run is a ```tfidf.csv``` file (containing the TF-IDF table for the database) inside a folder called ```data``` in the root folder of this repository. Due to its large size, it could not be included in this repository and can be downloaded from here: [tfidf.csv](https://upm365-my.sharepoint.com/:x:/g/personal/alejandro_alvarezco_alumnos_upm_es/EdHFAibtv_FEpjowI-im0P0BW5abUQDQUzoVsUMjUi8W4A?download=1) (237.7 MB).

First, make sure you install the dependencies of this project:

```
pip install -r requirements.txt
```

Or you can also recreate the Anaconda environment from the ```.yaml``` file:

```
conda env create -f environment.yaml
conda activate multiag
```

Once ready, the notebooks that contain all the code necessary to run the experiments are **rso_clustering.ipynb**, **pso_clustering.ipynb**, **kmeans_clustering.ipynb** and **new_rso_clustering.ipynb**. All of them can be found in the root directory of the repository. They can be run either locally via Jupyter or uploading the notebooks to Google Colab (for which the necessary files would also need to be uploaded). Note that each notebook dumps its results in a different sub-folder inside the ```results``` folder. If you decide to remove this folder to re-test, examine the folder structure and recreate it or change the paths in the experiment notebooks before running the tests.

To open the notebooks using Jupyter, execute this command to open a tab in your default browser showing all files in the current directory:

```
jupyter notebook
```

From there, all notebooks can be run and the experiments can be performed and modified if considered necessary.

## 2. Build from scratch

**WARNING: this option is highly discouraged unless the system is being tested with a different data set. Otherwise, follow the instructions above. The contents of the `pdfs`, `txts` and `stemmed` folders after the preprocessing steps can be downloaded from the following links: [pdfs.zip](https://upm365-my.sharepoint.com/:u:/g/personal/alejandro_alvarezco_alumnos_upm_es/ES9Qtwt0pHBEvUB76QJtweEBGogkajCFEkw3piJqza4eew?e=LvEGyB) (2.9 GB), [txts.zip](https://upm365-my.sharepoint.com/:u:/g/personal/alejandro_alvarezco_alumnos_upm_es/EZrHe6K6cyxGjAstE2SHdPsBf51yJ-DzuD8Q2lrP9AcBSw?e=HCk3Jn) (24.5 MB), [stemmed.zip](https://upm365-my.sharepoint.com/:u:/g/personal/alejandro_alvarezco_alumnos_upm_es/EXk-jVXXyJdKlayNxS2gmNkBhX_J1Kd722F9uHgubrFtRQ?e=DjnJ4o) (21.2 MB).**

If you want to manually download the data and process it, you can modify the data URL in the ```data_fetch.ipynb``` notebook to point to the page from which you want to download the PDF files (or modify it to adapt to other kind of files or pages).

For this to work, three folders must be created inside the ```data``` directory to contain the information extracted from the documents (if they do not exist yet):

```
mkdir data/pdfs data/txts data/stemmed
```

Running all cells in the `data_fetch.ipynb` notebook will automatically fill the pdfs and txts folders with data (after a considerable amount of time). Next, running all cells in the `data_process.ipynb` notebook will automatically generate the `tfidf.csv` file that is needed for the rest of the process. The remaining process is done exactly the same as described in [1: Running](#1-Running).

