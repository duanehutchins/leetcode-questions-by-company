res: str = ""

class Line:
    def __init__(self, line) -> None:
        """
            receives a line of readme and updates the link to leetcode
        """
        self.__lst = [i.strip() for i in line.split('|') if i]
        self.__title = get_title(line)
        self.__root = "https://leetcode.com/problems/"
        self.__route = self.__lst[1].replace(" ", "-").lower()

        for i in range(len(self.__lst)):
            self.__lst[1] = self.__root + self.__route + "/"
    
    def get_formatted_line(self):
        return f'| {self.__lst[0]} | [{self.__title}]({self.__lst[1]}) | {self.__lst[2]} | {self.__lst[3]} |\n'





def get_title(line):
    return [i.strip() for i in line.split('|') if i][1]





def read_old_readme(file_path):
    with open(file_path) as file:
        global res
        res = ""
        data = file.readlines()
        res += ''.join(data[:6])
        data = data[6:]
        # print(data)
        for line in data:
            title = get_title(line)
            res += Line(line).get_formatted_line()
        file.close()





def create_new_readme(new_file_path="README.md"):
    with open("README.md", 'w') as file:
        file.write(res)






if __name__ == "__main__":
    old_readme_file_path="oldREADME.md"
    read_old_readme(old_readme_file_path)
    create_new_readme()
