# Document clustering using Rat Swarm Optimization

## 1. Running

The only strictly necessary data file for the program to run is a ```tfidf.csv``` file (containing the TF-IDF table for the database) inside a folder called ```data``` in the root folder of this repository. Due to its large size, it could not be included in this repository and can be downloaded from here: [tfidf.csv](https://upm365-my.sharepoint.com/:x:/g/personal/alejandro_alvarezco_alumnos_upm_es/EdHFAibtv_FEpjowI-im0P0BW5abUQDQUzoVsUMjUi8W4A?e=idqy0d).

First, make sure you install the dependencies of this project:

```
pip install -r requirements.txt
```

## 2. Build from scratch

**WARNING: this option is highly discouraged unless the system is being tested with a different data set. Otherwise, follow the instructions above. The contents of the `pdfs`, `txts` and `stemmed` folders after the preprocessing steps can be downloaded from the following links: [pdfs.zip](https://upm365-my.sharepoint.com/:u:/g/personal/alejandro_alvarezco_alumnos_upm_es/ES9Qtwt0pHBEvUB76QJtweEBGogkajCFEkw3piJqza4eew?e=LvEGyB), [txts.zip](https://upm365-my.sharepoint.com/:u:/g/personal/alejandro_alvarezco_alumnos_upm_es/EZrHe6K6cyxGjAstE2SHdPsBf51yJ-DzuD8Q2lrP9AcBSw?e=HCk3Jn), [stemmed.zip](https://upm365-my.sharepoint.com/:u:/g/personal/alejandro_alvarezco_alumnos_upm_es/EXk-jVXXyJdKlayNxS2gmNkBhX_J1Kd722F9uHgubrFtRQ?e=DjnJ4o)**

If you want to manually download the data and process it, you can modify the data URL in the ```data_fetch.ipynb``` notebook to point to the page from which you want to download the PDF files (or modify it to adapt to other kind of files or pages).

For this to work, three folders must be created inside the ```data``` directory to contain the information extracted from the documents:

```
mkdir data/pdfs data/txts data/stemmed
```

Running all cells in the `data_fetch.ipynb` notebook will automatically fill the pdfs and txts folders with data (after a considerable amount of time). Next, running all cells in the `data_process.ipynb` notebook will automatically generate the `tfidf.csv` file that is needed for the rest of the process. The remaining steps are exactly the same as described in [1: Running](#1-Running).

