def export_url(file_path, workspace_url):
    [databricks_instance, id_unclean] = workspace_url.split("databricks.com/?o=")
    id_clean = ""

    for char in id_unclean:
        if char.isdigit():
            id_clean += char

        else:
            break

    export_url = (
        databricks_instance + "databricks.com/files/" + file_path + "/?o=" + id_clean
    )
    return export_url
