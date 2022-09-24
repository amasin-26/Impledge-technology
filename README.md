<h1>Word Composition Problem</h1>
  <p>A compounded word is one that can be constructed by combining (concatenating) shorter words
  also found in the same file</p>
  
<h1>Input file</h1>
<ol>
<li>Input_01.txt</li>
<li>Input_02.txt</li>
</ol>

<h1>Output</h1>
<ul>
<li>Input_01.txt</li>

1. Longest Compound Word: ratcatdogcat<br>
2. Second Longest Compound Word: catsdogcats


 <li>Input_02.txt </li>
 
1. Longest Compound Word: ethylenediaminetetraacetates<br>
2. Second Longest Compound Word: electroencephalographically
 
</ul>

<h2>Approach</h2>
Used Trie data structure its a special tree that stores strings. 
Maximum number of children of a node is equal to size of alphabet. 
Trie supports search, insert and delete operations in O(k) time where 
k is length of word.
<br>
First read the file and then make the Trie by calling Trie() function . 
After making trie we have to check the longest compund word by calling 
LongestCompoundWord() fuction . <br>
After getting the longest compund word remove the longest word and again 
call the function for second longest compund word .

  
  
