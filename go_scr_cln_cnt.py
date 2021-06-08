import twint
import time
from collections import Counter
import csv

# Define Variables
twUserArray = ['peteraltmaier', 'AkbulutGokay', 'aggelidis_fdp', 'bela_bach', 'badulrichmartha', 'Thomas_Bareiss', 'BerndBaumannAfD', 'DietmarBartsch', 'nicole_ae_bauer', 'jensbeeck', 'lgbeutin', 'MarcBernhardAfD', 'andreasbleckmdb', 'PeterBoehringer', 'StBrandner', 'JuergenBraunAfD', 'Marcus_Buehl', 'marcobuelow', 'KarambaDiaby', 'ekindeligoez', 'FabioDeMasi', 'MarcusFaber', 'DFoest', 'Erhard_Grundl', 'RonjaKemmer', 'tobiaslindner']
twUserName = ''
twPath = '/tweets_clean.csv'
twCounted = '/word_count.txt'
mostOccurMax = 5

# START LOOP
for index in range(len(twUserArray)):
    twUserName = twUserArray[index]
    print(twUserName)

    # SCRAPER
    c = twint.Config()

    c.Username = twUserName
    #c.Limit = False
    c.Filter_retweets = False
    c.Custom["tweet"] = ["tweet"]
    c.Store_csv = True
    c.Output = twUserName

    twint.run.Profile(c)

    print('#################### 1. COLLECTING DONE ####################')
    time.sleep(1)


    # CLEANER
    with open(twUserName + '/tweets.csv', encoding='utf8') as oldfile, open(twUserName + twPath, 'w', encoding='utf8') as newfile:
        for i, line in enumerate(oldfile):
            if i == 0 or not line.startswith('RT'):
                newfile.write(line)

    print('#################### 2. CLEANING DONE ####################')
    time.sleep(1)


    # COUNTER
    # CONFIG
    csv_file = twUserName + twPath
    unwanted_words = ['rt', '-', '&amp;', '#', 'http://', 'https://', 'die', 'der', 'und', 'für', 'das', 'von', 'in', 'nicht', 'ist', 'den', 'im', 'haben', 'habe', 'ein', 'mit', 'bei', 'an', 'dass', 'sind', 'werden', 'viele', 'schon', 'es', 'dem', 'als', 'des', 'vor', 'auf', 'wurde', 'aus', 'eine', 'was']
    open_csv_list = []

    # Open CSV
    with open(csv_file, 'r', encoding='utf8') as f:
      file = csv.reader(f)
      open_csv_list = list(file)
      open_csv_list = [[x.lower() for x in l] for l in open_csv_list] #Lovercase everything

    # Count the lines in the csv file
    with open(csv_file, 'r', encoding='utf8') as f:
      file = csv.reader(f)
      row_count = sum(1 for row in file) # Count lines in csv file

    # Convert nested list to list
    nn_list = [' '.join([str(c) for c in lst]) for lst in open_csv_list]

    # Split strings for list
    splitted_list = [word for line in nn_list for word in line.split()]

    def remove_all_by_strings(list_obj, strings):
      for string in strings:
        while string in list_obj:
          splitted_list.remove(string)

    remove_all_by_strings(splitted_list, unwanted_words)

    # Pass the split_it list to instance of Counter class.
    count_instance = Counter(splitted_list)

    # most_common() produces k frequently encountered
    # input values and their respective counts.
    most_occur = count_instance.most_common(mostOccurMax)

    print(most_occur)

    # Write the top n of the most occured words
    list_count = open(twUserName + twCounted, "w", encoding="utf8")
    for t in most_occur:
      line_mo = ' '.join(str(x) for x in t)
      list_count.write(line_mo + '\n')
    list_count.close()

    # Append the csv line counter
    with open(twUserName + twCounted, "a", encoding="utf8") as list_count_append:
      list_count_append.write(str(row_count))
    list_count_append.close()


    print(row_count)
    print('#################### 3. FILTERING & COUNTING DONE ####################')
    time.sleep(1)

    #END LOOP
# EOF
