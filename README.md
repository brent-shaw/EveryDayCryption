# EveryDayCryption

## Notes

This is not intended as a serious and secure project. More for learning and testing.

## Tools

### encrypt.py

Encrypt one or more files.

```
$ python encrypt.py test1.txt test2.txt test3.txt
```

### decrypt.py

Decrypt one or more files.

```
$ python decrypt.py *
```
NOTE: You can say all. It will only try decrypt files with the '.encrypted' extention. It is important not to rename files that have been encrypted.

### lsd.py

List files with original and encrypted filenames.

This is useful if you do not with to decrypt all files, but only knoe the name of the original file.
```
$ python lsd.py
```
