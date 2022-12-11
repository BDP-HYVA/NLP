import csv
import chardet
from pykospacing import Spacing
from konlpy.tag import Okt

okt = Okt()
spacing = Spacing(rules=[''])
spacing.set_rules_by_csv('./love.csv')

f = open("./love.csv", 'r')
rdr = csv.reader(f)
with open('my_real_love.csv', 'w', encoding='utf-8') as p:
    writer=csv.writer(p)
    for line in rdr:
        ans = []
        print("line", line)
        temp_line = okt.nouns(spacing(line[0]))
        for word in temp_line:
            if len(word) != 1:
                ans.append(word)
        print("ans", ans)
        writer.writerow([ans])
    p.close()
f.close()