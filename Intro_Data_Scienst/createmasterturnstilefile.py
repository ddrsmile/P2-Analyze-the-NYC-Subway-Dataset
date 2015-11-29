def cmtf(filenames, output_file):
  with open(output_file, 'w') as master_file:
    master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
    for filename in filenames:
      reader = open(filename, 'r')
      for row in reader:
        master_file.write(row)
