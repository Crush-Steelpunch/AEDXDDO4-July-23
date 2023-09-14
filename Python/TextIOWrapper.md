 |  read(self, size=-1, /)
 |      Read at most n characters from stream.
 |
 |      Read from underlying buffer until we have n characters or we hit EOF.
 |      If n is negative or omitted, read until EOF.
 |
 |
 |  readline(self, size=-1, /)
 |      Read until newline or EOF.
 |
 |      Returns an empty string if EOF is hit immediately.
 |
 |  readlines(self, hint=-1, /)
 |      Return a list of lines from the stream.
 |
 |      hint can be specified to control the number of lines read: no more
 |      lines will be read if the total size (in bytes/characters) of all
 |      lines so far exceeds hint.
 |
 |  close(self, /)
 |      Flush and close the IO object.
 |
 |      This method has no effect if the file is already closed.
 |
 |  write(self, text, /)
 |      Write string to stream.
 |      Returns the number of characters written (which is always equal to
 |      the length of the string).
    writelines(self, lines, /)