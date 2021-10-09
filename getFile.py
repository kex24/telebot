def getFileText(path, extent, length = 10):
    
    with open(path, 'r') as f:
        content_lines = f.readlines()
        
    nlines = len(content_lines)
    
    if extent == 'cat':
        r = range(nlines)
    elif extent == 'head':
        r = range(min(length, nlines))
    elif extent == 'tail':
        r = range(-min(length, nlines), 0)
    
    output = ''.join([content_lines[i] for i in r])
    
    return output


if __name__ == '__main__':
    test_path = 'test.log'
    test_extent = 'tail'
    print(getFileText(test_path, test_extent, length=5))
    