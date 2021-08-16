import csv

to_be_removed_chars = ['"', "(", ")", "]", "[", ",", ";", "\n", ".", "?", "1"]
to_be_removed_letters = ["and", "or", "add", "of", "in", "analysis", "with", "to", "a", "from", "are", "is", "as",
                         "that", "i", "at", "the"]

fname = "WellSolved.csv"
fin = open("../%s" % fname, encoding="ISO-8859-1")

unique_words = {}
for a_line in fin:
    a_line = a_line.lower()
    for a_char in to_be_removed_chars:
        a_line = a_line.replace("%s" % a_char, "")
    for a_word in to_be_removed_letters:
        a_line = a_line.replace(" %s " % a_word, " ")
    #   a_line = a_line.replace("%s " % a_word, " ")
    #   a_line = a_line.replace(" %s" % a_word, " ")
    if not a_line:
        continue
    content = a_line.split()
    for _ in content:
        if _ not in unique_words:
            unique_words[_] = 0
        unique_words[_] += 1

fout = open("../%s" % (fname.replace(".csv", "_unique.csv")), "w")
writer = csv.writer(fout)
writer.writerow(["Word", "Count"])
for _ in unique_words:
    writer.writerow([_, unique_words[_]])
    # fout.write("%s\n" % _)
fout.close()
