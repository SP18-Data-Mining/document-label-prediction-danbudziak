def compSciArticles(document):
    document = open(document, "r")
    document = document.read()
    documentList = document.split()
    docLength = len(documentList)
    bagOfWords = [ ]
    outputLabel = {}
    artScore = 0
    #Stop words taken from a site that google recommended to find stop words for text mining
    stopWords = ["a","about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
                 "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't",
                 "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he",
                 "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've",
                 "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of",
                 "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "shouldn't",
                 "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll",
                 "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were",
                 "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't",
                 "you", "you'd", "you'll", "you're", "your", "yours", "youself", "yourselves"]
    #Creating labels from the article
    labels = {
              "Computer" : [ 'digital', 'laptop', 'ibm', 'computation', 'software', 'hardware', 'apple', 'Microsoft', 'software'],
              "Degree" : ['Camrbidge Diploma','study','theory','degree','school','engineer','science','algorithm','mathematics','academic'],
              "Machine" : ['screen', 'mouse', 'keyboard', 'laptop', 'webcam', 'hard drive', 'cpu'],
              "Program" : ['design', 'structure', 'web', 'microsoft', 'application', 'machine learning','games', 'programming', 'algorithm'],
              }
              
    #Putting all the words that are not in stopWords into our "bagOfWords"
    for word in documentList:
    	if word not in stopWords:
    		bagOfWords.append(word)
    		bagLength = len(bagOfWords)
    		
    for word in bagOfWords:
        for labelKey in labels:
    	    #Iterating over all the words associated with the label
            associatedToLabel = labels[labelKey]
            if word in associatedToLabel:
                if word in outputLabel.keys():
                    outputLabel[word][0] += 1
                else:
    		    #Update the dictionary
                    data = []
                    data.append(1)
                    data.append(labelKey)
                    entry = { word:data}
                    outputLabel.update(entry)
                    artScore+=1                    
            if artScore > 6:
                artScore=6
    
    return artScore

def diabetesArticles(document):
    document = open(document,"r")
    document = document.read()
    bagOfWords = []
    documentList = document.split()
    outputLabel = {}
    artScore = 0
    docLength = len(documentList)
    #Stop words taken from a site that google recommended to find stop words for text mining
    stopWords = ["a","about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
                 "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't",
                 "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he",
                 "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've",
                 "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of",
                 "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "shouldn't",
                 "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll",
                 "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were",
                 "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't",
                 "you", "you'd", "you'll", "you're", "your", "yours", "youself", "yourselves"]
    labels = {
              "diabetes" : ['disease','blood sugar','glucose','cells','insulin','type'],
              "human" : ['heart','stomach','nerves','kidney','eyes','blood','hormone'],
              "disease" : ['blood', 'heart', 'stroke', 'limb', 'pregnant', 'glucose', 'sugar', 'glucose','diet','exercise'],
    	      "doctor" : [ 'tests','medical', 'professional', 'blood','test']
              }

    #Putting all the words that are not in stopWords into our "bagOfWords"
    for word in documentList :
    	if word not in stopWords :
    		bagOfWords.append(word)
    		bagLength = len(bagOfWords)

    #If the word is in bag of words, we make sure to update our positivity score and also add it to our outputLabel
    for word in bagOfWords:
        for labelKey in labels:
    	    #Iterating over all the words associated with the label
            associatedToLabel = labels[labelKey]
            if word in associatedToLabel:
                if word in outputLabel.keys() :
                    outputLabel[word][0] += 1
                else :
    		    #Update the dictionary
                    data = []
                    data.append(1)
                    data.append(labelKey)
                    entry = { word:data}
                    outputLabel.update(entry)
                    artScore += 1
            if artScore<0:
                artScore=0
    return artScore

def precisionScore(bagLength,docLength):
    precisionScore = (bagLength/float(docLength))*100
    print(int(precisionScore))
    return precisionScore

def main():
    fp = "False Positive"
    tp = "True Positive"
    documents=['unlabeled-1.txt','unlabeled-2.txt','unlabeled-3.txt','unlabeled-4.txt','unlabeled-5.txt','unlabeled-6.txt']
    for theDocs in documents:
        compCount = compSciArticles(theDocs)
        diabetesCount = diabetesArticles(theDocs)
        diff = compCount - diabetesCount
        if diff > 0:           
            score = precisionScore
            if diff >= 3:
                rating = tp
            elif diff < 3:
                rating = fp
            print"The document",theDocs, "is about Computer Science.\n" "The article score is",diff, "\nThis is a",rating
            print"The precision score is:",score,"%"
            if diff < 3:
                print"My results are below confidence"
            elif diff >= 3:
                print"My results are above confidence"
        else :
            if diff > 3:
                rating = tp
            elif diff <= 3:
                rating = fp               
            score = precisionScore
            if diff <= 3:
                artScore=0
                print"--- MY RESULTS ARE NOT CONCLUSIVE ABOUT",theDocs,"---"
            print"The document",theDocs, "is about Diabetes.\n" "The article score is",diff, "\nThis is a",rating
            print"The precision score is:",score,"%"
        print"********************************************************************************"
main()
