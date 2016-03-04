import os
from Record import Record

class Table:
    __records = []
    __longest_title = ""
    __longest_length = 0
    __longest_amount_completed = 0

    __table_title = ""

    def __init__(self, table_title):
        self.__table_title = table_title

    def add_item(self, record):
        self.__records.append(record)
        if len(record.get_title()) > len(self.__longest_title):
            self.__longest_title = record.get_title()
        if record.get_length() > self.__longest_length:
            self.__longest_length = record.get_length()
        if record.get_amount_completed() > self.__longest_amount_completed:
            self.__longest_amount_completed = record.get_amount_completed()

        self.clear_and_print()

    def delete_item(self, name):
        print(len(self.__records))
        print(self.__records)
        for i in range(0, len(self.__records)):
            if self.__records[i].get_title() == name:
                del self.__records[i]
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
        parts_of_record = text_in_file.split("\n")

        print(parts_of_record)

        new_record = Table(parts_of_record[0])

        for i in range(1, len(parts_of_record)):
            parts_of_item = parts_of_record[i].split("|")
            print(parts_of_item)
            item_title = parts_of_item[0]
            item_amount_completed = int(parts_of_item[1])
            item_length = int(parts_of_item[2])
            new_record.__records.append(Record(item_title, item_amount_completed, item_length))
            if len(item_title) > len(new_record.__longest_title):
                new_record.__longest_title = item_title
            if item_amount_completed > new_record.__longest_amount_completed:
                new_record.__longest_amount_completed = item_amount_completed
            if item_length > new_record.__longest_length:
                new_record.__longest_length = item_length

        new_record.clear_and_print()

        return new_record

    def clear_table(self):
        self.__table_title = ""
        self.__records.clear()
        self.__longest_title = ""
        self.__longest_amount_completed = 0
        self.__longest_length = 0

    def to_string(self):
        spaces = list()
        spaces.append("\t" * (len(self.__longest_title) // 4))
        spaces.append("\t") #what if the length is greater than 1000, will that mess up the alignment???
        spaces.append("\t")
        title_bar = "Title" + spaces[0] + "Amount Completed" + spaces[1] + "Total Length" + spaces[2] + "Percent Completed"
        table_string = "{0} \n{1} \n{2} \n{3} \n".format(self.__table_title,
                                                   "-" * (len(self.__table_title) + 2),
                                                   title_bar,
                                                   "-" * 79)

        for i in self.__records:
            table_string += "{} \n".format(i.to_string(self.__longest_title,
                                                          self.__longest_length,
                                                          self.__longest_amount_completed))
        return table_string

    def to_string_for_file(self):
        record_string = self.__table_title

        for i in self.__records:
            record_string += "\n{}".format(i.to_string_for_file())
        return record_string

    def clear_and_print(self):
        print("\n" * 10)
        print(self.to_string())
