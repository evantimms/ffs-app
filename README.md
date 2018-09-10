# Fast Fourier Transform Sound Identifier

## Goal: Use the FFS algorithm to split a Sound into its individual frequencies and find its match from a database

### What is a Fourier Tranfrom?

The Fourier Transform, first developed by Joseph Fourier in 1822, is a mathematical operation
that decomposes a function of time into the individual frequencies that combine to make up the complete signal.

### Okay, now what about the FAST Fourier Transform

This is an agorithm that does what the original Fourier Transform sets out to do: Decompose a signal into its individual freqencies.
The most common implemenation of the FFS is the Cooley-Turkey algorithm. This is a divide and conquer algorithm that, by using recursion, 
splits a Discrete Fourier Transform(DTF) into a composition of smaller DFTs which are muliplied by complex roots of unity(explained later) as known as twiddle factors. Other implementations include Rader's algorithm, and Cornelius Lanczo's apporach which uses the Chinese remainder thoreom to factorize the DTF without using twiddle factors.

### Implementation

I have decided to use Python as the language of choice for this project. Python is amazing because it does a great job of simplying very complex code into one or two lines, making your life as programmer much easier. There is also an extensive collection of libraries for Python. The main ones used in this project will be TKinter and SciPy. Tkinter is a simply GUI tool for Python, and NumPy is a fantastic library for everything mathematical and supports everything from probability and statistics equations to, you guessed it, Fourier transforms. I will also be using Matplotlib for pretty graphing.

My goal is to start small, with basic single frequency sounds, and work my way up to more complex sounds with multiple freqencies. An awesome end goal would be a song identifier, hopefully Shazam doesn't sue.

I also would like to try implementing my own version of the FFS, but I will be using SciPy's version first for proof of concept.


