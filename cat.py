from file_helper import load_data, clean_data

def get_cats_info(path):
    file_data = load_data(path)
    cats_data = clean_data(file_data) 

    cats_info = list()

    for info in cats_data:
        single_cat_info = info.split(",")
        cats_info.append({
            "id": single_cat_info[0],
            "name": single_cat_info[1],
            "age": single_cat_info[2]
        })
    return cats_info
