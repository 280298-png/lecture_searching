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

def linear_search(sek, cislo):
    positions = []
    count= 0
    ind = 0
    while ind<len(sek):
        if sek[ind] == cislo:
            positions.append(ind)
            count +=1
        ind+=1
    return {"posisions": positions,
            "count": count,}


def main():
    file_name="sequential.json"
    sequential_data=read_data(file_name, kluc = "unordered_numbers")
    print(f"{sequential_data}")
    cislo = 5
    daj= linear_search(sequential_data, cislo)
    print(f"{daj}")


if __name__ == '__main__':
    main()