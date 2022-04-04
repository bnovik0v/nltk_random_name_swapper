# RandomPersonSwapper

RandomPersonSwapper swaps names in text randomly. 



## Bulid

```docker build -t name_swapper . ```

## Start

Run sh file with absolute path to file

```sh run.sh /path/to/file```

### Output

Output will be placed right next to input file and look like that:

| File name | Purpose |
| --- | --- |
|out_{filename} | text after swaps |
|rules_{filename} | rules of swapping |

## Example

| Original | Output Text | List of Swap Rules |
| --- | --- | --- |
| Andrew. Phillip. Tom. Sam. Richard Dokkins. | Andrew. Tom. Phillip. Richard Dokkins. Sam. | [['Tom', 'Phillip'], ['Sam', 'Richard Dokkins']]
| Andrew. Phillip. Tom. Sam. Richard Dokkins. | Sam. Phillip. Richard Dokkins. Andrew. Tom. | [['Tom', 'Richard Dokkins'], ['Sam', 'Andrew']] |

<table>
<tr>
<th> Original </th>
<th> Output Text </th>
<th> List of Swap Rules </th>
</tr>
<tr>
<td>
While in France, <b>Christine Lagarde</b> discussed
short-term stimulus efforts in a recent interview
with the Wall Street Journal. While in France,
<b>Anna Mironova</b> discussed short-term stimulus efforts
in a recent interview with the Wall Street Journal.
First up in London will be <b>Riccardo Tisci</b>, onetime
Givenchy darling, favorite of Kardashian-Jenners everywhere,
who returns to the catwalk with men’s and women’s wear after
a year and a half away, this time to reimagine Burberry after
the departure of <b>Christopher Bailey</b>.
<b>Barbara</b> wants to know how could you do it. It's alright.
<b>Jane</b> was mistaken. <b>Sandra</b>. <b>James</b> is her lover.
</td>
<td>
While in France, <b>Sandra</b> discussed short-term stimulus
efforts in a recent interview with the Wall Street
Journal. While in France, <b>Barbara</b> discussed short-term
stimulus efforts in a recent interview with the Wall 
Street Journal. First up in London will be <b>Christopher
Bailey</b>, onetime Givenchy darling, favorite of
Kardashian-Jenners everywhere, who returns to the
catwalk with men’s and women’s wear after a year
and a half away, this time to reimagine Burberry
after the departure of <b>Riccardo Tisci</b>.
<b>Anna Mironova</b> wants to know how could you do
it. It's alright. <b>James</b> was mistaken. <b>Christine
Lagarde</b>. <b>Jane</b> is her lover.

</td>
<td>
[['Christopher Bailey', 'Riccardo Tisci'], ['Jane', 'James'], ['Anna Mironova', 'Barbara'], ['Sandra', 'Christine Lagarde']]
</td>
</tr>
</table>
