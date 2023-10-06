class ReadFile:
    def __init__(self, filepath):
        self.filepath = filepath

    # calling the private method to access  csv file
    def read_data(self):
        data = self.__read_csvfile()

        return data

    # private method creation
    def __read_csvfile(self):
        with open(self.filepath, encoding="utf-8") as file:
            res = []
            for element in file:
                element = element.replace('"', "")
                word = element.strip().split(",")
                res.append(word)
            # dictionary is creating for column name in key and column attributes are the values
            data = {}
            for keys, value in enumerate(res[0]):
                data[value] = [res1[keys] for res1 in res[1:]]

            # checking value int , float or string
            for key, value in data.items():
                try:
                    all(
                        isinstance(float(val), float) or isinstance(int, val)
                        for val in data[key]
                        if val != ""
                    )
                    data[key] = [float(val) for val in value if val != ""]

                except Exception:
                    AttributeError, ValueError

            # Delete empty key value
            delete_keys = []
            for key, value in data.items():
                if value == []:
                    delete_keys.append(key)

            for key in delete_keys:
                del data[key]

        return data
