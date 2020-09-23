#NEIL VARUN NAIDU
#CWID 10468310
#CS 555
#Project 02

#opening GEDCOM file
text_file = open(r'C:\Users\Neil Naidu\Desktop\SampleInput.ged', 'r')

#BEGIN
print("\f")

#Traverse File
for line in text_file:
    print("\n-->", line, end="")

    #handles empty lines in GEDCOM files
    if line == "\n":
        print("<-- <whitespace>")

    line_words = line.split()

    #handles no tag and whitespaces in individual lines of the GEDCOM file
    if len(line_words) > 2:
        
        level_number = int(line[:1])

        if line_words[2] == "INDI" or line_words[2] == "FAM":
            #extract argument
            line_arg = line.split(' ',2)[1]

            #extract the tag of the line
            line_tag = line_words[2].strip()

        else:
            #extract the tag of the line
            line_tag = line_words[1].strip()

            #extract argument
            line_arg = line.split(' ',2)[2]

        #print the attributes of input line
        print("<--",level_number,"|", line_tag,"|", end="")

        #check if the tag is valid according to the overview document
        if level_number == 0 and line_tag == "INDI":
            print("Y", end="")
        elif level_number == 1 and line_tag == "NAME":
            print("Y", end="")
        elif level_number == 1 and line_tag == "SEX":
            print("Y", end="")
        elif level_number == 1 and line_tag == "BIRT":
            print("Y", end="")
        elif level_number == 1 and line_tag == "DEAT":
            print("Y", end="")
        elif level_number == 0 and line_tag == "FAM":
            print("Y", end="")
        elif level_number == 1 and line_tag == "FAMS":
            print("Y", end="")
        elif level_number == 1 and line_tag == "MARR":
            print("Y", end="")
        elif level_number == 1 and line_tag == "FAMC":
            print("Y", end="")
        elif level_number == 0 and line_tag == "HEAD":
            print("Y", end="")
        elif level_number == 1 and line_tag == "HUSB":
            print("Y", end="")
        elif level_number == 1 and line_tag == "WIFE":
            print("Y", end="")
        elif level_number == 0 and line_tag == "TRLR":
            print("Y", end="")
        elif level_number == 0 and line_tag == "NOTE":
            print("Y", end="")
        elif level_number == 2 and line_tag == "DATE":
            print("Y", end="")
        elif level_number == 1 and line_tag == "CHIL":
            print("Y", end="")
        elif level_number == 1 and line_tag == "DIV":
            print("Y", end="")
        else:
            print("N", end="")
                
        #print line argument
        print("|",line_arg, end="")

    #for lines without arguments
    elif len(line_words) == 2:
        #extract the tag of the line
        line_tag = line_words[1].strip()
        level_number = int(line[:1])
        #print the attributes of input line
        print("<--",level_number,"|", line_tag,"|", end="")
        #check if the tag is valid according to the overview document
        if level_number == 0 and line_tag == "INDI":
            print("Y|", end="")
        elif level_number == 1 and line_tag == "NAME":
            print("Y|", end="")
        elif level_number == 1 and line_tag == "SEX":
            print("Y|", end="")
        elif level_number == 1 and line_tag == "BIRT":
            print("Y|", end="")
        elif level_number == 1 and line_tag == "DEAT":
            print("Y|", end="")
        elif level_number == 0 and line_tag == "FAM":
            print("Y|", end="")
        elif level_number == 1 and line_tag == "FAMS":
            print("Y|", end="")
        elif level_number == 1 and line_tag == "MARR":
            print("Y|", end="")
        elif level_number == 1 and line_tag == "FAMC":
            print("Y|", end="")
        elif level_number == 0 and line_tag == "HEAD":
            print("Y|", end="")
        elif level_number == 1 and line_tag == "HUSB":
            print("Y|", end="")
        elif level_number == 1 and line_tag == "WIFE":
            print("Y|", end="")
        elif level_number == 0 and line_tag == "TRLR":
            print("Y|", end="")
        elif level_number == 0 and line_tag == "NOTE":
            print("Y|", end="")
        elif level_number == 2 and line_tag == "DATE":
            print("Y|", end="")
        elif level_number == 1 and line_tag == "CHIL":
            print("Y|", end="")
        elif level_number == 1 and line_tag == "DIV":
            print("Y|", end="")
        else:
            print("N|", end="")


#end of file