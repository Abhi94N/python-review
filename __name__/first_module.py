#print(f"First Module's name: {__name__}")

print("This will always run")

def main():
    print('First module main method')
    print(f"First Module's name: {__name__}")

# when importing first_module, the __name__ is not main and therefore won't print First Module
if __name__ == '__main__':
    main()
else:
    print('Run from Import')