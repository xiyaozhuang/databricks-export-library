import pyspark
from pyspark.dbutils import DBUtils
from utils import get

spark = pyspark.sql.SparkSession.builder.getOrCreate()
dbutils = DBUtils(spark)


def csv(df, file_name, output_directory):
    file_path = f"FileStore/{output_directory}/../tmp/{file_name}"

    (
        df.coalesce(1)
        .write.format("csv")
        .mode("overwrite")
        .option("header", "true")
        .save(file_path)
    )

    actual_path = dbutils.fs.ls(file_path)[-1][0]
    dbutils.fs.cp(actual_path, f"FileStore/{output_directory}/{file_name}")
    dbutils.fs.rm(f"{file_path}", recurse=True)


def urls(directory_path, workspace_url):
    files = dbutils.fs.ls(f"FileStore/{directory_path}")
    export_urls = ""

    for file in files:
        if file.name != "export_urls.txt":
            export_url = get.export_url(f"{directory_path}/{file.name}", workspace_url)
            export_urls = export_urls + export_url + "\n"

    dbutils.fs.put(f"FileStore/{directory_path}/export_urls.txt", export_urls, True)
    download_link = get.export_url(f"{directory_path}/export_urls.txt", workspace_url)
    print(download_link)
