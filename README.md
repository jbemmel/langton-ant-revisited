# Revisiting [Langton's Ant](https://en.wikipedia.org/wiki/Langton%27s_ant) using Python

In 1986 computer scientist Chris Langton came up with a way to illustrate the emergence of complex behavior out of a (seemingly) simple set of rules.
His article on ["Studying Artifical Life with Cellular Automata"](https://deepblue.lib.umich.edu/bitstream/2027.42/26022/1/0000093.pdf) describes the details.

![image](https://user-images.githubusercontent.com/2031627/149033490-b0e5f63f-bdb8-483c-a483-51f72a15af3a.png)

# Data structures

The original algorithm uses a (bounded) 2D grid for the virtual ant ('vant'). In this implementation, it is replaced with a 1-dimensional array (implemented as a Python dictionary with integers as keys); directions (N)orth and (S)outh are implemented as increases/decreases of a fixed 'width'; it was found that a width of 48 is minimally required to keep the pattern from interfering with itself.

![image](https://user-images.githubusercontent.com/2031627/149033044-b217e17a-c746-43a9-b3ab-407cae59d653.png)
Sample 10 by 10 array; to go 'North' from 45, subtract 10

# Output: Repeating cycle of 104 steps
First occurence (104) after 10184 iterations, 14 loops highlighted
```
ESESWSENWNENESENWSWNWSENESESENWSWSWNESENWSWSESENWSWNESESENWSWSENWNESWSWSENWNWNENWNESWSESWSENWNENWNWNENES
    -----    ----- -----   ----  ----+++++   ----+++++ -----++++----- -----     -----   -----
```
N: 25
E: 27
S: 27
W: 25

Net displacement: 2*E, 2*S

Alternative RLE: Initial direction, then '1' for right turn or '0' for left turn:
```
10100111100100111100111100101111010000111101101111000010111101111000010111101001100001100111100110100100
     ----     ----  ----    ----  ----++++    ----++++  ---- ----++++  ----      ----    ----
```
(never 5 times in a row the same turn)

## Loop reduction
14 loops collapsed, removing 14*4=56 turns leaving 104-56=48
10100<ins>**1111**</ins>00100**1111**00**1111**0010**1111**01**00001111**0110**11110000**10**1111**0**11110000**10**1111**010011**0000**1100**1111**00110100100
```
10100111100100111100111100101111010000111101101111000010111101111000010111101001100001100111100110100100
101000010000001001011010010010011110000110100100
4 secondary loops, leaving 48-4*4=32:
10110010010110100100100110100100
```

```
ESESWSENWNENESENWSWNWSENESESENWSWSWNESENWSWSESENWSWNESESENWSWSENWNESWSWSENWNWNENWNESWSESWSENWNENWNWNENES
ESESWNENESWNESESWSWSESESWSWNWNENWSESWNENWNWNENES
ESENESESWSWSESESWSWNWNENWNWNENES
```

Impression of the resulting path:
```
                🡢   🡢
		 🡣 🡡 🡣
		  🡢🡢  🡢 
		   🡡🡣  🡣
		  🡢	🡠
		 🡡    🡣
		  🡠  🡠
		   🡡 🡣
		    🡠 🡢
	             🡡 🡣
		    🡢  🡢
		    🡡	 🡣
		     🡠  🡠
		      🡡 🡣
		       🡠
```
