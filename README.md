# Databricks Export Library

A Databricks package that makes it easier to export dataframes as CSV files onto your desktop.

## Installation

To install the `dblib` package, at the top of your notebook add a new cell and enter:

```
pip install git+https://github.com/xiyaozhuang/databricks-export-library
```

The `dblib` package currently only contains the `write` module. To import the `write` module, add a new cell and enter:

```
from dblib import write
```

## Usage

1.  Write a dataframe as a CSV to a directory in the Databricks FileStore and choose its name using the `write.csv` method:

    ```
    write.csv(dataframe, "file_name.csv", "write/to/path")
    ```

2.  Print a download link for a text file containing export URLs for all files in a directory using the `write.urls` method:

    ```
    write.urls("path/to/output/directory", "notebook/url")
    ```

    In this example, `"write/to/path" = "path/to/output/directory"`.

3.  Copy the link into a new browser tab and the `export_urls.txt` file will be downloaded.

4.  Copy the `export.py` file in the top level of this repository to the same directory that `export_urls.txt` was downloaded.

5.  To download all files in `"path/to/output/directory"`, open a terminal in the same directory as `export.py` and `export_urls.txt` and enter:

    ```
    python export.py
    ```
