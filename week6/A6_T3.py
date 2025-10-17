
def copyFile(srcFile, destFile):
  file_r = open(srcFile, 'r')
  file_w = open(destFile, 'w')
  while True:
    line = file_r.readline()
    if len(line) == 0:
      break
    else:
      file_w.write(line)
  file_r.close()
  file_w.close()


def main():
  print('Program starting.\nThis program can copy a file.')
  srcFile = input("Insert source filename: ")
  destFile = input("Insert destination filename: ")
  copyFile(srcFile, destFile)
  print(f"Reading file '{srcFile}' content.")
  print("File content ready in memory.")
  print(f"Writing content into file '{destFile}'.")
  print("Copying operation complete")
  print("Program ending.")

main()
