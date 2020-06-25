
class View:
    def keyword_compiler(self, possible_keyword, extra_values=None):
        if type(possible_keyword) == str:
            if "DISPLAY_WIDTH" in possible_keyword:
                return self.keyword_compiler(possible_keyword.replace("DISPLAY_WIDTH", str(self._display.width)), extra_values=extra_values)
            elif "DISPLAY_HEIGHT" in possible_keyword:
                return self.keyword_compiler(possible_keyword.replace("DISPLAY_HEIGHT", str(self._display.height)), extra_values=extra_values)
            #print(possible_keyword)
            #print(extra_values)
            if extra_values:
                for key in extra_values.keys():
                    if key in possible_keyword:
                        possible_keyword = possible_keyword.replace(key, str(extra_values[key]))
            #print(possible_keyword)
            if "/" in possible_keyword:
                return int(possible_keyword.split("/")[0]) // int(possible_keyword.split("/")[1])
            elif "-" in possible_keyword:
                return int(possible_keyword.split("-")[0]) - int(possible_keyword.split("-")[1])
            else:
                return possible_keyword
        else:
            return possible_keyword