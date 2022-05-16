from os import system

def main(arg):
	output.write("")
	write = lambda content: output.writelines(content)
	loops = 0
	prompt = arg
	pointer = 0

	write("outputstr=\"\"\na=[]\nptr=0\niter=0\nwhile iter<64:\n\ta.append(0)\n\titer+=1\n")
	while pointer < len(prompt):
		loopCheck = "\t" * loops
		if prompt[pointer] == "+":
			write(loopCheck + "a[ptr]+=1\n")
		elif prompt[pointer] == "-":
			write(loopCheck + "a[ptr]-=1\n")
		elif prompt[pointer] == ">":
			write(loopCheck + "ptr+=1\n")
		elif prompt[pointer] == "<":
			write(loopCheck + "ptr-=1\n")
		elif prompt[pointer] == "[":
			write(f"loopOrigin{loops}=ptr\nwhile a[loopOrigin{loops}]>0:\n")
			loops += 1
		elif prompt[pointer] == "]":
			loops -= 1
		elif prompt[pointer] == ".":
			write(loopCheck + "outputstr+=str(chr(a[ptr]))\n")
		elif prompt[pointer] == ",":
			write(loopCheck + "a[ptr]=ord(input()[0])\n")
		pointer += 1
	write("print(outputstr)")
	output.close()

	

if __name__ == "__main__":
	print("Python Brainf**k Compiler v1.2.2, say \"quit\" to exit")
	while True:
		i = input("$ ")
		if i != "quit":
			output = open("out", "w")
			if i[0] != "*":
				main(i)
			else:
				lis = list(i)
				lis.remove("*")
				f = open("".join(lis))
				main(f.read())
				f.close()
			system("python3 out")
			system("rm out")
		else:
			break
