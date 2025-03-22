# Octaprobe
Yet Another Vulnerability Scanner

### Lab Setup

1. Install Virtualization Software
- Go to the [VirtualBox download page](https://www.virtualbox.org/wiki/Downloads).
- Choose the appropriate version for your operating system (Windows, macOS, Linux).
- Download the installer file.
- Run the installer and follow the on-screen instructions to complete the installation.
- Once installed, open VirtualBox to ensure it is working correctly.

2. Install Kali Linux using VirtualBox
- Go to the [Kali Linux download page](https://www.kali.org/get-kali/#kali-virtual-machines).
- Under the "Virtual Machines" section, choose the VirtualBox option.
- Download the appropriate image for your system architecture (64-bit or 32-bit).
- Open VirtualBox and click on `File` > `Import Appliance`.
- Browse to the downloaded Kali Linux image file and select it.
- Follow the prompts to import the virtual machine.
- Once the import is complete, start the Kali Linux virtual machine from the VirtualBox Manager.

3. Install Metasploitable2
- Go to the [Metasploitable2 download page](https://sourceforge.net/projects/metasploitable/files/Metasploitable2/).
- Click on the download link to get the Metasploitable2 zip file.
- Extract the downloaded zip file to a location of your choice.
- Open VirtualBox and click on `File` > `Import Appliance`.
- Browse to the extracted Metasploitable2 `.ova` file and select it.
- Follow the prompts to import the virtual machine.
- Once the import is complete, start the Metasploitable2 virtual machine from the VirtualBox Manager.

4. Verify Setup
- Start both the Kali Linux and Metasploitable2 virtual machines in VirtualBox.
- In Kali Linux, open a terminal window.
- Determine the IP address of the Metasploitable2 machine by logging into it and running the command `ifconfig` or `ip a`.
- In the Kali Linux terminal, use the `ping` command followed by the IP address of the Metasploitable2 machine. For example:
    ```sh
    ping 192.168.1.100
    ```
- If the network is configured correctly, you should see replies from the Metasploitable2 machine.
- Press `Ctrl + C` to stop the ping command.

5. Configure API Key
a. For Kali Linux:
- Open a terminal in your Kali Linux virtual machine.
- Edit the `.bashrc` file to add the API key as an environment variable:
    ```sh
    nano ~/.bashrc
    ```
- Add the following line at the end of the file, replacing `YOUR_API_KEY` with your actual API key:
    ```sh
    export VULNERS_API_KEY=<YOUR_API_KEY>
    ```
- Save the file and exit the editor by pressing `Ctrl + X`, then `Y`, and `Enter`.
- Apply the changes by sourcing the `.bashrc` file:
    ```sh
    source ~/.bashrc
    ```
- Verify that the environment variable is set correctly:
    ```sh
    echo $VULNERS_API_KEY
    - You should see your API key printed in the terminal.

b. For Windows:
- Open the Start Menu and search for "Environment Variables".
- Click on "Edit the system environment variables".
- In the System Properties window, click on the "Environment Variables" button.
- In the Environment Variables window, under the "User variables" section, click on "New".
- In the "New User Variable" dialog, enter `VULNERS_API_KEY` as the variable name and your actual API key as the variable value.
- Click "OK" to save the new variable.
- Close all remaining windows by clicking "OK".
- Open a new Command Prompt window to apply the changes.
- Verify that the environment variable is set correctly:
    ```sh
    echo %VULNERS_API_KEY%
    ```
- You should see your API key printed in the terminal.


### Environment Setup

1. Download the Project
- Open a terminal in your Kali Linux virtual machine.
- Ensure you have `git` installed by running:
    ```sh
    sudo apt-get update
    sudo apt-get install git
    ```
- Navigate to the directory where you want to clone the repository:
    ```sh
    cd /path/to/your/directory
    ```
- Clone the repository using the following command:
    ```sh
    git clone https://github.com/NONAN23x/Octaprobe.git
    ```
- Navigate into the cloned repository directory:
    ```sh
    cd Octaprobe
    ```
- Verify the contents of the repository:
    ```sh
    ls
    ```
- You have successfully cloned the repository into your Kali Linux machine.

2. Install Dependencies
a. For Kali Linux:
- Ensure you have `pip` installed by running:
    ```sh
    sudo apt-get install python3-pip
    ```

b. For Windows:
- Open a Command Prompt window.
- Install the required Python packages using `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Scanner