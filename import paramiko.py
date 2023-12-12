import paramiko

# Function to copy file from Linux to Windows
def copy_file_from_linux_to_windows(linux_host, linux_user, linux_password, linux_file_path, windows_file_path):
    try:
        # Establish SSH connection
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=linux_host, username=linux_user, password=linux_password)

        # SCP file from Linux to Windows
        scp_client = ssh_client.open_sftp()
        scp_client.get(linux_file_path, windows_file_path)
        scp_client.close()

        # Close SSH connection
        ssh_client.close()
        print(f"File copied successfully from {linux_file_path} to {windows_file_path}")
    except Exception as e:
        print(f"Error: {e}")

# Linux and Windows details
linux_host = 'linux_machine_ip_or_hostname'
linux_user = 'your_linux_username'
linux_password = 'your_linux_password'
linux_file_path = '/path/to/your/linux/file.txt'

windows_file_path = r'C:\path\to\your\windows\file.txt'

# Copy file from Linux to Windows
copy_file_from_linux_to_windows(linux_host, linux_user, linux_password, linux_file_path, windows_file_path)