# Usage:
# Not ready now because of vimrc config. 
# but soon will be working to fix it

.PHONY = all clean

CC = g++ 		# compiler to use

LINKERFLAG = -lm
CFLAGS := -c -Wall
SRCS := $(wildcard *.h)
BINS := $(SRCS: %.h:%)

all: ${BINS}
	./a.out << 

%: %.o
	@echo "Checking.."
	${CC}  $<

%.o: %.c
	@echo "Creating object.."
	${CC}  $<

clean:
	@echo "Cleaning up..."
	rm -rvf *.o ${BINS}
