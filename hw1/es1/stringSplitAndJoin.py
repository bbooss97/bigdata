

def split_and_join(line):
    #return line.replace(" ","-")
    return "-".join(line.split())
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)