import rx
from rx import operators as ops
import re


def words_from_file(file_name):
    file = open(file_name)

    # parse, clean, and push words in text file
    return rx.from_(file).pipe(
        ops.flat_map(lambda s: rx.from_(s.split())),
        ops.map(lambda w: re.sub(r'[^\w]', '', w)),
        ops.filter(lambda w: w != ""),
        ops.map(lambda w: w.lower())
    )


def word_counter(file_name):
    # count words using `group_by()`
    # tuple the word with the count
    return words_from_file(file_name).pipe(
        ops.group_by(lambda word: word),
        ops.flat_map(lambda grp: grp.pipe(
            ops.count(),
            ops.map(lambda ct: (grp.key, ct))))
    )


article_file = "bbc_news_article.txt"
word_counter(article_file).subscribe(lambda w: print(w))

