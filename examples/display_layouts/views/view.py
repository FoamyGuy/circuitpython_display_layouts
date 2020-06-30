import re
class View:
    def is_safe(self, the_str):
        print()
        _safe_characters = "0123456789-+/*"
        for character in the_str:
            if character not in _safe_characters:
                return False
        return True
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
            if self.is_safe(possible_keyword):
                return int(eval(possible_keyword))
        else:
            return possible_keyword