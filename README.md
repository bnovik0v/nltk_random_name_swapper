

Build

```docker build -t name_swapper . ```

Start

```sh run.sh /path/to/file```

Output

| file | purpose |
| --- | --- |
|filename_out | text with swapping |
|filename_rules | rules to swap|

Example

| orig | transformed | rules |
| --- | --- | --- |
| Andrew. Phillip. Tom. Sam. Richard Dokkins. | Sam. Phillip. Tom. Andrew. Richard Dokkins. | ['Andrew', 'Sam']]
| Andrew. Phillip. Tom. Sam. Richard Dokkins. | Sam. Phillip. Richard Dokkins. Andrew. Tom. | [['Tom', 'Richard Dokkins'], ['Sam', 'Andrew']] |