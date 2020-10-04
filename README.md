# godelize


This is a python script that accepts keyboard input and turns that input into a Godel Number.
https://en.wikipedia.org/wiki/G%C3%B6del_numbering

Then it performs a prime factorization of that Godel Number creating an array of prime numbers.  The count of each prime indicates the unicode character.
The script then returns the original input the user entered.

## Motivation

I was reading The Computational Beauty of Nature by Gary William Flake.  Early on in the book the author refers to Godel Numbers
created by the mathematician Kurt Godel. https://en.wikipedia.org/wiki/Kurt_G%c3%b6del

From what I can understand, Godel devised this method to help him in studying Formal Systems and ultimately coming up with his Incompleteness Theorems.
https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems

I was more struck by the Godel Numbering system and the idea of taking a piece of information and whether it be a piece of text, an equation,
a computer program or an image and encoding it into an integer. Even though this integer is huge and unwieldly, it still seems pretty interesting.
Then, the ability to return from that integer to the original piece of information.
I suppose that this is what encryption does but this seemed simpler to me.

I decided to see if I could write a python script to perform this task. I'm not sure what good this is. But it is kind of a cool trick.

If anyone can think of a good way to use this, please help yourself to the source code.


## Usage

At command prompt type: python godelize.py
You will be prompted to enter some text:
![godelTerm1.png](https://github.com/godelize/godelize/blob/main/godelTerm1.png)

Enter some text or equation or whatever (keep in mind that the longer it is, the longer the processe will take):
![godelTerm2.png](https://github.com/godelize/godelize/blob/main/godelTerm2.png)

After some processing, you will presented with:
![godelTerm3.png](https://github.com/godelize/godelize/blob/main/godelTerm3.png)
which will show what you entered, the Godel Number for that text...

At the end, you will be shown the prime factorization of the Godel Number.
Then a list of unicode symbols which is the count of each prime.
Then the original text you entered:
![godelTerm4.png](https://github.com/godelize/godelize/blob/main/godelTerm4.png)

<!--
<details>
<summary>summary</summary>
aaa bbb ccc

</details>
-->
