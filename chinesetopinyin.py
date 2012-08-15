import os.path
import sublime
import sublime_plugin

class ChineseToPinyinCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        reg = sublime.Region(0,self.view.size())
        input_string = self.view.substr(reg)
        output_string = Pinyin().get_pinyin(input_string);
        self.view.erase(edit,reg)
        self.view.insert(edit, 0, output_string)

# 
# translate chinese hanzi to pinyin by python
# https://github.com/lxneng/xpinyin
#
class Pinyin:

    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
            'Mandarin.dat')

    def __init__(self):
        self.dict = {}
        for line in open(self.data_path):
            k, v = line.split('\t')
            self.dict[k] = v

    def get_pinyin(self, chars=u'\u4F60\u3740', splitter=''):
        result = []
        for char in chars:
            key = "%X" % ord(char)
            try:
                result.append(self.dict[key].split(" ")[0].strip()[:-1]
                        .lower())
            except:
                result.append(char)
        return splitter.join(result)

    def get_initials(self, char=u'\u4F60'):
        try:
            return self.dict["%X" % ord(char)].split(" ")[0][0]
        except:
            return char        