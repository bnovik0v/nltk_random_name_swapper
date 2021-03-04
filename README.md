# RandomPersonSwapper

RandomPersonSwapper will make random Person swaps in your text. 



## Bulid

```docker build -t name_swapper . ```

## Start

Run sh file with absolute path to file

```sh run.sh /path/to/file```

### Output

Output will be placed in input file folder and looks like that:

| File name | Purpose |
| --- | --- |
|out_filename | text after swaps |
|rules_filename | rules of swapping |

## Example

| Original | Output Text | List of Swap Rules |
| --- | --- | --- |
| Andrew. Phillip. Tom. Sam. Richard Dokkins. | Sam. Phillip. Tom. Andrew. Richard Dokkins. | ['Andrew', 'Sam']]
| Andrew. Phillip. Tom. Sam. Richard Dokkins. | Sam. Phillip. Richard Dokkins. Andrew. Tom. | [['Tom', 'Richard Dokkins'], ['Sam', 'Andrew']] |

<table>
<tr>
<th> Original </th>
<th> Output Text </th>
<th> List of Swap Rules </th>
</tr>
<tr>
<td>
While in France, Christine Lagarde discussed
short-term stimulus efforts in a recent interview
with the Wall Street Journal. While in France,
Anna Mironova discussed short-term stimulus efforts
in a recent interview with the Wall Street Journal.
First up in London will be <b>Riccardo Tisci</b>, onetime
Givenchy darling, favorite of Kardashian-Jenners everywhere,
who returns to the catwalk with men’s and women’s wear after
a year and a half away, this time to reimagine Burberry after
the departure of <b>Christopher Bailey</b>.
<b>Barbara</b> wants to know how could you do it. It's alright.
<b>Jane</b> was mistaken. Sandra. James is her lover.
</td>
<td>
While in France, Christine Lagarde discussed 
short-term stimulus efforts in a recent interview 
with the Wall Street Journal. While in France, 
Anna Mironova discussed short-term stimulus efforts 
in a recent interview with the Wall Street Journal. 
First up in London will be <b>Jane</b>, onetime Givenchy 
darling, favorite of Kardashian-Jenners everywhere,
who returns to the catwalk with men’s and women’s 
wear after a year and a half away, this time to
reimagine Burberry after the departure of <b>Barbara</b>.
<b>Christopher Bailey</b> wants to know how could you 
do it. It's alright. <b>Riccardo Tisci</b> was mistaken. 
Sandra. James is her lover.
</td>
<td>
[['Jane', 'Riccardo Tisci'], ['Barbara', 'Christopher Bailey']]
</td>
</tr>
</table>