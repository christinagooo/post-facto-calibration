This folder is for files related to coded apertures

The 4 files within this folder are variations of each other. 
They all differ in terms of the count, or shadow cast from the mask, resulting in different cross correlation graphs. 
All of them share the same mask, which is where they are similar

After running any one of the program files, 3 graphs will automatically be generated. 
The first graph is the mask, the second graph is the counts (cast shadow), and the third is the cross correlation graph between the mask and shadow. 

Detail as to where the 4 files differ:

"codedaperture-perfect.py" has its counts graph as a perfect shadow of the mask

"codedaperture-imperfect.py" has its counts graph as essentially a perfect shadow of the mask, but x-rays bleed into adjacent bins

"codedaperture-zeroShifted.py" has its counts graph as a perfect shadow of the mask, but shifted left or right to varying degrees

"codedaperture-randomcount.py" has its count graph completely random generated and not related to the mask in any way

To run the files (Make sure you are in the codedaperture directory):

```
python3 codedaperture-perfect.py
python3 codedaperture-imperfect.py
python3 codedaperture-zeroShifted.py
python3 codedaperture-randomcount.py
```