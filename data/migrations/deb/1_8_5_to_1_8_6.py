import shutil
shutil.copyfile('/home/sovrin/sovrin_backup_1.8.2.zip', '/home/sovrin/backup_proof.zip')
with open('/home/sovrin/.sovrin/migration_proof', 'w') as f:
  f.write('1.5.5')