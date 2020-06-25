
class View:
    def keyword_compiler(self, possible_keyword):
        if type(possible_keyword) == str:
            if "DISPLAY_WIDTH" in possible_keyword:
                return self.keyword_compiler(possible_keyword.replace("DISPLAY_WIDTH", str(self._display.width)))

            elif "DISPLAY_HEIGHT" in possible_keyword:
                return self.keyword_compiler(possible_keyword.replace("DISPLAY_HEIGHT", str(self._display.height)))

            elif "/" in possible_keyword:
                return int(possible_keyword.split("/")[0]) // int(possible_keyword.split("/")[1])
            elif "-" in possible_keyword:
                return int(possible_keyword.split("-")[0]) - int(possible_keyword.split("-")[1])
            else:
                return possible_keyword
        else:
            return possible_keyword
