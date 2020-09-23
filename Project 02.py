#NEIL VARUN NAIDU
#CWID 10468310
#CS 555
#Project 02

#opening GEDCOM file
text_file = open(r'C:\Users\Neil Naidu\Desktop\SampleInput.ged', 'r')
with open('output.txt', 'w') as f:
    #BEGIN
    print("\f", file = f)
    #Traverse File
    for line in text_file:
        print("\n-->", line, file = f)
        #handles empty lines in GEDCOM files
        if line == "\n":
            print("<-- <whitespace>", file = f)
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
            print("<--",level_number,"|", line_tag,"|", file = f)
            #check if the tag is valid according to the overview document
            if level_number == 0 and line_tag == "INDI":
                print("Y", file = f)
            elif level_number == 1 and line_tag == "NAME":
                print("Y", file = f)
            elif level_number == 1 and line_tag == "SEX":
                print("Y", file = f)
            elif level_number == 1 and line_tag == "BIRT":
                print("Y", file = f)
            elif level_number == 1 and line_tag == "DEAT":
                print("Y", file = f)
            elif level_number == 0 and line_tag == "FAM":
                print("Y", file = f)
            elif level_number == 1 and line_tag == "FAMS":
                print("Y", file = f)
            elif level_number == 1 and line_tag == "MARR":
                print("Y", file = f)
            elif level_number == 1 and line_tag == "FAMC":
                print("Y", file = f)
            elif level_number == 0 and line_tag == "HEAD":
                print("Y", file = f)
            elif level_number == 1 and line_tag == "HUSB":
                print("Y", file = f)
            elif level_number == 1 and line_tag == "WIFE":
                print("Y", file = f)
            elif level_number == 0 and line_tag == "TRLR":
                print("Y", file = f)
            elif level_number == 0 and line_tag == "NOTE":
                print("Y", file = f)
            elif level_number == 2 and line_tag == "DATE":
                print("Y", file = f)
            elif level_number == 1 and line_tag == "CHIL":
                print("Y", file = f)
            elif level_number == 1 and line_tag == "DIV":
                print("Y", file = f)
            else:
                print("N", file = f)        
            #print line argument
            print("|",line_arg, file = f)
        #for lines without arguments
        elif len(line_words) == 2:
            #extract the tag of the line
            line_tag = line_words[1].strip()
            level_number = int(line[:1])
            #print the attributes of input line
            print("<--",level_number,"|", line_tag,"|", file = f)
            #check if the tag is valid according to the overview document
            if level_number == 0 and line_tag == "INDI":
                print("Y|", file = f)
            elif level_number == 1 and line_tag == "NAME":
                print("Y|", file = f)
            elif level_number == 1 and line_tag == "SEX":
                print("Y|", file = f)
            elif level_number == 1 and line_tag == "BIRT":
                print("Y|", file = f)
            elif level_number == 1 and line_tag == "DEAT":
                print("Y|", file = f)
            elif level_number == 0 and line_tag == "FAM":
                print("Y|", file = f)
            elif level_number == 1 and line_tag == "FAMS":
                print("Y|", file = f)
            elif level_number == 1 and line_tag == "MARR":
                print("Y|", file = f)
            elif level_number == 1 and line_tag == "FAMC":
                print("Y|", file = f)
            elif level_number == 0 and line_tag == "HEAD":
                print("Y|", file = f)
            elif level_number == 1 and line_tag == "HUSB":
                print("Y|", file = f)
            elif level_number == 1 and line_tag == "WIFE":
                print("Y|", file = f)
            elif level_number == 0 and line_tag == "TRLR":
                print("Y|", file = f)
            elif level_number == 0 and line_tag == "NOTE":
                print("Y|", file = f)
            elif level_number == 2 and line_tag == "DATE":
                print("Y|", file = f)
            elif level_number == 1 and line_tag == "CHIL":
                print("Y|", file = f)
            elif level_number == 1 and line_tag == "DIV":
                print("Y|", file = f)
            else:
                print("N|", file = f)
#end of file
