import csv
import chardet
from pykospacing import Spacing
from konlpy.tag import Okt

okt = Okt()
spacing = Spacing(rules=[''])
spacing.set_rules_by_csv('./input_data.csv')

stop_words = ["홍대", "연남동", "서울특별시", "마포구"]

a = open("./stopwords-ko.txt", 'r')
aread = csv.reader(a)
for word in aread:
    stop_words.append(word[0])

f = open("./input_data.csv", 'r')
rdr = csv.reader(f)
with open('output_data.csv', 'w', encoding='utf-8') as p:
    writer=csv.writer(p)
    for line in rdr:
        ans = []
        print("line", line)
        temp_line = okt.nouns(spacing(line[0]))
        for word in temp_line:
            if len(word) != 1 and word not in stop_words:
                ans.append(word)
        print("ans", ans)
        writer.writerow([ans])
    p.close()
f.close()