import utils as u

filename = u.get_file()
djt = u.TwitterCorpus(filename,None)
print("\nclean_text")
djt.clean_text()
print("\ntokenize_tag")
djt.tokenize_tag()
print("\nconvert time")
djt.convert_time()
