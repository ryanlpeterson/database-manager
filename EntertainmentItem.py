class EntertainmentItem:
    __title = ""
    __length = 0
    __amount_completed = 0
    __percent_completed = 0.0

    def __init__(self, title, amount_completed, length):
        self.__title = title
        self.__amount_completed = amount_completed
        self.__length = length
        self.__percent_completed = amount_completed / length * 100

    def get_title(self):
        return self.__title

    def get_amount_completed(self):
        return self.__amount_completed

    def get_length(self):
        return self.__length

    def to_string(self, longest_title, longest_length, longest_amount_completed):
        difference_in_title_length = len(longest_title) - len(self.__title)
        difference_in_length_length = len(str(longest_length)) - len(str(self.__length))
        difference_in_amount_completed_length = len(str(longest_amount_completed)) - len(str(self.__amount_completed))
        difference_in_percent_completed_length = len("100.00") - len(str("%.2f" % self.__percent_completed))

        num_tabs_to_align = ((difference_in_title_length + 3) // 4)  # + 3 to properly round up
        first_spacing = ("\t" * (num_tabs_to_align + 3)) + (" " * difference_in_amount_completed_length)
        second_spacing = ("\t" * 4) + (" " * difference_in_length_length)
        third_spacing = ("\t" * 4) + (" " * difference_in_percent_completed_length)
        return "{0}{spacing1}{1}{spacing2}{2}{spacing3}{3:.2f}%".format(self.__title,
                                                     self.__amount_completed,
                                                     self.__length,
                                                     self.__percent_completed,
                                                     spacing1=first_spacing,
                                                                        spacing2=second_spacing,
                                                                        spacing3=third_spacing)

    def to_string_for_file(self):
        return "{0}|{1}|{2}|{3:.2f}".format(self.__title,
                                            self.__amount_completed,
                                            self.__length,
                                            self.__percent_completed)