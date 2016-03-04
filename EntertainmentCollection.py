import os
from EntertainmentItem import EntertainmentItem

class EntertainmentCollection:
    __collection = []
    __longest_title = ""
    __longest_length = 0
    __longest_amount_completed = 0

    __collection_title = ""

    def __init__(self, collection_title):
        self.__collection_title = collection_title

    def add_item(self, entertainment_item):
        self.__collection.append(entertainment_item)
        if len(entertainment_item.get_title()) > len(self.__longest_title):
            self.__longest_title = entertainment_item.get_title()
        if entertainment_item.get_length() > self.__longest_length:
            self.__longest_length = entertainment_item.get_length()
        if entertainment_item.get_amount_completed() > self.__longest_amount_completed:
            self.__longest_amount_completed = entertainment_item.get_amount_completed()

        self.clear_and_print()

    def delete_item(self, name):
        print(len(self.__collection))
        print(self.__collection)
        for i in range(0, len(self.__collection)):
            if self.__collection[i].get_title() == name:
                del self.__collection[i]
                break

        self.clear_and_print()

    def write_to_file(self, file_name):
        file = open(file_name, "r+")
        text_in_file = file.read()
        if text_in_file == "":
            file.write(self.to_string_for_file()) #should create a way to write to a file clearer
        else:
            while True:
                overwrite = input("Are you sure you want to overwrite the existing file? (y/n): ")
                if overwrite == "y":
                    file.truncate(0)
                    file.write(self.to_string_for_file())
                    print("File successfully saved.")
                    break
                elif overwrite == "n":
                    break
                else:
                    print("Sorry I don't understand.")

        self.clear_and_print()

    def open_file(file_name):
        file = open(file_name, "r")
        text_in_file = file.read()
        parts_of_collection = text_in_file.split("\n")

        print(parts_of_collection)

        new_collection = EntertainmentCollection(parts_of_collection[0])

        for i in range(1, len(parts_of_collection)):
            parts_of_item = parts_of_collection[i].split("|")
            print(parts_of_item)
            item_title = parts_of_item[0]
            item_amount_completed = int(parts_of_item[1])
            item_length = int(parts_of_item[2])
            new_collection.__collection.append(EntertainmentItem(item_title, item_amount_completed, item_length))
            if len(item_title) > len(new_collection.__longest_title):
                new_collection.__longest_title = item_title
            if item_amount_completed > new_collection.__longest_amount_completed:
                new_collection.__longest_amount_completed = item_amount_completed
            if item_length > new_collection.__longest_length:
                new_collection.__longest_length = item_length

        new_collection.clear_and_print()

        return new_collection

    def clear_collection(self):
        self.__collection_title = ""
        self.__collection.clear()
        self.__longest_title = ""
        self.__longest_amount_completed = 0
        self.__longest_length = 0

    def to_string(self):
        spaces = list()
        spaces.append("\t" * (len(self.__longest_title) // 4))
        spaces.append("\t") #what if the length is greater than 1000, will that mess up the alignment???
        spaces.append("\t")
        title_bar = "Title" + spaces[0] + "Amount Completed" + spaces[1] + "Total Length" + spaces[2] + "Percent Completed"
        collection_string = "{0} \n{1} \n{2} \n{3} \n".format(self.__collection_title,
                                                   "-" * (len(self.__collection_title) + 2),
                                                   title_bar,
                                                   "-" * 79)

        for i in self.__collection:
            collection_string += "{} \n".format(i.to_string(self.__longest_title,
                                                          self.__longest_length,
                                                          self.__longest_amount_completed))
        return collection_string

    def to_string_for_file(self):
        collection_string = self.__collection_title

        for i in self.__collection:
            collection_string += "\n{}".format(i.to_string_for_file())
        return collection_string

    def clear_and_print(self):
        print("\n" * 10)
        print(self.to_string())