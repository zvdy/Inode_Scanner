# Inode Scanner for Linux

This is a simple tool to scan a directory and list all files with the same inode number. This can be useful to find duplicate files.

## Usage
> **Note:** This tool only works on Linux. If no path is specified, the root directory will be scanned. This can take a while.
```
$ Python3 Scanner.py -f /path/to/file -p /path/to/directory/to/scan
```

## Example

```
$ Python3 Scanner.py -f /home/user/Downloads/hardlink1 -p /home/user
```

Output:

```
/home/user/Downloads/hardlink1
/home/user/Downloads/hardlink2
/home/user/Desktop/hardlink3
```

## Why?
I developed this tool because I wanted to find duplicate files on my system. I found a lot of duplicate files in my Downloads folder. I used this tool to find the duplicate files and then deleted them.

---

Also had the following use case: A friend of mine had a backup script on his Linux server for some DDBB. This script created a hardlink and then zipped the hardlinked so the backup was faster and the DDBB was not corrupted. The problem was that the hardlink was not deleted after the backup was done. So I used this tool to find the hardlink and delete it.

---

Other use case: You can´t create a hardlink on a different partition. So if you are thinking about adding a partition to your system and you want to know if you have hardlinks on your system, you can use this tool to find them.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
