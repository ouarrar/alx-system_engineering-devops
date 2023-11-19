#alx-system_engineering-devops/command_line_for_the_win

step 1 : navigate to the directory screenshots in local machine :
		 cd ~/Desktop/screenshots
step 2 : Establish a connection to the sandbox environment : 
		 sftp <username>@<hostname>
step 3 : navigate to the directory where you want to upload the screenshots
         cd alx-system_engineering-devops/command_line_for_the_win/
step 4 : upload file 0-first_9_tasks.png
         put 0-first_9_tasks.png
step 5 : confirm that the screenshots have been successfully transferred by checking the sandbox directory.
         ls -l
