# the BD Install script maker script
# author theDXT

print("Starting the script to make scripts")

from csv import DictReader
# load the csv file with the variables and define it as the list
with open('few_clients2.csv', 'r') as the_list:
    # define new variable to load the list as object mapping
    csv_dict_reader = DictReader(the_list)
    # run a loop for each item in the csv
    for item in csv_dict_reader:
        # make powershell files for each client using the shortname and define it as script
        with open((item['shortname'])+ "_BD_Install.ps1", 'w') as script:
            # define the header comments and load in the client full name
            header_comments = ["# ", (item['client']), " Bit Defender Silent install\n \n"]
            # save the header comments to the file
            script.writelines(header_comments)
            # define the GZID stuff and load in the client keycode for the correct mappings
            GZID = ["# the BitDefender Gravity Zone ID to match the install to the correct customer\n", '$GZID = "GZ_PACKAGE_ID=', (item['Keycode']),'"']
            # save that to the file
            script.writelines(GZID)
            # load the rest of the install script that doesnt change
            source = open("template.txt", "r")
            # loop it for each line because I didnt find another way that worked
            for line in source:
                script.write(line)
print("all done")