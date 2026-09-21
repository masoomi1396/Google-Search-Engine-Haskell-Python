Amirmohammad Masoumi - 3648672
Jan-Jaap Lankhaar - 3872319

-- Imperative

We only did the 7.1

We implemented the function for search in ordsearch file (both binary and linear). We also implemented a function for sort (merge sort from assignemnt).
In addition, we implemented a function for using a hashtable to find duplicates and removes them (mergeDict)
And at the end, we transfer the dictionary to a list and return it.

Also, in google.py we added a time for checking the amount time that takes to make the search 

 --  Using Binary Search
    Time spent reading text files: 40ms
    Time spent creating search table: 809ms
    Search term: dead
    Time spent to search table: 0ms
    'dead' occurs in ['brian.txt', 'eyre.txt', 'grail.txt']

    --
    Search term: spank
    Time spent to search table: 0ms
    'spank' occurs in ['grail.txt']

    --

    Search term: NO
    Time spent to search table: 0ms
    'NO' does not occur
 
 -- Using Linear search
    Time spent reading text files: 51ms
    Time spent creating search table: 752ms
    Search term: spank
    Time spent to search table: 7ms
    'spank' occurs in ['grail.txt']


-- Functional

We only did the 7.3

We used the mergeSort and dedup function from the assignments to sort and remove duplicated (in both words and filenames) then we Implemented getKeys function where we pass on a pairs and we get all the keys (words) as list of string -> Here we used dedup and mergeSort to firstly sort the keys then remove duplicated ones
Then we used getItems function by passing on a key (only one) and pairs to get all the filename for that key then by using dedup and mergeSort we sort it and removed duplicates
After that we have mergeBackPairs to merge the keys and items as a table then return it (it is for all keys and items) -> we need to pass on all keys and items
In makeTable function we used mergeBackPairs (we needed to pass all the keys and all the items )

Then we implemented three functions to validate the table, isDuplicatedKeys which checks is there any duplicated words in our table, isDuplicatedFilenames which checks based on each key is there any duplicated filename, and lastly noEmptyList which checks is there any empty list (for filenames) for each key

--
    runghc Google.hs 'brian.txt' 'grail.txt' 
    Search term: dead
    ["brian.txt","grail.txt"]
    Search term: spank
    ["grail.txt"]
    Search term: NO
    []
--
    ghci Google.hs  
    quickCheck prop_makeTableValid 
    +++ OK, passed 100 tests.
--