SRC = $(shell find -iname "*.ino")
OUT = $(patsubst %.ino, %.txt, $(SRC))

all: main
	@

main:
	python arduino_grader.py

clean:
	@rm -f $(OUT)

.PHONY: clean all main