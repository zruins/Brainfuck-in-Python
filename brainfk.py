from os import system

def main(arg):
	output.write("")
	write = lambda content: output.writelines(content)
	inLoop = False
	prompt = arg
	
	pointer = 0

	write("a=[]\nptr=0\niter=0\nwhile iter<64:\n\ta.append(0)\n\titer+=1\n")
	while pointer < len(prompt):
		loopCheck = ("\t" if inLoop else "")
		if prompt[pointer] == "+":
			write(loopCheck + "a[ptr]+=1\n")
		elif prompt[pointer] == "-":
			write(loopCheck + "a[ptr]-=1\n")
		elif prompt[pointer] == ">":
			write(loopCheck + "ptr+=1\n")
		elif prompt[pointer] == "<":
			write(loopCheck + "ptr-=1\n")
		elif prompt[pointer] == "[":
			if loopCheck:
				raise SyntaxError("Nested loops are unsupported")
			write("loopOrigin=ptr\nwhile a[loopOrigin]>0:\n")
			inLoop = True
		elif prompt[pointer] == "]":
			inLoop = False
		elif prompt[pointer] == ".":
			write(loopCheck + "print(chr(a[ptr]))\n")
		elif prompt[pointer] == ",":
			write(loopCheck + "a[ptr]=ord(input()[0])\n")
		pointer += 1
	output.close()

	

if __name__ == "__main__":
	output = open("out.py", "w")
	print("Python Brainf**k Compiler v1.0.0, say \"quit\" to exit")
	while True:
		i = input("$ ")
		if i != "quit":
			main(i)
			system("python3 out.py")
		else:
			break
	system("rm out.py")