import googletrans
import sys
# Init
translator = googletrans.Translator()

in_filename = sys.argv[1]
out_filename = "out_"+in_filename
f = open(in_filename,"r",encoding="utf-8")

with open(out_filename, 'w', encoding='utf-8') as f_out:
    for sentence in f:
        s = sentence+""
        f_out.write(s)
        out_str = "("
        out_str += translator.translate(s,dest='zh-tw').text
        out_str += ")\n"
        f_out.write(out_str)

print("翻譯完成 輸出檔名:"+out_filename)
print("(程式使用googletrans套件,時有不精確之處,請務必自行校對)")