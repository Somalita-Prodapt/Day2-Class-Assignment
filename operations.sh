
mkdir Backup
mkdir Project


cp file1.txt Backup/

# Move file
mv file2.txt Backup/

# Rename file
mv notes.txt mynotes.txt

# Move renamed file
mv mynotes.txt Project/

# Search for the file
echo "Searching for mynotes.txt..."
find . -name "mynotes.txt"

# Change permission of this script
chmod 755 operations.sh

echo "Script permissions:"
ls -l operations.sh

# Create compressed archive
tar -czvf project_backup.tar.gz Backup Project

# Create extraction folder
mkdir Structure2

# Extract archive into Structure2
tar -xzvf project_backup.tar.gz -C Structure2

# Verify folder structure
echo
echo "Current Structure:"
find .

echo
echo "Extracted Structure:"
find Structure2

echo "Completed Successfully."
