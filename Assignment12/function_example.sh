#!/bin/bash


print_something () {
echo Hello I am a function
}
print_something
print_something

print_something () {
echo Hello $1
}
print_something Mars
print_something Jupiter
