# ArduinoGrader

## Usage
Install arduino-cli from [Here](https://arduino.github.io/arduino-cli/1.1/installation/)

Open Command Prompt and install the arduino:avr platform:

    arduino-cli core install arduino:avr

Clone the repo and navigate to the folder.

https://github.com/tharnath08/ArduinoGrader

Edit the values in the these [lines](https://github.com/tharnath08/ArduinoGrader/blob/main/arduino_grader.py#L11-L17) based on the assignment.

Install the required packages:

    pip install -r requirements.txt

Run the grader script by:

    python arduino_grader.py

or just:

    make

The grader will flash all the code and monitor the serial monitor one by one. Wait till the script ends.

The .txt file with the output will be generated in the same folder as the .ino file.

Replace the submissions folder with the actual submission.

.ino file should have the same name as it folder for this script to work just like arduino IDE.

To clear the generated output, use:

    make clean