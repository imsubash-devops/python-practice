def update_server_config(file_path,key,value):
     # Open the file in read mode to read its content
    with open(file_path,"r") as file:
            # Read all the lines from the file into a list
        lines = file.readlines()
         # Open the file in write mode to update its content
    with open(file_path, "w") as file:
        # Iterate through each line in the list
        for line in lines:
             # Check if the specified key is present in the line
            if key in line:
                  # If the key is found, update its value and write the modified line
                file.write(key + "=" + value + "\n")
            else:
                # If the key is not found, write the line as it is
                file.write(line)
update_server_config("server.conf","MAX_CONNECTIONS","1000")