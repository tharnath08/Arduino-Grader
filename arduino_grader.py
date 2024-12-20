import os
import subprocess
import serial
import time

# Configuration
arduino_cli_path = "arduino-cli"
board_fqbn = "arduino:avr:uno"


####################
#Update These Fields
####################
port = "COM8"  # Update the COM port of the arduino here
baud_rate = 9600  # Update based on your assignment requirements
timeout = 10  # Time to monitor the serial port for (Max time the arduino takes to print all the data)


#############################
#Function to flash .ino file
#and monitor the serial port
#############################
def flash_and_read(folder_path, sketch_file):

    sketch_path = os.path.join(folder_path, sketch_file)     #Path for the Sketch
    output_file = os.path.splitext(sketch_file)[0] + ".txt"  #Name of the output File
    output_path = os.path.join(folder_path, output_file)     #Path for the output file
    
    # Compile and upload the sketch
    print(f"Flashing {sketch_file}...")
    compile_cmd = [arduino_cli_path, "compile", "--fqbn", board_fqbn, sketch_path]
    upload_cmd = [arduino_cli_path, "upload", "--fqbn", board_fqbn, "--port", port, sketch_path]
    
    try:
        subprocess.run(compile_cmd, check=True)
        subprocess.run(upload_cmd, check=True)
    except subprocess.CalledProcessError as e:
        with open(output_path, "w") as output:
            output.write("Error Flashing File into Arduino\n")
        print(f"Error flashing {sketch_file}: {e}")
        return
    
    time.sleep(2)      #Arduino reset time after flashing

    # Open serial port and read data
    print(f"Reading serial output from {sketch_file}...")
    try:
        with serial.Serial(port, baud_rate, timeout=timeout) as ser:
            serial_data = ""
            start_time = time.time()
            while time.time() - start_time < timeout:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    serial_data += line + "\n"
            
            # Save serial data to text file
            with open(output_path, "w") as output:
                output.write(serial_data)
                print(f"Saved output to {output_path}")
    except Exception as e:
        with open(output_path, "w") as output:
            output.write("Error reading serial data: {e}\n")
        print(f"Error reading serial data: {e}")


#############################
#Function to fetch .ino files
#from the subdirectories
#############################
def process_submissions():
    submissions_folder = os.getcwd()

    for root, _, files in os.walk(submissions_folder):
        for file in files:
            if file.endswith(".ino"):
                flash_and_read(root,file)


if __name__ == "__main__":
    process_submissions()
