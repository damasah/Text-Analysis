# import libraries

import sys, getopt, re, spacy, os, nltk
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


#Define a function that converts pdf and returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 
   
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in 
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf 
            text = convert(pdfFilename) #get string of text content of pdf
            textFilename = txtDir + pdf + ".txt"
            textFile = open(textFilename, "w") #make text file
            textFile.write(text) #write text to text file
			#textFile.close

# assigning the pdfDir and txtDir directories to avoiding a repeat of the convertion in the subsequent processes
pdfDir = "/Users/elliotdamasah/Documents/School/Thesis/NSA/Data1/pdfToText/Pdf/2012/"
txtDir = "/Users/elliotdamasah/Documents/School/Thesis/NSA/Data1/pdfToText/Text/2012/"

convertMultiple(pdfDir, txtDir)

# Tells you the number of files in the directory that are not hidden
noHidden = [not(mk.startswith('.')) for mk in os.listdir(pdfDir)]
sum(noHidden)

# Tells you the absolute path
os.path.abspath('.'
                
# Tells you the number of items in the directory of the PDF(pdfDir), and it includes hidden files.
len(os.listdir(pdfDir))               
                
# Tells you the number of hidden files in the directory. Note this is based on MacOS's use of dot(.) 
# to prefix hidden files on its operating systems
q = [(f.startswith('.')) for f in (os.listdir(txtDir))];
sum(q)
                
# Tells you the number of files in the directory that are not hidden files.
y = list(filter(lambda f:not f.startswith('.'),(os.listdir(txtDir))));
len(y)
                
# This results in an absolute directory name by concatenating the directory name to the file names.
# And then it shows you the first first in the list
fullLink1 = [(os.path.join(txtDir,lin)) for lin in y]
#fullLink1 = [(txtDir + lin) for lin in y];
fullLink1[:5]
                
# Prints the current directory and the items in it
print(os.getcwd());
# os.listdir('.')
                
# Tells you the absolute paths of the directory
os.path.abspath('.')

# Assigns a directory name to the variable txtDir
# txtDir = "/Users/elliotdamasah/Downloads/Test_for_data/pdfToText/Text/2003/";

# Assigns a list of all the content of the txtDir directory, which now produced in a list
txtDirList = os.listdir(txtDir);

# Tells you the number of files in the list called txtDirList
len(txtDirList)
                
os.chdir('/Users/elliotdamasah/Documents/School/Thesis/NSA/Data1/pdfToText/Text/2003');
os.getcwd()
                
pathA = '/Users/elliotdamasah/Documents/School/Thesis/NSA/Data1/pdfToText/Text/Processed/allCombined/allCombinedWithDates.txt';
                
# A function that extracts the text from each text file in a specified location.

def extractor1(textDirectory):
    
    for x in textDirectory: 
        firstTxtOpen = open(x, 'r')

        readIn = firstTxtOpen.read();

        reTabRep = re.sub(r'\t', ' ', readIn);

        reNewLineRep = re.sub(r'\n', ' ', reTabRep);

        reReturnRep = re.sub(r'\r', ' ', reNewLineRep);
        
        reVerticalLineRep = re.sub(r'\x0b', ' ', reReturnRep);
        
        reFormfeederRep = re.sub(r'\x0c', ' ', reVerticalLineRep);
        
        reReduceSpaceRep = re.sub(r'\s{2,100}',' ', reFormfeederRep);

        try:
            matches = re.search(r'\d+\/\d+\/\d+\s*(.*)\s*\"\(U\/\/FOUO\)', reReduceSpaceRep, re.MULTILINE | re.DOTALL);

            txtExtract = matches.group(0);

            saveTxtExtract = open(pathA, 'a+');

            saveTxtExtract.write(txtExtract);

            saveTxtExtract.close();
        except:
            print('COULD NOT EXTRACT FILE AT INDEX:{}'.format(textDirectory.index(x)), x)
            continue
            
    return
                

# A function to clean a text by doing the following:
# 1. Removing punctuations
# 2. Convert all characters to lower case
def cleaner(textLoad):
    puncPurge = re.sub("[ ',', '\', '.', '!', '?' ]", ' ', textLoad)
    lowerCon = puncPurge.lower();
    return
                
# Find the location of an element in a list:
fullLink1.index('/Users/elliotdamasah/Downloads/Test_for_data/pdfToText/Text/2003/2003-10-21_SIDToday_-_Denial__Deception_Awards.pdf.txt')
                
# Uses regular expressions to target the body section in the newsletters
firstTxtOpen = open(fullLink1[-1], 'r');
#print(firstTxtOpen.read())
reTabRep = re.sub(r'\t', ' ', firstTxtOpen.read());
#reTabRep = re.sub(r'\t', ' ', coco1);
#print(reTabRep)
reNewLineRep = re.sub(r'\n', ' ', reTabRep);
#print(reNewLineRep)
reReduceSpaceRep = re.sub(r'\s{1,100}',' ', reNewLineRep);
#print(reReduceSpaceRep)
#reBodyRep = re.search(r'\d+\/\d+\/\d+\s*(.*)\s*\"\(U\/\/FOUO\)', reReduceSpaceRep, flags=0 );
#print(reBodyRep)
regex = r"\d+\/\d+\/\d+\s*(.*)\s*\"\(U\/\/FOUO\)";
matches = re.search(regex, reReduceSpaceRep, re.DOTALL);
print(matches.group(1))
