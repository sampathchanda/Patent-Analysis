# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:23:08 2016

@author: praneetdutta
"""
def tfidf(abstract):
 numberdocs=len(docs)
    allword={}
    i=0
    logup=np.log(len(docs))
    listofdicts=[]
    for element in docs:
        dictelement={}
        wordinsent=element.split()
        for element1 in wordinsent:
            if element1 in dictelement:
                dictelement[element1]+=1
            else:
                dictelement[element1]=1
        listofdicts.append(dictelement)
        for wordd in dictelement.keys():
            if wordd in allword:
                allword[wordd]+=1
            else:
                allword[wordd]=1
        i+=1
  
    dataa=[]
    xentry=[]
    yentry=[]          
    for word in allword:
        j=0
        for element in docs:
            currentdict=listofdicts[j]
            if word in element:
             if(word in currentdict and word in allword):
               value=float(currentdict[word]*(logup-(np.log(allword[word]))))
               if(value!=0):
                   dataa.append(value)
                   xentry.append(j)
                   yentry.append(allword.keys().index(word))
                   
            j+=1
    all_words=[]
    for element in allword.keys():
        all_words.append(element)
    dataa= np.array(dataa)
    xentry=np.array(xentry)
    yentry=np.array(yentry)        
   
    tfidf=sp.csr_matrix((dataa, (xentry,yentry)))
    return (tfidf)