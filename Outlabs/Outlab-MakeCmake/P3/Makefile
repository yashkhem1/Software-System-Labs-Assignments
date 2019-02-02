all: main
main: main.cpp depend.cpp depend.h
	g++ -c depend.cpp main.cpp
	g++ main.o depend.o depend.h -o main 
.PHONY: skiprebuildh
.PHONY: skiprebuild
skiprebuild:
	make -t
skiprebuildh: main.o depend.cpp depend.h
	touch -amt 197103101513 depend.h
