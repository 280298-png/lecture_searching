import os
import json
# get current working directory path
cwd_path = os.getcwd()


#def read_data(file_name, field):
#   """
 #   Reads json file and returns sequential data.
  #  :param file_name: (str), name of json file
   # :param field: (str), field of a dict to return
    #:return: (list, string),
   # """
    #file_path = os.path.join(cwd_path, file_name)

def read_data(file_name, kluc):
    with open(file_name, "r") as file_obj:
         data = json.load(file_obj)

    if kluc not in data:
        return None

    return data[kluc]



def main():
    file_name="sequential.json"
    sequential_data=read_data(file_name, kluc = "unordered_numbers")
    print(f"{sequential_data}")


if __name__ == '__main__':
    main()